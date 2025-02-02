#!/usr/bin/env python3

"""
This script creates bookmarks for all snapshots matching some pattern.
"""

import libzfs
import re

from contextlib import suppress

SNAPSHOT_PATTERN = re.compile(r"your_pattern_here")

def bookmark_all() -> int:
    """Create bookmarks for all snapshots matching some pattern."""
    bookmarks_created = 0
    for snapshot in libzfs.ZFS().snapshots:
        if SNAPSHOT_PATTERN.search(f"{snapshot.parent.name}@{snapshot.snapshot_name}"):
            with suppress(FileExistsError):  # Skip if bookmark already exists
                snapshot.bookmark(snapshot.snapshot_name)
                bookmarks_created += 1
    return bookmarks_created

if __name__ == "__main__":
    print(f"Created {bookmark_all()} bookmark(s)")
