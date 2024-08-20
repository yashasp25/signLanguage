import cv2

# Attempt to open the default camera (index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video device.")
else:
    print("Camera is accessible. Press 'q' to exit.")
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error: Could not read frame.")
            break

    cap.release()
    cv2.destroyAllWindows()
