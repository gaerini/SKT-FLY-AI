import face_recognition
import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)
# Load a sample picture and learn how to recognize it.
bill_image = face_recognition.load_image_file("./face_recognition_examples/img/known/Bill Gates.jpg")
bill_face_encoding = face_recognition.face_encodings(bill_image)[0]
steve_image = face_recognition.load_image_file("./face_recognition_examples/img/known/Steve Jobs.jpg")
steve_face_encoding = face_recognition.face_encodings(steve_image)[0]
jhkim_image = face_recognition.load_image_file("./sampletest.jpg")
jhkim_face_encoding = face_recognition.face_encodings(jhkim_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
bill_face_encoding,
steve_face_encoding,
jhkim_face_encoding
]
known_face_names = [
"Bill Gates",
"Steve Jobs",
"Jiho"
]

video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
print("!")
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, top - 35), (right, top), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, top - 6), font, 1.0, (255, 255, 255), 1)
        # Display the resulting image
    cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()