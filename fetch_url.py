#!/usr/bin/env python3
"""Fetch URLs with User-Agent Velocity/1. Saves to grabbed scripts/. Loops until you enter nothing or quit."""

import urllib.request
import urllib.error
import sys
import os
import re

USER_AGENT = "Velocity/1"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grabbed scripts")


def fetch_one(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    body = None
    content_type = ""

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read()
            content_type = resp.headers.get("Content-Type", "").split(";")[0].strip().lower()
    except urllib.error.HTTPError as e:
        body = e.read()
        content_type = e.headers.get("Content-Type", "").split(";")[0].strip().lower()
        print(f"HTTP {e.code}: {e.reason}", file=sys.stderr)
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}", file=sys.stderr)
        return
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return

    if body is None:
        return

    try:
        text = body.decode("utf-8", errors="replace")
    except Exception:
        text = body.decode("latin-1", errors="replace")
    print(text)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    host = url.split("/")[2] if "/" in url[8:] else "out"
    safe_name = re.sub(r"[^\w\-\.]", "_", host)
    ext = ".html" if "html" in content_type else ".txt" if "text" in content_type else ".bin"
    path = os.path.join(OUTPUT_DIR, safe_name + ext)
    if os.path.exists(path):
        base, ex = os.path.splitext(path)
        i = 1
        while os.path.exists(f"{base}_{i}{ex}"):
            i += 1
        path = f"{base}_{i}{ex}"

    with open(path, "wb") as f:
        f.write(body)
    print(f"\nSaved to {path}", file=sys.stderr)


def main():
    print(f"Saves to: {OUTPUT_DIR}", file=sys.stderr)
    print("Enter URL (or leave empty / type quit to exit).\n", file=sys.stderr)

    while True:
        try:
            url = input("URL: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.", file=sys.stderr)
            break
        if not url or url.lower() in ("quit", "exit", "q"):
            print("Bye.", file=sys.stderr)
            break
        fetch_one(url)
        print("", file=sys.stderr)


if __name__ == "__main__":
    main()
