# Site

Personal blog and portfolio. Built with [Hugo](https://gohugo.io/) and the [hugo-blog-awesome](https://github.com/hugo-sid/hugo-blog-awesome) theme. Hosted on GitHub Pages.

---

## Local development

```bash
hugo server
```

Open http://localhost:1313 in your browser. The site hot-reloads on save.

---

## Writing a new blog post

1. Create a new file in `content/en/posts/`:

```bash
hugo new content en/posts/YYYY-MM-DD-your-post-title.md
```

2. Edit the frontmatter at the top of the file:

```yaml
---
title: "Your Post Title"
date: 2026-06-13
slug: "your-post-title"
categories:
  - "Engineering Leadership"
---
```

3. Write your post below the `---` in Markdown.

4. Preview locally with `hugo server`, then deploy (see below).

**Category suggestions** (keep consistent for filtering):
- Engineering Leadership
- Developer Platforms
- Technical Craft
- DevOps
- Architecture

---

## Deploying to GitHub Pages

### First-time setup

1. Create a GitHub repository named `rfitzhugh.github.io` (must match your GitHub username exactly).

2. Add a GitHub Actions workflow file at `.github/workflows/deploy.yml`:

```yaml
name: Deploy Hugo site

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true
      - uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: 'latest'
          extended: true
      - uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

3. Push the repo to GitHub:

```bash
git remote add origin git@github.com:rfitzhugh/rfitzhugh.github.io.git
git push -u origin main
```

4. In your GitHub repo settings → Pages → set source to the `gh-pages` branch.

After this, every push to `main` will automatically build and deploy the site.

---

## Adding a custom domain

Once you've purchased a domain:

1. In `hugo.toml`, update `baseURL`:

```toml
baseURL = 'https://yourdomain.com/'
```

2. Create a file called `CNAME` in the `static/` folder containing just your domain:

```
yourdomain.com
```

3. In your domain registrar's DNS settings, add:
   - An `A` record pointing to GitHub Pages IPs:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`
   - Or a `CNAME` record pointing `www` to `rfitzhugh.github.io`

4. In your GitHub repo settings → Pages → add your custom domain and enable "Enforce HTTPS".

DNS changes can take up to 24 hours to propagate.

---

## Adding a Projects section

When you're ready to add projects:

1. Create the projects content directory:

```bash
mkdir -p content/en/projects
```

2. Create an index file at `content/en/projects/_index.md`:

```yaml
---
title: "Projects"
description: "Things I've built"
---
```

3. Add individual project files at `content/en/projects/project-name.md`:

```yaml
---
title: "Project Name"
date: 2026-01-01
description: "One-line description"
link: "https://github.com/rfitzhugh/project"
---

What it is, why you built it, what you learned.
```

4. Add Projects to the nav in `hugo.toml`:

```toml
[[Languages.en-gb.menu.main]]
  pageRef="projects"
  name = 'Projects'
  url = '/projects/'
  weight = 25
```

5. You'll need a custom list layout for projects since the theme doesn't include one by default. Create `layouts/projects/list.html` modelled on the posts list, or use the theme's default list layout as a starting point.

---

## Updating the theme

The theme is included as a git submodule. To update it:

```bash
git submodule update --remote themes/hugo-blog-awesome
```

Test locally before pushing — theme updates occasionally include breaking changes.

---

## Key files

| File | Purpose |
|------|---------|
| `hugo.toml` | Site config — title, baseURL, nav, social links, author bio |
| `content/en/posts/` | Blog posts (Markdown) |
| `content/en/about/_index.md` | About page content |
| `assets/images/logo-light.png` | Logo shown in light mode |
| `assets/images/logo-dark.png` | Logo shown in dark mode |
| `assets/sass/_custom.scss` | Custom CSS overrides |
| `layouts/_partials/header.html` | Nav/header override |
| `static/` | Static files copied as-is (e.g. CNAME for custom domain) |
