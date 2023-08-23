import cv2  # Import the OpenCV library for computer vision
import time  # Import the time module for time-related operations

# Initialize the video capture object using the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Initialize a variable to keep track of the previous time
pTime = 0

# Start an infinite loop to continuously capture and display frames from the camera
while True:
    # Capture a frame from the camera
    success, img = cap.read()
    
    # Convert the color space of the captured image from BGR to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Get the current time
    cTime = time.time()
    
    # Calculate the frames per second (FPS) using the time difference between the current and previous time
    fps = 1 / (cTime - pTime)
    
    # Update the previous time
    pTime = cTime
    
    # Draw the calculated FPS on the image
    cv2.putText(img, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the image with the FPS text
    cv2.imshow("Test", img)
    
    # Wait for a key event for 1 millisecond (0 means wait indefinitely, 1 means wait for 1 ms)
    cv2.waitKey(1)

# Clean up: Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
