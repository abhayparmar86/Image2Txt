# Improved Version with added functionalities:
# Key Improvements:
# User Instructions: The user is informed to press 's' to save the image and 'q' to quit without saving.
# Error Handling: Added error handling for the camera not opening and frame grabbing failure.
# Code Organization: Separated the logic into functions for capturing the image, extracting text, and running the main program flow.
# Dependencies Check: Basic checks are included to ensure camera access and file saving.

# application for camera link: https://github.com/UB-Mannheim/tesseract/wiki

import cv2
from PIL import Image
from pytesseract import pytesseract
import matplotlib.pyplot as plt

def capture_image():
    """
    Capture an image from the webcam and save it to a file when 's' is pressed.
    """
    try:
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            print("Error: Could not open webcam.")
            return None

        while True:
            ret, image = camera.read()
            if not ret:
                print("Error: Failed to grab frame.")
                break

            # Convert the image from BGR to RGB for displaying
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Display the image using matplotlib
            plt.imshow(rgb_image)
            plt.title('Press "s" to save and exit, "q" to quit without saving')
            plt.show(block=False)

            if plt.waitforbuttonpress():
                key = plt.get_current_fig_manager().canvas.key_press_handler_id
                plt.close()
                if key == ord('s'):
                    cv2.imwrite('test1.jpg', image)
                    print("Image saved as 'test1.jpg'.")
                    return 'test1.jpg'
                elif key == ord('q'):
                    print("Quit without saving.")
                    break

        camera.release()
        return None

    except Exception as e:
        print(f"An error occurred while capturing image: {e}")
        return None

def extract_text(image_path):
    """
    Extract text from the saved image using Tesseract OCR.
    """
    try:
        path_to_tesseract = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(Image.open(image_path))
        print("Extracted Text:")
        print(text.strip())
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")

def main():
    image_path = capture_image()
    if image_path:
        extract_text(image_path)

if __name__ == "__main__":
    main()