import streamlit as st
import face_recognition
import cv2
import numpy as np
import pandas as pd
import os
from datetime import datetime
from PIL import Image

DATASET_PATH = "dataset"
ATTENDANCE_FILE = "attendance.csv"

st.title("Face Detection Attendance System")

menu = ["Register Face", "Mark Attendance", "View Attendance"]
choice = st.sidebar.selectbox("Menu", menu)

# -----------------------------
# REGISTER FACE
# -----------------------------
if choice == "Register Face":

    st.header("Register Student Face")

    name = st.text_input("Enter Student Name")

    uploaded_file = st.file_uploader(
        "Upload Face Image",
        type=["jpg", "png", "jpeg"]
    )

    if st.button("Save Face"):

        if name and uploaded_file:

            person_dir = os.path.join(DATASET_PATH, name)

            os.makedirs(person_dir, exist_ok=True)

            image_path = os.path.join(person_dir, "1.jpg")

            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.success(f"{name} registered successfully!")

# -----------------------------
# LOAD KNOWN FACES
# -----------------------------
known_face_encodings = []
known_face_names = []

if os.path.exists(DATASET_PATH):

    for person_name in os.listdir(DATASET_PATH):

        person_folder = os.path.join(DATASET_PATH, person_name)

        for image_name in os.listdir(person_folder):

            image_path = os.path.join(person_folder, image_name)

            image = face_recognition.load_image_file(image_path)

            encodings = face_recognition.face_encodings(image)

            if len(encodings) > 0:
                known_face_encodings.append(encodings[0])
                known_face_names.append(person_name)

# -----------------------------
# MARK ATTENDANCE
# -----------------------------
if choice == "Mark Attendance":

    st.header("Upload Image for Attendance")

    uploaded_image = st.file_uploader(
        "Upload Image",
        type=["jpg", "png", "jpeg"]
    )

    if uploaded_image:

        image = Image.open(uploaded_image)
        image_np = np.array(image)

        face_locations = face_recognition.face_locations(image_np)
        face_encodings = face_recognition.face_encodings(
            image_np,
            face_locations
        )

        marked_names = []

        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(
                known_face_encodings,
                face_encoding
            )

            name = "Unknown"

            face_distances = face_recognition.face_distance(
                known_face_encodings,
                face_encoding
            )

            if len(face_distances) > 0:

                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

            marked_names.append(name)

        st.image(image, caption="Processed Image")

        for name in marked_names:

            if name != "Unknown":

                now = datetime.now()

                date = now.strftime("%Y-%m-%d")
                time = now.strftime("%H:%M:%S")

                attendance_data = {
                    "Name": [name],
                    "Date": [date],
                    "Time": [time]
                }

                df = pd.DataFrame(attendance_data)

                # Avoid duplicate entry
                if os.path.exists(ATTENDANCE_FILE):

                    old_df = pd.read_csv(ATTENDANCE_FILE)

                    duplicate = (
                        (old_df["Name"] == name) &
                        (old_df["Date"] == date)
                    ).any()

                    if not duplicate:
                        df.to_csv(
                            ATTENDANCE_FILE,
                            mode='a',
                            header=False,
                            index=False
                        )

                else:
                    df.to_csv(
                        ATTENDANCE_FILE,
                        index=False
                    )

                st.success(f"Attendance Marked for {name}")

            else:
                st.warning("Unknown Face Detected")

# -----------------------------
# VIEW ATTENDANCE
# -----------------------------
if choice == "View Attendance":

    st.header("Attendance Report")

    if os.path.exists(ATTENDANCE_FILE):

        df = pd.read_csv(ATTENDANCE_FILE)

        st.dataframe(df)

        st.download_button(
            "Download Attendance CSV",
            df.to_csv(index=False),
            "attendance.csv",
            "text/csv"
        )

    else:
        st.warning("No attendance records found.")