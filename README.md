# Virtual Drawing Application

A real-time virtual drawing application that uses computer vision and hand tracking to create an interactive drawing experience. Users can draw on their screen using hand gestures captured through their webcam.

## Features

### Drawing Capabilities
- Real-time hand gesture recognition
- Multiple color selection (Pink, Blue, Green)
- Eraser tool
- Adjustable brush and eraser thickness
- Canvas overlay with transparency
- Dual display mode (Canvas and Combined view)

### Hand Gestures
- Drawing Mode: Index finger up
- Selection Mode: Index and Middle fingers up
- Color Selection: Use Selection Mode in the header area
- Eraser: Select black color for erasing

### Technical Features
- Real-time webcam feed processing
- Hand landmark detection using MediaPipe
- Canvas overlay with alpha blending
- Robust error handling and logging
- Clean exit functionality

## Requirements

- Python 3.7+
- OpenCV (`cv2`)
- NumPy
- MediaPipe
- Logging

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Kunal-2301/Air-Canvas.git
cd Air-Canvas
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the application:
```bash
python app.py
```

2. Controls:
   - Raise only index finger to draw
   - Raise both index and middle fingers to select colors
   - Move to the header area to change colors
   - Press 'q' to quit

## Project Structure

- `app.py`: Main application file with drawing logic
- `track.py`: Hand tracking module implementation
- `Header/`: Directory containing color selection images
- Four color options:
  - Pink (Default): 250-450px
  - Blue: 550-750px
  - Green: 800-950px
  - Black (Eraser): 1050-1200px

## Technical Details

- Canvas Resolution: 1280x720 pixels
- Header Height: 125 pixels
- Brush Thickness: 25px
- Eraser Thickness: 100px
- Hand Detection Confidence: 0.85

## Error Handling

- Camera initialization verification
- Frame capture validation
- Image loading error handling
- Landmark detection error management
- Resource cleanup on exit


