# Gesture Guide - Clash Royale Edition 1

## 🎥 Custom Video Reactions (MP4)

1. **😂 JIJIJA** (`JIJIJA.mp4`)
   - **How to trigger:** Just laugh! Open your mouth wide
   - **When:** Laughing emotionally
   - **Detection:** Mouth opening detected (no hands required)

2. **🤐 MIMIMI** (`MIMIMI.mp4`)
   - **How to trigger:** Close both hands into fists (anywhere in frame)
   - **When:** Complaining/whining gesture
   - **Detection:** Both hands with no fingers extended (closed fists)

3. **⚖️ SIXSEVEN** (`SIXSEVEN.mp4`)
   - **How to trigger:** Extend both hands out to your sides like balancing
   - **When:** Balancing or "what can I do?" gesture
   - **Detection:** Two hands with open palms extended far apart

4. **🤫 CERRAO** (`CERRAO.mp4`)
   - **How to trigger:** Make a fist but keep one finger (index) up
   - **When:** Thinking or "shush" gesture
   - **Detection:** One hand with only index finger extended

## 👌 Neutral/Default
- **OK Sign Image** (`ok_sign.jpg`) - Shown when no gesture detected or neutral position

## Tips for Best Detection

- Make sure your hands are well-lit and clearly visible to the camera
- For two-hand gestures (MIMIMI, SIXSEVEN), keep both hands in frame
- Position yourself so your face area is visible for face-relative gestures
- Videos will loop automatically when active

## Customizing Gestures

If you want to adjust sensitivity or detection logic, edit the `detect_gesture()` function in `gesture_meme_tracker.py`.

Key detection parameters:
- **Hand height:** `wrist.y < 0.4` means hand is near face
- **Hand separation:** `x_distance > 0.3` means hands are far apart
- **Finger count:** `num_extended >= 3` means multiple fingers up

