import feedparser
import os
from datetime import datetime

keywords = open("keywords.txt").read().lower().splitlines()
feeds = open("feeds.txt").read().splitlines()

new_items = []

for feed in feeds:
    parsed = feedparser.parse(feed)

    for entry in parsed.entries:
        text = (entry.title + " " + entry.get("summary","")).lower()

        if any(k in text for k in keywords):
            date = entry.get("published","")
            item = f"- {date} — [{entry.title}]({entry.link})"
            new_items.append(item)

# remove duplicates
new_items = list(dict.fromkeys(new_items))

# read existing README
if os.path.exists("README.md"):
    with open("README.md") as f:
        content = f.read()
else:
    content = ""

start_marker = "<!-- NEWS START -->"
end_marker = "<!-- NEWS END -->"

if start_marker in content:
    old_section = content.split(start_marker)[1].split(end_marker)[0]
    old_items = [line.strip() for line in old_section.split("\n") if line.strip()]
else:
    old_items = []

combined = new_items + old_items
combined = list(dict.fromkeys(combined))  # deduplicate

# keep latest 100
combined = combined[:100]

news_block = "\n".join(combined)

new_content = f"""# Doprax News Monitor

Automated ecosystem news relevant to Doprax users.

Last update: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}

## Latest Signals

{start_marker}
{news_block}
{end_marker}
"""

with open("README.md","w") as f:
    f.write(new_content)
