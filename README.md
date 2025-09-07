Screenshot-to-Text (OCR)

A simple Python script to capture your screen, extract text using OCR (Tesseract via pytesseract), print the recognized text, copy it to your clipboard, and save both the screenshot and extracted text to files.

## Features

- Captures the entire primary monitor.
- Runs OCR using Tesseract (via pytesseract).
- Prints extracted text to the console.
- Copies extracted text to your clipboard.
- Saves the screenshot and extracted text to timestamped files.

## Requirements

- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Python packages:
  - `mss`
  - `pillow`
  - `pytesseract`
  - `pyperclip`

## Installation

1. **Install Tesseract:**
   - **Windows:** [Download installer](https://github.com/tesseract-ocr/tesseract/releases)
   - **macOS:** `brew install tesseract`
   - **Linux (Debian/Ubuntu):** `sudo apt install tesseract-ocr`

2. **Install Python dependencies:**
   ```sh
   pip install mss pillow pytesseract pyperclip
   ```

3. *(Optional, Windows only)* If Tesseract is not in your PATH, set its path in index.py:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

## Usage

Run the script:

```sh
python index.py
```

- Press Enter to capture the full screen.
- The script will display the extracted text, copy it to your clipboard, and save both the screenshot and text in the `ocr_outputs` folder.

## Output

- `ocr_outputs/screenshot_YYYYMMDD_HHMMSS.png` — the captured screenshot.
- `ocr_outputs/screenshot_YYYYMMDD_HHMMSS.txt` — the extracted text.

## Troubleshooting

- **Missing dependencies:** Install them with `pip install ...` as shown above.
- **Tesseract not found:** Ensure Tesseract is installed and available in your system PATH, or set its path in the script.
- **No text detected:** The OCR may not recognize text if the screenshot is blank or low quality.

## License

MIT License

---

See index.py for the full source code..
