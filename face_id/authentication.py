#!/usr/bin/env python3
import cv2
from simple_facerec import SimpleFacerec
import time

def authenticate(callback):
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        face_locations, face_names, is_recognised = sfr.detect_known_faces(frame)
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or is_recognised:
            break

    cap.release()
    cv2.destroyAllWindows()
    callback(is_recognised)

def callback(is_recognised):
    print("Recognition status:", "Recognised" if is_recognised else "Not Recognised")

def main():
    print("Starting authentication system...")
    authenticate(callback)

if __name__ == "__main__":
    main()
