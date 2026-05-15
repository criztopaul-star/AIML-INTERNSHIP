import cv2
import os

# Enter student name
name = input("Enter Student Name: ")

# Create folder
dataset_path = "dataset"
person_path = os.path.join(dataset_path, name)

os.makedirs(person_path, exist_ok=True)

# Open webcam
cap = cv2.VideoCapture(0)

count = 0

print("Capturing face images...")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera not working")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        count += 1

        face = frame[y:y+h, x:x+w]

        file_name = os.path.join(
            person_path,
            f"{count}.jpg"
        )

        cv2.imwrite(file_name, face)

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Image {count}",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Capturing Faces", frame)

    # Stop after 30 images
    if count >= 30:
        break

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Dataset Created Successfully!")