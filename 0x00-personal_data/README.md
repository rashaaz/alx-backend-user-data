# 0x00-personal_data

## Project Overview
**Start Date:** Jul 3, 2024 6:00 AM  
**End Date:** Jul 5, 2024 6:00 AM  
**Checker Release:** Jul 3, 2024 6:00 PM  
**Manual QA Review:** Request upon project completion  
**Auto Review:** Launches at the deadline  

## Resources
- [What Is PII, non-PII, and Personal Data?](#)
- [Logging Documentation](#)
- [bcrypt Package](#)
- [Logging to Files, Setting Levels, and Formatting](#)

## Learning Objectives
By the end of this project, you should be able to explain:
- Examples of Personally Identifiable Information (PII)
- How to implement a log filter to obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

## Requirements
- Files interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- Files must end with a new line
- First line of all files: `#!/usr/bin/env python3`
- `README.md` file at the root of the project folder
- Code should follow `pycodestyle` (version 2.5)
- All files must be executable
- File lengths tested using `wc`
- Modules, classes, and functions must have proper documentation
- Functions should be type annotated

## Tasks

### 0. Regex-ing
Write a function `filter_datum` to obfuscate specific fields in a log message using regex.

**Arguments:**
- `fields` (list of strings): Fields to obfuscate
- `redaction` (string): Replacement string for obfuscation
- `message` (string): Log line
- `separator` (string): Field separator in the log line

**Example:**
```python
filter_datum(fields, 'xxx', message, ';')

