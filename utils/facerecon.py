import numpy as np
import cv2
import face_recognition

def find_face_embeddings(image_binary):
    # Convert the binary data to numpy array
    nparr = np.frombuffer(image_binary, np.uint8)
    # Read the image
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Get face encodings from the image
    face_enc = face_recognition.face_encodings(image)
    # Return face encodings
    return face_enc[0] if face_enc else None

def compare_faces(emb1, emb2):
    emb1 = np.array(emb1)
    emb2 = np.array(emb2)
    is_same = face_recognition.compare_faces([emb1], emb2)[0]
    if is_same:
        distance = face_recognition.face_distance([emb1], emb2)
        distance = round(distance[0] * 100)
        accuracy = 100 - round(distance)
    return is_same


if __name__ == "__main__":
    # Example usage:
    with open("testimg\d1.jpg", "rb") as file:
        image_binary_1 = file.read()

    with open("testimg\\sigma.jpg", "rb") as file:
        image_binary_2 = file.read()

    image_1 = list(find_face_embeddings(image_binary_1))
    image_2 = list(find_face_embeddings(image_binary_2))
    print(image_2)
    print(compare_faces(image_1, image_2))