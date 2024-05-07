import threading
import cv2
from face_id.simple_facerec import SimpleFacerec
import time

def authenticate(callback):
    def run():
        sfr = SimpleFacerec()
        sfr.load_encoding_images("face_id/images/")
        cap = cv2.VideoCapture(0)
        window_name = "Frame"

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            face_locations, face_names, is_recognised = sfr.detect_known_faces(frame)
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

            cv2.imshow(window_name, frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or is_recognised:
                break

        cap.release()
        cv2.destroyWindow(window_name)
        callback(is_recognised)

    thread = threading.Thread(target=run)
    thread.start()

