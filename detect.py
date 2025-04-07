from pathlib import Path
# import face_recognition
# from deepface import DeepFace


def encode_known_faces( model: str = 'hog', dir:Path = Path('images')):
    # names = []
    # encodings = []
    for filepath in dir.glob("[!Samples]*/*.jpg"):
        print(filepath.parent.name)


encode_known_faces('hello')
