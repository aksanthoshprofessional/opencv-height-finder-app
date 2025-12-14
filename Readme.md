# Height Finder

## Introduction

**Height Finder** is a Python-based tool that allows users to determine the height of an object in an image using mathematical calculations. By leveraging Tkinter for its GUI and OpenCV for image processing, this application provides an intuitive interface for selecting an image, marking reference points, and calculating the height based on user input.

## Features

- **Intuitive GUI** for easy interaction using `Tkinter`.
- **Image Selection** via a file dialog.
- **Interactive Mouse Input** to mark reference points on an image.
- **Height Calculation** based on angle measurements and user-specified distance.
- **Popup Alerts** for user guidance and result display.

## Dependencies

Ensure the following Python libraries are installed:

- `tkinter` (built-in with Python)
- `cv2` (OpenCV)
- `math`

You can install missing dependencies with:

```bash
pip install opencv-python
```

## Usage
- Run the script using:

```bash
python HeightFinder.py
```
- Select an image using the Open Image button.

- Click to mark reference points to measure the object's angle.

- Enter the object's distance in the prompt when asked.

- The calculated height will be displayed in a message box.

## How It Works
- The tool uses angle calculation and trigonometry to determine the height.

- The user selects three points: two defining the base and one at the object's peak.

- The slope is calculated, and the angle is determined.

- The final height is computed using the distance and tangent function.

## Author
- Developed by Santhosh.A

## Notes
- Ensure images are clear and the object has distinguishable reference points.

- The accuracy of height calculation depends on correct distance input from the user.

- Use responsibly for image analysis and measurement tasks.
