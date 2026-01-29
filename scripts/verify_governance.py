#!/usr/bin/env python3
import os
import sys
import glob

def check_exists(path):
    if not os.path.exists(path):
        print(f"ERROR: Missing required artifact: {path}")
        return False
    return True

def check_not_exists(path_pattern):
    found = glob.glob(path_pattern)
    if found:
        print(f"ERROR: Forbidden artifacts found matching: {path_pattern}")
        for f in found:
            print(f"  - {f}")
        return False
    return True

def check_decision_content(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    missing = []
    if "## Rationale" not in content:
        missing.append("Rationale")
    if "## Impact" not in content:
        missing.append("Impact")

    if missing:
        print(f"ERROR: {filepath} is missing sections: {', '.join(missing)}")
        return False
    return True

def main():
    success = True

    # Check required files
    if not check_exists("DECISIONS/"): success = False
    if not check_exists("CHANGELOG.md"): success = False
    if not check_exists("GLOSSARY.md"): success = False

    # Check forbidden files
    if not check_not_exists("docs/decisions/*"): success = False
    if not check_not_exists("docs/audits/*"): success = False

    # Check DECISION content
    decisions = glob.glob("DECISIONS/DECISION-*.md")
    for d in decisions:
        if not check_decision_content(d):
            success = False

    if not success:
        sys.exit(1)

    print("Governance verification passed.")

if __name__ == "__main__":
    main()
