#!/usr/bin/env python3
"""Render the public README through GitHub's Markdown API for a local preview.

Requires Python 3 and network access. Does not publish or modify GitHub content.
The output uses GitHub-style CSS; GitHub's surrounding UI may differ.
"""
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '.preview'
OUT.mkdir(exist_ok=True)
request = Request(
    'https://api.github.com/markdown',
    data=json.dumps({'text': (ROOT / 'README.md').read_text(), 'mode': 'gfm', 'context': 'ROYIANS/ROYIANS'}).encode(),
    headers={'Content-Type': 'application/json', 'User-Agent': 'royians-profile-preview'},
)
with urlopen(request, timeout=30) as response:
    body = response.read().decode()
(OUT / 'readme.html').write_text(body)
with urlopen('https://raw.githubusercontent.com/sindresorhus/github-markdown-css/main/github-markdown.css', timeout=30) as response:
    (OUT / 'github-markdown.css').write_bytes(response.read())

# GitHub resolves user-content anchors in its own page router; mirror that locally.
for anchor in ['selected-work', 'the-workbench']:
    body = body.replace(f'href="#{anchor}"', f'href="#user-content-{anchor}"')

template = '''<!doctype html>
<html lang="zh-CN">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>ROYIANS · Profile preview</title>
<base href="../">
<link rel="stylesheet" href=".preview/github-markdown.css">
<style>
body { margin: 0; background: #fff; color: #1f2328; }
.shell { max-width: 894px; margin: 40px auto; padding: 24px 32px; border: 1px solid #d1d9e0; border-radius: 8px; }
.label { font: 12px ui-monospace, monospace; margin: 0 0 24px; color: #59636e; }
.markdown-body { font-size: 16px; }
@media (prefers-color-scheme: dark) {
    body { background: #0d1117; color: #f0f6fc; }
    .shell { border-color: #3d444d; }
    .label { color: #9198a1; }
}
@media (max-width: 600px) {
    .shell { margin: 0; padding: 20px 16px; border: 0; border-radius: 0; }
    .label { font-size: 11px; }
}
</style>
<main class="shell"><div class="label">ROYIANS / README.md</div>
<article class="markdown-body">CONTENT</article></main>
</html>
'''
(OUT / 'index.html').write_text(template.replace('CONTENT', body))
print(f'Preview: {(OUT / "index.html").as_uri()}')
