from deepface import DeepFace

result = DeepFace.verify(img1_path = "images/Abby/Abby-1.jpg", img2_path = "images/Abby/Abby-3.jpg")
print(result)

result = DeepFace.verify(img1_path = "images/Abby/Abby-4.jpg", img2_path = "images/Abby/Abby-8.jpg")
print(result)
