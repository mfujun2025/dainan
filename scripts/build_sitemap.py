#!/usr/bin/env python3
# 自动生成 sitemap.xml
# 首页(priority 1.0) 永远第一，其后按文件名倒序列出 news/*.html
import glob, html, os, re
from datetime import datetime, timezone

BASE = "https://xn--6krt95a.cn"
SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 仓库根
NEWS_DIR = os.path.join(SRC, "news")
SITEMAP = os.path.join(SRC, "sitemap.xml")

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
TAG_RE = re.compile(r"<[^>]+>")

def fetch_title(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        m = TITLE_RE.search(raw)
        if m:
            t = TAG_RE.sub("", m.group(1)).replace("| 戴南.cn", "").strip()
            return html.escape(t)
    except Exception:
        pass
    return os.path.basename(path)

def latest_mtime(files):
    try:
        return max(os.path.getmtime(f) for f in files)
    except Exception:
        return 0

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

files = sorted(glob.glob(os.path.join(NEWS_DIR, "*.html")), reverse=True)

urls = []
urls.append(('BASE', BASE + "/", 1.0, today))
for f in files:
    name = os.path.basename(f)
    title = fetch_title(f)
    urls.append((title, BASE + "/news/" + name, 0.8, today))

lines = []
lines.append('<?xml version="1.0" encoding="UTF-8"?>')
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
for _, loc, pri, lastmod in urls:
    lines.append('  <url>')
    lines.append('    <loc>%s</loc>' % loc)
    lines.append('    <lastmod>%s</lastmod>' % lastmod)
    lines.append('    <changefreq>%s</changefreq>' % ('weekly' if pri >= 1.0 else 'monthly'))
    lines.append('    <priority>%s</priority>' % str(pri))
    lines.append('  </url>')
lines.append('</urlset>')
content = "\n".join(lines) + "\n"

with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write(content)

print("sitemap.xml 已生成，共 %d 个 URL" % len(urls))
for _, loc, _, _ in urls:
    print("  " + loc)
