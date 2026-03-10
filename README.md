# doprax-news-monitor
Deployment, hosting, privacy, dev infrastructure, and self-hosting.

# Doprax News Monitor

Automated daily fetcher of cloud/VPS/PaaS/news relevant to Doprax using GitHub Actions + RSS.

### What it does
- Runs every day at 8:00 UTC
- Pulls from selected RSS feeds (see `feeds.txt`)
- Filters for keywords like "Heroku alternative 2026", "VPS unlimited traffic", "Hetzner price", "V2Ray VPS", etc.
- Saves filtered items to `news/latest.json` and a human-readable `news/summary.md`
- Commits changes automatically → creates history of news over time

### How to use / view
- Check `news/summary.md` for the latest digest (viewable directly on GitHub)
- Or browse commit history for past days
- (Optional) Enable GitHub Pages on the `news` folder for a simple static page

### Setup
1. Fork or clone this repo
2. Add/edit `feeds.txt` with RSS URLs
3. Adjust keywords in `fetch_news.py`
4. Workflow runs on schedule (or trigger manually via workflow_dispatch)

Questions? Open an issue.

Last updated: March 2026
