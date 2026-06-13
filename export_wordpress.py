#!/usr/bin/env python3

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup


SITE = "technicloud.wordpress.com"
API_BASE = f"https://public-api.wordpress.com/rest/v1.1/sites/{SITE}/posts/"
OUTPUT_DIR = Path("markdown")


def curl_json(url: str) -> dict:
    result = subprocess.run(
        ["curl", "-L", "--silent", "--show-error", "--fail", url],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def iter_posts() -> Iterable[dict]:
    next_page = ""
    while True:
        url = f"{API_BASE}?number=100"
        if next_page:
            url += f"&page_handle={next_page}"
        payload = curl_json(url)
        yield from payload.get("posts", [])
        next_page = payload.get("meta", {}).get("next_page")
        if not next_page:
            break


def clean_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for wrapper in soup.find_all(["div", "figure"]):
        wrapper.unwrap()

    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr not in {"href", "src", "alt"}:
                del tag.attrs[attr]

    return str(soup)


def html_to_markdown(html: str) -> str:
    result = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=html,
        text=True,
        capture_output=True,
        check=True,
    )
    text = result.stdout.strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text + "\n"


def yaml_escape(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def list_term_names(post: dict, key: str) -> list[str]:
    items = post.get(key, {})
    return [item["name"] for item in items.values()]


def build_front_matter(post: dict) -> str:
    categories = list_term_names(post, "categories")
    tags = list_term_names(post, "tags")
    date = post["date"]
    modified = post["modified"]
    lines = [
        "---",
        f'title: {yaml_escape(post["title"])}',
        f"date: {yaml_escape(date)}",
        f"modified: {yaml_escape(modified)}",
        f'slug: {yaml_escape(post["slug"])}',
        f'url: {yaml_escape(post["URL"])}',
        f'author: {yaml_escape(post["author"]["name"])}',
    ]
    if categories:
        lines.append("categories:")
        lines.extend(f"  - {yaml_escape(name)}" for name in categories)
    else:
        lines.append("categories: []")
    if tags:
        lines.append("tags:")
        lines.extend(f"  - {yaml_escape(name)}" for name in tags)
    else:
        lines.append("tags: []")
    lines.append("---")
    return "\n".join(lines)


def output_name(post: dict) -> str:
    dt = datetime.fromisoformat(post["date"])
    return f"{dt:%Y-%m-%d}-{post['slug']}.md"


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    exported = 0
    for post in iter_posts():
        if post.get("status") != "publish":
            continue
        front_matter = build_front_matter(post)
        body = html_to_markdown(clean_html(post.get("content", "")))
        output = OUTPUT_DIR / output_name(post)
        output.write_text(front_matter + "\n\n" + body, encoding="utf-8")
        exported += 1

    stamp = datetime.now(timezone.utc).isoformat()
    manifest = {
        "site": SITE,
        "exported_at": stamp,
        "output_dir": str(OUTPUT_DIR),
        "post_count": exported,
    }
    (OUTPUT_DIR / "_export_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Exported {exported} posts to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
