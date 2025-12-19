#!/usr/bin/env python3
#By Ali Alrahbe
import argparse
import re
import sys

#using Regex to avoid mis lead line like INFORMATION or USER_INFO
LEVEL_RE = re.compile(r"\b(INFO|WARNING|ALERT)\b")

def read_cli_arguments():
    p = argparse.ArgumentParser(
        description="Parse log file and count log levels (INFO / WARNING / ALERT)"
    )
    p.add_argument("--file", required=True, metavar="LOG_FILE", help="Path to the log file to parse")
    p.add_argument("--show-lines", action="store_true", help="Print line numbers for each level")
    return p.parse_args()

def main():
    args = read_cli_arguments()
    log_file = args.file

    counts = {"INFO": 0, "WARNING": 0, "ALERT": 0}
    lines  = {"INFO": [], "WARNING": [], "ALERT": []}

    try:
        with open(log_file, "r", encoding="utf-8", errors="replace") as f:
            for line_number, line in enumerate(f, start=1):
                match = LEVEL_RE.search(line)
                if not match:
                    continue
                level = match.group(1) # group(1) returns the captured log level (INFO/WARNING/ALERT)
                counts[level] += 1
                if args.show_lines:
                    lines[level].append(line_number)

    except FileNotFoundError:
        print(f"Error: file not found -> {log_file}", file=sys.stderr)
        return 1
    except PermissionError:
        print(f"Error: permission denied -> {log_file}", file=sys.stderr)
        return 1
    except IsADirectoryError:
        print(f"Error: expected a file but got a directory -> {log_file}", file=sys.stderr)
        return 1

    for level in ("INFO", "WARNING", "ALERT"):
        print(f"{level}: {counts[level]}")

    if args.show_lines:
        print("############ LINES ############")
        for level in ("INFO", "WARNING", "ALERT"):
            print(f"{level} lines: {lines[level]}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
