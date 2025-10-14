"""
Quick dependency checker for Gesture Meme Tracker
Run this script to verify all required packages are installed correctly
"""

import sys

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("=" * 60)
    print("Checking dependencies for Gesture Meme Tracker...")
    print("=" * 60)
    
    required_packages = {
        'cv2': 'opencv-python',
        'mediapipe': 'mediapipe',
        'numpy': 'numpy'
    }
    
    all_installed = True
    
    for module_name, package_name in required_packages.items():
        try:
            if module_name == 'cv2':
                import cv2
                version = cv2.__version__
            elif module_name == 'mediapipe':
                import mediapipe
                version = mediapipe.__version__
            elif module_name == 'numpy':
                import numpy
                version = numpy.__version__
            
            print(f"✓ {package_name:20s} - Installed (v{version})")
        except ImportError:
            print(f"✗ {package_name:20s} - NOT INSTALLED")
            all_installed = False
    
    print("=" * 60)
    
    if all_installed:
        print("✓ All dependencies are installed!")
        print("\nYou can now run: python gesture_meme_tracker.py")
    else:
        print("✗ Some dependencies are missing!")
        print("\nInstall missing packages with:")
        print("  pip install -r requirements.txt")
    
    print("=" * 60)
    
    # Check webcam availability
    print("\nChecking webcam availability...")
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print("✓ Webcam is accessible!")
            cap.release()
        else:
            print("✗ Cannot access webcam!")
            print("  Make sure no other application is using it.")
    except Exception as e:
        print(f"✗ Error checking webcam: {e}")
    
    print("=" * 60)

if __name__ == "__main__":
    check_dependencies()

