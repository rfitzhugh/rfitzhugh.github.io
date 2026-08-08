# Debt

Known gaps and cleanup for this Hugo site (`hugo-blog-awesome` on GitHub Pages).

## Product / content

| Priority | Item | Estimate | Notes |
| --- | --- | --- | --- |
| 🔴 | Tighten homepage About signal | 1 hr | `content/en/pages/about.md` already exists and is linked in nav, but the home bio in `hugo.toml` (`params.author`) is only name + one line, with no avatar. Make the first-screen “who is this” clearer (short bio, optional avatar via `params.author.avatar`). |
| 🟠 | Add Talks page | 1–2 hr | No talks content or nav entry yet. Mirror the Projects pattern in the README: `content/en/talks/`, list layout if needed, then add a `menu.main` entry in `hugo.toml`. |
| 🟠 | Surface LinkedIn + GitHub in nav (not only footer) | 30 min | `[[params.socialIcons]]` already has GitHub + LinkedIn and the footer renders them. Nav (`layouts/_partials/header.html`) is Home / Posts / About only — add social links there (and keep `click_social` analytics working). |
| 🟡 | Add Projects section | 2–3 hr | Documented in README but not started. Needs `content/en/projects/`, nav entry, and likely `layouts/projects/list.html`. |
| 🟡 | Clean up post categories | 1 hr | README suggests a short set (Engineering Leadership, Developer Platforms, Technical Craft, DevOps, Architecture). Live posts still use Leadership, Mentorship, Terraform, Cloud, Automation, Design Patterns, and some duplicates. Normalize for filtering. |

## Site polish

| Priority | Item | Estimate | Notes |
| --- | --- | --- | --- |
| 🟠 | Fix About URL to `/about/` | 30 min | Nav points at `/pages/about/` because the file lives under `content/en/pages/`. Prefer `/about/` (aliases or move content) so the path matches the label. |
| 🟡 | Custom domain | 1 hr | Steps are in the README; not configured yet (`baseURL` is still `https://rfitzhugh.github.io/`, no `static/CNAME`). |
| 🟢 | Author identity beyond “RF” | 30 min | Site title, webmanifest, and copyright all use “RF”. Decide whether full name should appear in metadata / footer / About. |

## Repo hygiene

| Priority | Item | Estimate | Notes |
| --- | --- | --- | --- |
| 🟠 | Stop tracking built `public/` | 30 min | ~145 generated files are committed; deploys already publish from CI to `gh-pages`. Add `public/` to `.gitignore` and remove it from git. |
| 🟢 | Ignore local junk | 15 min | `.DS_Store` files still show up under `content/`; tighten `.gitignore` (`**/.DS_Store`, `resources/_gen/`). |
| 🟢 | Retire or document `export_wordpress.py` | 15 min | Looks like a one-off migration helper at the repo root. Keep with a note, or remove if unused. |

## Done / already in place

- About page content (`content/en/pages/about.md`)
- Footer social icons (GitHub, LinkedIn, RSS) via `hugo.toml`
- GA4 + custom events (`assets/js/analytics.js`, documented in README)
- Deploy workflow (`.github/workflows/deploy.yml` → `gh-pages`)
