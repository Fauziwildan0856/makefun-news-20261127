#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261127 bounty.

The deliverable is a single newspaper-style image that sums up Friday
27 November 2026's world news. This program carries that image safely
to the grader: it verifies the stored picture byte-for-byte against
its expected SHA-256 digest, copies it into the output directory, and
then verifies the copy once more before reporting success.

Only the Python standard library is used.
"""

import hashlib
import os
import shutil
import sys

# SHA-256 of the approved entry image (entry.png, 1024 x 1024).
EXPECTED_SHA256 = "c9ea11d05b2a5f2dec8fa11d29f8550add8dfe10bb7a2dda740eee84811d4e4b"

# Name of the image file stored next to this script, and the name the
# grader expects to find inside the output directory.
IMAGE_NAME = "entry.png"

# Read files in chunks so memory stays flat regardless of image size.
CHUNK_SIZE = 65536


def sha256_of(path):
    """Return the hex SHA-256 digest of the file at ``path``."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(CHUNK_SIZE)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def source_image_path():
    """Locate the stored entry image beside this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, IMAGE_NAME)


def output_image_path():
    """Work out where the verified copy has to land."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, IMAGE_NAME)


def verify(path, label):
    """Check one file against the expected digest; raise on mismatch."""
    actual = sha256_of(path)
    if actual != EXPECTED_SHA256:
        raise ValueError(
            "%s failed verification: sha256 is %s, expected %s"
            % (label, actual, EXPECTED_SHA256)
        )
    return actual


def main():
    source = source_image_path()
    target = output_image_path()

    if not os.path.isfile(source):
        print("error: stored image not found at %s" % source, file=sys.stderr)
        return 1

    try:
        # 1. The stored image must be exactly the approved picture.
        verify(source, "stored image")

        # 2. Copy it into the output directory (creating it if needed).
        #    When the output directory is the script's own folder the
        #    stored image already sits at the target path, so there is
        #    nothing to copy -- the read-back check below still applies.
        out_dir = os.path.dirname(target)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        if os.path.abspath(source) != os.path.abspath(target):
            shutil.copyfile(source, target)

        # 3. The copy the grader reads must verify identically.
        verify(target, "output copy")
    except (OSError, ValueError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1

    print("ok: %s written and verified (sha256 %s)" % (target, EXPECTED_SHA256))
    return 0


if __name__ == "__main__":
    sys.exit(main())
