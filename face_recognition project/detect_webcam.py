import face_recognition
import cv2

# Get a reference to the webcam (usually 0 or 1, depending on your setup)
webcam = cv2.VideoCapture(0)

while True:
    # Capture a single frame from the webcam
    ret, frame = webcam.read()

    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(frame)

    # Loop through each face and draw a rectangle around it
    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the output frame
    cv2.imshow("Webcam", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()