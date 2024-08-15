import cv2
from pyzbar.pyzbar import decode

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Width
cam.set(4, 480)  # Height

camera = True

while camera:
    success, frame = cam.read()

    if not success:
        break

    for barcode in decode(frame):
        qr_data = barcode.data.decode('utf-8')
        print(f"QR Code detected: {qr_data}")

        # Write the QR code data to a text file
        with open("scanned_qr_code.txt", "w") as file:
            file.write(qr_data)

        # Automatically exit after scanning a QR code
        camera = False
        break

    cv2.imshow("QR Code Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera = False

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
