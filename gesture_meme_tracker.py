"""
Gesture Meme Tracker - Real-time Hand Gesture Detection with Meme Display
Uses MediaPipe Hands to detect gestures and displays corresponding meme images
"""

import cv2
import mediapipe as mp
import numpy as np
import os

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Dictionary mapping gestures to meme image filenames
GESTURE_MEMES = {
    "thumbs_up": "thumbs_up.jpg",
    "peace": "peace.jpg",
    "fist": "fist.jpg",
    "open_palm": "open_palm.jpg",
    "ok_sign": "ok_sign.jpg",
    "none": "default.jpg"  # Default image when no gesture detected
}


def detect_gesture(hand_landmarks):
    """
    Detects hand gesture based on landmark positions.
    
    Args:
        hand_landmarks: MediaPipe hand landmarks object containing 21 points
        
    Returns:
        String representing the detected gesture name
        
    Landmark indices (key points):
    - 0: Wrist
    - 4: Thumb tip
    - 8: Index finger tip
    - 12: Middle finger tip
    - 16: Ring finger tip
    - 20: Pinky tip
    - 3, 7, 11, 15, 19: Finger DIPs (second from tip)
    - 2, 6, 10, 14, 18: Finger PIPs (middle joints)
    """
    
    # Extract landmark coordinates
    landmarks = hand_landmarks.landmark
    
    # Helper function to check if finger is extended
    def is_finger_extended(tip_idx, pip_idx, mcp_idx):
        """Check if a finger is extended by comparing y-coordinates"""
        # In image coordinates, y increases downward, so tip.y < pip.y means extended
        return landmarks[tip_idx].y < landmarks[pip_idx].y and landmarks[pip_idx].y < landmarks[mcp_idx].y
    
    # Helper function to check if thumb is extended (uses x-coordinate)
    def is_thumb_extended():
        """Check if thumb is extended by comparing x-coordinates"""
        # Thumb extends horizontally, so we use x-coordinates
        # For right hand: thumb extends left (smaller x)
        # For left hand: thumb extends right (larger x)
        wrist_x = landmarks[0].x
        thumb_tip_x = landmarks[4].x
        thumb_ip_x = landmarks[3].x
        thumb_mcp_x = landmarks[2].x
        
        # Check if thumb is extended away from palm
        thumb_extended = abs(thumb_tip_x - wrist_x) > abs(thumb_mcp_x - wrist_x)
        return thumb_extended and landmarks[4].y < landmarks[3].y
    
    # Count extended fingers (excluding thumb)
    extended_fingers = []
    
    # Index finger (8: tip, 6: PIP, 5: MCP)
    if is_finger_extended(8, 6, 5):
        extended_fingers.append("index")
    
    # Middle finger (12: tip, 10: PIP, 9: MCP)
    if is_finger_extended(12, 10, 9):
        extended_fingers.append("middle")
    
    # Ring finger (16: tip, 14: PIP, 13: MCP)
    if is_finger_extended(16, 14, 13):
        extended_fingers.append("ring")
    
    if is_finger_extended(20, 18, 17):
        extended_fingers.append("pinky")
    
    thumb_extended = is_thumb_extended()
    
    num_extended = len(extended_fingers)
    
    if thumb_extended and num_extended == 0:
        return "thumbs_up"
    
    if not thumb_extended and num_extended == 2 and "index" in extended_fingers and "middle" in extended_fingers:
        return "peace"
    
    if num_extended >= 4:
        return "open_palm"
    
    if not thumb_extended and num_extended == 0:
        return "fist"
    
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    
    distance = np.sqrt((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)
    
    if distance < 0.05 and num_extended >= 2:
        return "ok_sign"
    
    return "none"


def load_meme_images(images_folder):
    """
    Load all meme images from the specified folder.
    
    Args:
        images_folder: Path to folder containing meme images
        
    Returns:
        Dictionary mapping gesture names to loaded images
    """
    meme_images = {}
    
    for gesture, filename in GESTURE_MEMES.items():
        image_path = os.path.join(images_folder, filename)
        
        # Try to load image, create placeholder if not found
        if os.path.exists(image_path):
            img = cv2.imread(image_path)
            if img is not None:
                meme_images[gesture] = img
            else:
                # Create placeholder if image fails to load
                meme_images[gesture] = create_placeholder_image(gesture)
        else:
            # Create placeholder if image doesn't exist
            meme_images[gesture] = create_placeholder_image(gesture)
    
    return meme_images


def create_placeholder_image(gesture_name):
    """
    Create a placeholder image with text when meme image is not found.
    
    Args:
        gesture_name: Name of the gesture
        
    Returns:
        Numpy array representing the placeholder image
    """
    # Create a colored background
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    
    # Different colors for different gestures
    colors = {
        "thumbs_up": (0, 255, 0),      # Green
        "peace": (255, 255, 0),         # Cyan
        "fist": (0, 0, 255),            # Red
        "open_palm": (255, 0, 255),     # Magenta
        "ok_sign": (0, 255, 255),       # Yellow
        "none": (128, 128, 128)         # Gray
    }
    
    color = colors.get(gesture_name, (255, 255, 255))
    img[:] = color
    
    # Add text
    text = gesture_name.upper().replace("_", " ")
    cv2.putText(img, text, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 0, 0), 3, cv2.LINE_AA)
    
    return img


def resize_meme(meme_image, target_height):
    """
    Resize meme image to match the target height while maintaining aspect ratio.
    
    Args:
        meme_image: Original meme image
        target_height: Desired height in pixels
        
    Returns:
        Resized image
    """
    height, width = meme_image.shape[:2]
    aspect_ratio = width / height
    new_width = int(target_height * aspect_ratio)
    
    # Resize image
    resized = cv2.resize(meme_image, (new_width, target_height), 
                        interpolation=cv2.INTER_AREA)
    
    return resized


def main():
    """
    Main function to run the Gesture Meme Tracker application.
    """
    print("=" * 60)
    print("Gesture Meme Tracker running — press 'q' to quit.")
    print("=" * 60)
    print("\nDetectable gestures:")
    print("👍 Thumbs up")
    print("✌️  Peace sign")
    print("✊ Fist")
    print("🖐️  Open palm")
    print("👌 OK sign")
    print("\nMake sure your hand is visible to the camera!")
    print("=" * 60)
    
    # Create images folder if it doesn't exist
    images_folder = os.path.join(os.path.dirname(__file__), "images")
    if not os.path.exists(images_folder):
        os.makedirs(images_folder)
        print(f"\nCreated images folder at: {images_folder}")
        print("Note: Add your meme images to this folder!")
        print("Expected filenames:", list(GESTURE_MEMES.values()))
        print()
    
    # Load meme images
    meme_images = load_meme_images(images_folder)
    
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    # Check if webcam opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam!")
        return
    
    # Set camera resolution (optional, adjust as needed)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # Initialize MediaPipe Hands
    with mp_hands.Hands(
        static_image_mode=False,          # False for video stream
        max_num_hands=1,                   # Detect one hand at a time
        min_detection_confidence=0.7,      # Confidence threshold for detection
        min_tracking_confidence=0.5        # Confidence threshold for tracking
    ) as hands:
        
        current_gesture = "none"
        
        while True:
            # Read frame from webcam
            success, frame = cap.read()
            
            if not success:
                print("Failed to grab frame from webcam!")
                break
            
            # Flip frame horizontally for mirror view
            frame = cv2.flip(frame, 1)
            
            # Get frame dimensions
            frame_height, frame_width, _ = frame.shape
            
            # Convert BGR to RGB (MediaPipe uses RGB)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Process the frame with MediaPipe Hands
            results = hands.process(rgb_frame)
            
            # Check if hand(s) detected
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw hand landmarks on the frame
                    mp_drawing.draw_landmarks(
                        frame, 
                        hand_landmarks, 
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                        mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
                    )
                    
                    # Detect gesture
                    current_gesture = detect_gesture(hand_landmarks)
            
            # Get appropriate meme for current gesture
            meme = meme_images.get(current_gesture, meme_images["none"])
            
            # Resize meme to match frame height
            meme_resized = resize_meme(meme, frame_height)
            
            # Ensure meme width doesn't exceed reasonable size
            meme_height, meme_width = meme_resized.shape[:2]
            if meme_width > frame_width:
                meme_resized = cv2.resize(meme_resized, (frame_width, frame_height))
                meme_width = frame_width
            
            # Create combined display (webcam + meme side by side)
            combined_width = frame_width + meme_width
            combined_frame = np.zeros((frame_height, combined_width, 3), dtype=np.uint8)
            
            # Place webcam frame on the left
            combined_frame[:, :frame_width] = frame
            
            # Place meme on the right
            combined_frame[:, frame_width:frame_width + meme_width] = meme_resized
            
            # Add text overlay showing current gesture
            gesture_text = current_gesture.replace("_", " ").title()
            cv2.putText(combined_frame, f"Gesture: {gesture_text}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                       1, (0, 255, 255), 2, cv2.LINE_AA)
            
            # Add instructions
            cv2.putText(combined_frame, "Press 'q' to quit", 
                       (10, frame_height - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.6, (255, 255, 255), 1, cv2.LINE_AA)
            
            # Display the combined frame
            cv2.imshow('Gesture Meme Tracker', combined_frame)
            
            # Check for 'q' key press to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("\nQuitting Gesture Meme Tracker...")
                break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print("Application closed successfully!")


if __name__ == "__main__":
    main()

