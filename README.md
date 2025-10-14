# 🎭 Gesture Meme Tracker

Real-time hand gesture detection with meme display using MediaPipe and OpenCV!

## 🚀 Features

- **Real-time hand gesture detection** using MediaPipe Hands
- **5 recognizable gestures**:
  - 👍 Thumbs up
  - ✌️ Peace sign
  - ✊ Fist
  - 🖐️ Open palm
  - 👌 OK sign
- **Dynamic meme display** - shows different meme for each gesture
- **Side-by-side view** - webcam feed and meme image displayed together
- **Beginner-friendly** - fully commented and easy to understand

## 📋 Requirements

- Python 3.7 or higher
- Webcam
- Required packages (see requirements.txt)

## 🔧 Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Add meme images:**
   - Create an `images` folder in the same directory as the script (it will be created automatically if it doesn't exist)
   - Add the following image files:
     - `thumbs_up.jpg` - for thumbs up gesture
     - `peace.jpg` - for peace sign
     - `fist.jpg` - for fist gesture
     - `open_palm.jpg` - for open palm
     - `ok_sign.jpg` - for OK sign
     - `default.jpg` - shown when no gesture detected

   **Note:** You can use `.jpg`, `.png`, or `.jpeg` formats (update filenames in code accordingly)

## 🎮 Usage

Run the script:
```bash
python gesture_meme_tracker.py
```

- **Show gestures** to the webcam to see corresponding memes
- **Press 'q'** to quit the application

## 🖐️ How Gestures Are Detected

The script uses MediaPipe's 21 hand landmarks to identify gestures:

- **Thumbs up**: Only thumb extended upward, all other fingers closed
- **Peace sign**: Index and middle fingers extended, others closed
- **Fist**: All fingers closed
- **Open palm**: All 4 fingers extended
- **OK sign**: Thumb and index finger tips touch, forming a circle

## 🎨 Customization

You can easily customize the script:

1. **Add more gestures**: Add logic to `detect_gesture()` function
2. **Change meme mappings**: Modify the `GESTURE_MEMES` dictionary
3. **Adjust detection sensitivity**: Change `min_detection_confidence` and `min_tracking_confidence` in the `main()` function

## 📝 Tips for Best Results

- Ensure good lighting
- Position your hand clearly in front of the camera
- Keep your hand at a reasonable distance (about 30-60cm from camera)
- Make gestures distinct and clear

## 🐛 Troubleshooting

**"No module named 'cv2'" or package import errors?**
- You likely have multiple Python installations
- Use the launcher script: `./run.sh`
- Or use the full Python path: `/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 gesture_meme_tracker.py`
- Check which Python: `which python` and `which pip`

**Webcam not opening?**
- **macOS**: Grant camera permission in System Settings → Privacy & Security → Camera
- Check if another application is using the webcam
- Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` in the code

**Gestures not being detected?**
- Ensure your full hand is visible in the frame
- Try adjusting lighting conditions
- Make gestures more distinct

**Missing meme images?**
- The script will create colored placeholder images if meme files are not found
- Add your own meme images to the `images` folder

## 📄 License

Free to use and modify for educational purposes!

---

**Gesture Meme Tracker** - Made with ❤️ using Python, OpenCV, and MediaPipe

