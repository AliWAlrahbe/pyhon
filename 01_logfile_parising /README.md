# Log Parser CLI Tool

This script parses a log file and counts log levels (`INFO`, `WARNING`, `ALERT`).
Optionally, it can also print the line numbers where each log level appears.

It is designed as a simple command-line tool and works well with large log files.

---

## Requirements

* Python 3.8 or newer
* No external dependencies (uses only standard library)

---

## Usage

Basic usage:

```bash
python log_parser.py --file LOG_FILE
```

Example:

```bash
python log_parser.py --file app.log
```

This will print how many times each log level appears.

---

## Show Line Numbers (Optional)

To also print the line numbers where each log level occurs, use:

```bash
python log_parser.py --file app.log --show-lines
```

---

## Example Output

Without `--show-lines`:

```
INFO: 12
WARNING: 3
ALERT: 1
```

With `--show-lines`:

```
INFO: 12
WARNING: 3
ALERT: 1
############ LINES ############
INFO lines: [1, 4, 7, 10, ...]
WARNING lines: [15, 42, 88]
ALERT lines: [101]
```

---

## Log Level Detection

The script uses regular expressions to detect log levels accurately.
It matches only full words, so it will **not** count misleading cases such as:

* `INFORMATION`
* `USER_INFO`

Only exact log levels are counted.

---

## Exit Codes

* `0` → Successful execution
* `1` → Error (file not found, permission issue, etc.)

This makes the script suitable for use in shell scripts, cron jobs, or CI/CD pipelines.

---

## Notes

* The file is read line by line (memory-efficient).
* Line number tracking is optional to avoid unnecessary memory usage.
* Designed as a small, clear CLI utility.

---
