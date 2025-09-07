//Screenshot-to-Text (OCR) simple script.

Captures the full screen, runs OCR (via pytesseract/Tesseract),
prints the text, copies it to clipboard, and saves it to a .txt file.

Usage:
    python screenshot_to_text.py
"""
import os
import sys
import time
from datetime import datetime
import tempfile

try:
    from mss import mss
except ImportError:
    print("Missing dependency: mss. Install with: pip install mss")
    sys.exit(1)

from PIL import Image
import pytesseract
import pyperclip

# If Tesseract is not in PATH on Windows, set its full path here, for example:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_fullscreen() -> Image.Image:
    """Capture the entire primary monitor and return a PIL.Image."""
    with mss() as sct:
        monitor = sct.monitors[1]  # 0 is all monitors combined; 1 is primary in mss
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
        return img

def run_ocr(image: Image.Image, lang: str = "eng") -> str:
    """Run Tesseract OCR on a PIL image and return recognized text."""
    try:
        text = pytesseract.image_to_string(image, lang=lang)
    except pytesseract.TesseractNotFoundError as e:
        raise RuntimeError(
            "Tesseract not found. Make sure tesseract is installed and available in PATH.\n"
            "On Windows: install from https://github.com/tesseract-ocr/tesseract/releases\n"
            "On macOS: brew install tesseract\n"
            "On Debian/Ubuntu: sudo apt install tesseract-ocr"
        ) from e
    return text

def save_image_and_text(image: Image.Image, text: str, out_dir: str = "."):
    """Save the screenshot image and the extracted text to files with timestamped names."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    img_path = os.path.join(out_dir, f"screenshot_{ts}.png")
    txt_path = os.path.join(out_dir, f"screenshot_{ts}.txt")

    image.save(img_path)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)

    return img_path, txt_path

def main():
    print("Screenshot-to-Text (OCR)\nPress Enter to capture the full screen...")
    input()
    print("Capturing screen...")
    img = capture_fullscreen()

    # Optionally show the captured image (uncomment if you want a preview)
    # img.show()

    print("Running OCR... (this may take a second)")
    try:
        text = run_ocr(img, lang="eng")
    except RuntimeError as err:
        print("Error:", err)
        sys.exit(1)

    if not text.strip():
        print("No text detected.")
    else:
        print("\n=== Extracted Text ===\n")
        print(text)
        # copy to clipboard
        try:
            pyperclip.copy(text)
            print("\n✔ Copied extracted text to clipboard.")
        except Exception as e:
            print(f"⚠ Could not copy to clipboard: {e}")

    # save image + text to temp folder (or current directory)
    out_dir = os.path.join(os.getcwd(), "ocr_outputs")
    os.makedirs(out_dir, exist_ok=True)
    img_path, txt_path = save_image_and_text(img, text, out_dir=out_dir)
    print(f"\nSaved screenshot to: {img_path}")
    print(f"Saved extracted text to: {txt_path}")

    print("\nDone.")

if __name__ == "__main__":
    main()
