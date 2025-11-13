# 🎭 Gesture Meme Tracker

Real-time hand gesture detection with meme display using MediaPipe!

## 🌐 Two Versions Available

### 🖥️ **Desktop Version** (Python + OpenCV)
Run locally on your computer with a native window

### 🌍 **Web Version** (JavaScript) ⭐ NEW!
Works in any browser, deploy to the internet, accessible anywhere!

## 🚀 Features

- **Real-time hand gesture detection** using MediaPipe Hands & Face Mesh
- **5 recognizable gestures**:
  - 😂 **JIJIJA** - Just laugh (open mouth)
  - 🤐 **MIMIMI** - Both hands closed (fists)
  - ⚖️ **SIXSEVEN** - Balance pose (hands extended wide)
  - 🤫 **CERRAO** - One finger up (index finger)
  - 👌 **DEFAULT** - Neutral state
- **Dynamic meme display** - shows different meme videos/images for each gesture
- **Side-by-side view** - webcam feed and meme displayed together
- **Beginner-friendly** - fully commented and easy to understand

---

# 🌍 Web Version (Recommended)

## 🎯 Live Demo
Once deployed, your app will be accessible from any device with a browser!

## ⚡ Quick Deploy

### Deploy to Vercel (Easiest!)

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add web version"
   git push origin main
   ```

2. **Deploy to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Sign in with GitHub
   - Click "New Project"
   - Import your `gesture-meme-tracker-1` repository
   - Click "Deploy" (that's it!)
   - Your site will be live at `https://your-project.vercel.app`

### Deploy to GitHub Pages

1. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main`, folder: `/ (root)`
   - Save

2. **Access your site:**
   - Your site will be live at `https://yourusername.github.io/gesture-meme-tracker-1`

## 💻 Local Testing (Web Version)

You can test the web version locally:

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

Then open `http://localhost:8000` in your browser.

## 📋 Web Version Requirements

- Modern web browser (Chrome, Firefox, Safari, Edge)
- Webcam
- HTTPS connection (required for camera access - automatically handled by Vercel/GitHub Pages)

---

# 🖥️ Desktop Version (Python)

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
      - (these will change) 
   - Create an `images` folder in the same directory as the script (it will be created automatically if it doesn't exist)
   - Add the following image files:
     - `JIJIJA.mp4` - Laughing royale
     - `CERRAO.mp4` - Crazy jawline
     - `MIMIMI.mp4` - Goblin crying
     - `SIXSEVEN.mp4` - 6 7 
     - `default.jpg` - shown when no gesture detected

   **Note:** You can use `.jpg`, `.png`, or `.jpeg` formats (update filenames in code accordingly)

## 🎮 Usage (Desktop Version)

Run the script:
```bash
python gesture_meme_tracker.py
```

- **Show gestures** to the webcam to see corresponding memes
- **Press 'q'** to quit the application

---

## 🖐️ How Gestures Are Detected

Both versions use MediaPipe's hand landmarks (21 points per hand) and face mesh to identify gestures:

- 😂 **JIJIJA** - Detects open mouth (laughing expression)
- 🤐 **MIMIMI** - Both hands with all fingers closed (fists)
- ⚖️ **SIXSEVEN** - Both hands with open palms spread apart horizontally
- 🤫 **CERRAO** - One hand with only the index finger extended
- 👌 **DEFAULT** - Any other hand position or no hands detected

## 🎨 Customization

### Web Version
Edit these files:
- `script.js` - Add gesture logic in `detectGesture()` function
- `GESTURE_MEMES` object - Change meme file mappings
- `style.css` - Customize appearance

### Desktop Version (Python)
1. **Add more gestures**: Edit `detect_gesture()` function in `gesture_meme_tracker.py`
2. **Change meme mappings**: Modify the `GESTURE_MEMES` dictionary
3. **Adjust detection sensitivity**: Change `min_detection_confidence` and `min_tracking_confidence`

## 📝 Tips for Best Results

- Ensure good lighting
- Position your hand clearly in front of the camera
- Keep your hand at a reasonable distance (about 30-60cm from camera)
- Make gestures distinct and clear

## 🐛 Troubleshooting

### Web Version

**Camera not working?**
- Allow camera permissions when prompted by the browser
- Make sure you're using HTTPS (Vercel/GitHub Pages automatically provide this)
- Check if another tab/app is using the webcam
- Try a different browser (Chrome works best)

**Site not loading meme videos?**
- Make sure the `images` folder is committed to your Git repository
- Check browser console (F12) for errors
- Videos must be in `.mp4` or `.webm` format

**Gestures not being detected?**
- Ensure good lighting
- Keep your hand(s) clearly visible and at a reasonable distance
- Make gestures distinct and deliberate
- Check if face is visible for JIJIJA gesture (laughing)

**Deployment issues?**
- Ensure all files (HTML, CSS, JS, images folder) are pushed to GitHub
- For Vercel: Check build logs for errors
- For GitHub Pages: Make sure Pages is enabled in repository settings

### Desktop Version (Python)

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

## 📁 Project Structure

```
gesture-meme-tracker-1/
├── index.html              # Web app main page
├── style.css               # Web app styling
├── script.js               # Web app JavaScript (MediaPipe Web)
├── vercel.json             # Vercel deployment config
├── gesture_meme_tracker.py # Desktop Python version
├── requirements.txt        # Python dependencies
├── run.sh                  # Python launcher script
├── images/                 # Meme videos and images
│   ├── JIJIJA.mp4
│   ├── MIMIMI.mp4
│   ├── SIXSEVEN.mp4
│   ├── CERRAO.mp4
│   └── ok_sign.jpg
└── README.md
```

## 🌟 Deployment Checklist

- [ ] All meme files are in the `images/` folder
- [ ] Files committed to Git: `git add . && git commit -m "Ready to deploy"`
- [ ] Pushed to GitHub: `git push origin main`
- [ ] Deployed to Vercel or GitHub Pages
- [ ] Tested on different devices (desktop, mobile, tablet)
- [ ] Camera permissions working correctly

## 📄 License

Free to use and modify for educational purposes!

---

**Gesture Meme Tracker** - Made with ❤️ using MediaPipe, JavaScript, Python, and OpenCV

🌐 **Web Version:** Runs entirely in your browser  
🖥️ **Desktop Version:** Native Python application

