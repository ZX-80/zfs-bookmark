#!/usr/bin/env python3

"""
This script creates bookmarks for all snapshots matching some pattern.
"""

import argparse
import libzfs
import re

from contextlib import suppress


def bookmark_all(snapshot_pattern: re.Pattern) -> int:
    """Create bookmarks for all snapshots matching some pattern."""
    bookmarks_created = 0
    for snapshot in libzfs.ZFS().snapshots:
        if snapshot_pattern.search(f"{snapshot.parent.name}@{snapshot.snapshot_name}"):
            with suppress(FileExistsError):  # Skip if bookmark already exists
                snapshot.bookmark(snapshot.snapshot_name)
                bookmarks_created += 1
    return bookmarks_created


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=bookmark_all.__doc__)
    parser.add_argument(
        "snapshot_pattern",
        type=re.compile,
        help='The regex pattern to compare with snapshots of the form "parent@name"',
    )
    print(f"Created {bookmark_all(parser.parse_args().snapshot_pattern)} bookmark(s)")

