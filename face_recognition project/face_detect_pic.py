import face_recognition
import cv2

# Specify the path to the input image file
image_path = "your_file.jpg"  # Replace with the actual path to your image file
image = face_recognition.load_image_file(image_path)

# Find all face locations in the image
face_locations = face_recognition.face_locations(image)

# Loop through each face and draw a rectangle around it
for face_location in face_locations:
    top, right, bottom, left = face_location
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    

# Save the output image with rectangles drawn around faces
output_path = "output.jpg"
cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

# Display the output image
cv2.imshow("Output", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()
