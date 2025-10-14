# 🚀 Quick Start Guide - Gesture Meme Tracker

## Step-by-Step Setup

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Check Installation (Optional but Recommended)
```bash
python check_dependencies.py
```
This will verify that all packages are installed and your webcam is accessible.

### 3️⃣ Add Meme Images
Add these 6 image files to the `images/` folder:
- `thumbs_up.jpg`
- `peace.jpg`
- `fist.jpg`
- `open_palm.jpg`
- `ok_sign.jpg`
- `default.jpg`

**Don't have memes?** No worries! The app will create colorful placeholder images automatically.

### 4️⃣ Run the Application

**Option 1: Use the launcher script (Recommended for macOS)**
```bash
./run.sh
```

**Option 2: Run directly with Python**
```bash
python gesture_meme_tracker.py
```

**Note for macOS users:** If you get "module not found" errors, you may have multiple Python installations. Use the full path:
```bash
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 gesture_meme_tracker.py
```

### 5️⃣ Make Gestures!
Show these gestures to your webcam:
- 👍 **Thumbs up** - Close all fingers, extend thumb upward
- ✌️ **Peace sign** - Extend index and middle fingers, close others
- ✊ **Fist** - Close all fingers tightly
- 🖐️ **Open palm** - Extend all fingers
- 👌 **OK sign** - Touch thumb tip to index tip, extend other fingers

### 6️⃣ Grant Camera Permission (macOS)
When you first run the app, macOS will ask for camera permission. Click **Allow**.

If you denied it accidentally:
- Go to **System Settings → Privacy & Security → Camera**
- Enable access for Terminal or Python

### 7️⃣ Quit
Press **'q'** on your keyboard to exit.

---

## 📁 Project Structure
```
monkey/
├── gesture_meme_tracker.py  ← Main application
├── run.sh                   ← Launcher script (macOS)
├── check_dependencies.py     ← Dependency checker
├── requirements.txt          ← Package dependencies
├── README.md                 ← Full documentation
├── QUICK_START.md           ← This file
└── images/                   ← Meme images folder
    ├── README.txt
    ├── thumbs_up.jpg
    ├── peace.jpg
    ├── fist.jpg
    ├── open_palm.jpg
    ├── ok_sign.jpg
    └── default.jpg
```

---

## 🎯 Usage Tips

**For best gesture detection:**
- Keep your hand 30-60cm from the camera
- Ensure good lighting
- Make clear, distinct gestures
- Show your full hand to the camera

**Having issues?**
- **Module not found?** Use `./run.sh` instead of `python gesture_meme_tracker.py`
- **Webcam denied?** Grant camera permission in System Settings (macOS)
- Read the troubleshooting section in README.md
- Run `check_dependencies.py` to verify setup
- Check that your webcam is not being used by another app

---

## 🎨 Customization Ideas

Want to make it your own?

1. **Add more gestures** - Edit the `detect_gesture()` function
2. **Use different images** - Replace files in `images/` folder  
3. **Change sensitivity** - Adjust confidence thresholds in code
4. **Add sound effects** - Import `pygame` and play sounds per gesture
5. **Record gestures** - Add functionality to save gesture videos

---

## 💡 How It Works

The app uses:
- **OpenCV** - Captures webcam video and displays output
- **MediaPipe Hands** - Detects 21 hand landmarks in real-time
- **Gesture Logic** - Analyzes landmark positions to classify gestures

The `detect_gesture()` function checks:
- Which fingers are extended
- Finger tip positions relative to joints
- Distance between specific landmarks (for OK sign)

---

**Ready to start?** Run `python gesture_meme_tracker.py` and have fun! 🎉

