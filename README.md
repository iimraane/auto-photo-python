# Slide Change Screenshot Capture - README

## Description

This Python project is designed to take a screenshot each time a change is detected on your computer screen. This can be particularly useful for extracting slides from a long video lecture, where slides change occasionally. The script ensures that you automatically get a screenshot whenever there is a significant change, perfect for capturing medical or other educational content presented in video form.

## Features
- Automatic detection of screen changes.
- Takes a screenshot whenever a change is detected.
- Saves screenshots with filenames based on a sequence number for easy organization.

## Dependencies
To use this project, you need to install the following libraries:
- `Pillow`

To install the dependencies, run the following command:
```sh
pip install Pillow
```

## Usage
1. Clone this project or copy the source code to your machine.
2. Ensure the dependencies are installed.
3. Simply run the Python script:
```sh
python slide_capture.py
```

The script will continuously monitor your screen for changes and take a screenshot whenever a change is detected. All screenshots will be saved in a folder named `screenshot_taken`.

## Technical Details
- The script captures the entire screen using `Pillow`.
- It compares the current screenshot with the previous one using pixel-level difference detection to determine any changes.
- If a significant change is detected (based on a defined threshold), a screenshot is saved in the `screenshot_taken` folder.
- Filenames are generated based on a sequence number (e.g., `capture_0001.png`) to ensure each screenshot is unique.

## Notes
- Make sure that your screen resolution remains constant while the script is running for accurate change detection.
- Screenshots will be saved in the `screenshot_taken` folder located in the same directory as the script.
- You can adjust the sensitivity of change detection by modifying the threshold value in the script.

## Supported Platforms
This project is compatible with Windows, Linux, and macOS.

## Author
This project was created to help efficiently capture content from long video lectures. Feel free to modify it to suit your needs!

## License
Just don't steal my code please...