# 🧹 Python File Cleaner

A simple Python utility that automatically removes unwanted files from a specified directory based on their file extensions.

## Features

- Deletes files with selected extensions
- Supports multiple file types
- Easy to customize
- Lightweight and fast
- Built with Python

## Technologies

- Python 3
- os
- time

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/python-file-cleaner.git
```

Navigate to the project:

```bash
cd python-file-cleaner
```

## Usage

Edit the folder path inside the script:

```python
PATH = r"C:\Users\YourName\Desktop"
```

Run the script:

```bash
python clean_up.py
```

## Example

Before:

```
Desktop/
├── notes.txt
├── report.docx
├── image.bmp
├── project/
└── chrome.lnk
```

After:

```
Desktop/
├── project/
└── chrome.lnk
```

## Project Structure

```
clean_up/
│
├── clean_up.py
├── README.md
└── LICENSE
```

## Future Improvements

- [ ] GUI version
- [ ] Delete files older than X days
- [ ] Clean Windows Temp folder
- [ ] Dry-run mode
- [ ] Logging
- [ ] Configuration file
- [ ] Command-line arguments

## License

MIT License
