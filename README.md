# Failed Login Analyzer

## Overview
A beginner Python cybersecurity project that analyzes sample authentication logs, counts failed login attempts per user, and generates alerts when a user reaches a defined threshold.

## Features
- Reads authentication logs line by line.
- Identifies failed login events in the expected log format.
- Counts failed login attempts for each user.
- Generates an alert when a user has 3 or more failed attempts.
- Saves results to `report.txt`.
- Skips lines that do not match the expected two-field format.

## Technologies
- Python 3
- File handling
- String parsing
- Dictionaries
- Loops and conditional statements

## Project Files
- `failed_login_analyzer.py` — analysis script.
- `login_logs.txt` — sample authentication logs.
- `report.txt` — generated analysis report.

## How to Run
1. Install Python 3.
2. Place the three project files in the same directory.
3. Open a terminal in the project directory.
4. Run:

   `python failed_login_analyzer.py`

## Detection Rule
The script generates an alert when a user's failed login count is greater than or equal to 3.

## Sample Output
```text
admin : 3 failed logins
ALERT: Suspicious login activity for admin
ahmed : 1 failed logins
```

## Limitations
- This is an educational prototype, not a production security monitoring system.
- It expects logs in the format `user=USERNAME status=STATUS`.
- Invalid lines are skipped but are not recorded in a separate error log.
- The detection rule uses a simple count threshold and does not consider timestamps, source IP addresses, or other contextual signals.

## Testing
Tested with sample authentication logs containing successful and failed login events. A malformed line containing only `status=failed` was tested and correctly excluded from the user counts.

## Future Improvements
- Record malformed lines for investigation.
- Add timestamp and source IP analysis.
- Add automated tests and performance benchmarks.
- Integrate with a SIEM in a future project.