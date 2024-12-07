# PDF Conversion and Processing Project

## Description

This project includes multiple Python scripts designed to perform common operations on PDF files and images. Each script is independent and focuses on a specific functionality such as converting images to PDF, extracting text from PDF files, or capturing automatic screenshots.

## Features

1. **Image to PDF Conversion** (from `image2pdf.py`):

   - Converts a set of images into a single PDF file.
   - Supported formats: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`, `.tiff`.

2. **PDF to Image Conversion** (from `pdf2image.py`):

   - Generates images for each page of a PDF file.
   - Allows specifying image resolution (DPI).

3. **Text Extraction from PDF** (from `pdf2text.py`):

   - Utilizes multiple methods to extract text (PyPDF2, pdfplumber, and OCR with pytesseract).

4. **Automatic Screenshot Capture** (from `slide_capture.py`):

   - Captures differences between successive screens and automatically saves significant screenshots.

## Prerequisites

- Python 3.7+
- Required Python modules:
  - `Pillow`
  - `PyPDF2`
  - `pdfplumber`
  - `pytesseract`
  - `PyMuPDF` (alias `fitz`)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure Tesseract OCR is installed (necessary for `pdf2text.py` in OCR mode):

   - [Instructions for installing Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## Usage Instructions

### 1. Image to PDF Conversion

- Script: `image2pdf.py`
- Steps:
  1. Place all images in a folder.
  2. Run the script:
     ```bash
     python image2pdf.py
     ```
  3. Follow the prompts to specify the folder path and output PDF file name.

### 2. PDF to Image Conversion

- Script: `pdf2image.py`
- Steps:
  1. Run the script:
     ```bash
     python pdf2image.py
     ```
  2. Provide the path to the PDF file and the output folder.

### 3. Text Extraction from PDF

- Script: `pdf2text.py`
- Steps:
  1. Run the script:
     ```bash
     python pdf2text.py
     ```
  2. Specify the path to the PDF file.
  3. If the text is successfully extracted, you can choose to save it to a text file.

### 4. Automatic Screenshot Capture

- Script: `slide_capture.py`
- Steps:
  1. Run the script:
     ```bash
     python slide_capture.py
     ```
  2. Screenshots will be automatically saved in the `screenshot_taken` folder.

## Key Notes

- For automatic screenshot capture, ensure permissions are enabled if running the script on macOS or Linux.
- The image difference threshold in `slide_capture.py` can be adjusted as needed.

## License

Please just dont steal my code...

