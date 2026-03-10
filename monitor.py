import feedparser

keywords = open("keywords.txt").read().lower().splitlines()
feeds = open("feeds.txt").read().splitlines()

results = []

for feed in feeds:
    parsed = feedparser.parse(feed)

    for entry in parsed.entries:
        text = (entry.title + " " + entry.get("summary","")).lower()

        if any(k in text for k in keywords):
            results.append(f"- [{entry.title}]({entry.link})")

with open("news.md", "w") as f:
    f.write("# Doprax Ecosystem News\n\n")
    for r in results[:50]:
        f.write(r + "\n")
