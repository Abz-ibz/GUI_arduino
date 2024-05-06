import cv2
import face_recognition
import numpy as np
import glob
import os

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        print("Loading encoding images from:", images_path)
        image_files = glob.glob(os.path.join(images_path, "*.*"))
        for img_path in image_files:
            img = cv2.imread(img_path)
            if img is None:
                continue
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            if encodings := face_recognition.face_encodings(rgb_img):
                self.known_face_encodings.append(encodings[0])
                basename = os.path.basename(img_path)
                filename = os.path.splitext(basename)[0]
                self.known_face_names.append(filename)

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        is_recognised = False

        if face_encodings:
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances) if face_distances.size > 0 else -1
                if best_match_index != -1 and matches[best_match_index]:
                    name = self.known_face_names[best_match_index]
                    is_recognised = True
                else:
                    name = "Unknown"
                face_names.append(name)

        face_locations = (np.array(face_locations) * (1 / self.frame_resizing)).astype(int)
        return face_locations, face_names, is_recognised
