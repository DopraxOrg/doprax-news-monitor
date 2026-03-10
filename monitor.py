import feedparser
from datetime import datetime

keywords = open("keywords.txt").read().lower().splitlines()
feeds = open("feeds.txt").read().splitlines()

results = []

for feed in feeds:
    parsed = feedparser.parse(feed)

    for entry in parsed.entries:
        text = (entry.title + " " + entry.get("summary","")).lower()

        if any(k in text for k in keywords):
            results.append(f"- [{entry.title}]({entry.link})")

results = list(dict.fromkeys(results))[:20]

with open("README.md", "w") as f:
    f.write("# Doprax News Monitor\n\n")
    f.write("Automated ecosystem news relevant to Doprax users.\n\n")
    f.write(f"Last update: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n\n")
    f.write("## Latest Signals\n\n")

    for r in results:
        f.write(r + "\n")
