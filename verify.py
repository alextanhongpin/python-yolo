from deepface import DeepFace

result = DeepFace.verify(img1_path = "images/Abby/Abby-1.jpg", img2_path = "images/Abby/Abby-3.jpg")
print(result)

result = DeepFace.verify(img1_path = "images/Abby/Abby-4.jpg", img2_path = "images/Abby/Abby-8.jpg")
print(result)


result = DeepFace.find(img_path = "images/Abby/Abby-1.jpg", db_path= "images/Abby")
print(result)

objs = DeepFace.analyze(
  img_path = "images/Abby/Abby-1.jpg", actions = ['age', 'gender', 'race', 'emotion']
)
print(objs)


face_objs = DeepFace.extract_faces(
  img_path = "images/Abby/Abby-1.jpg", align = True
)
print(face_objs)
