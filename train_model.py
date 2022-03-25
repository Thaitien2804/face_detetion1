# from lib import *
#
# recornized_images = cv2.face.LBPHFaceRecognizer_create()
#
# path = 'dataset'
#
# def getImagesWithID(path):
#     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
#     print(imagePaths)
#     faces = []
#     IDs = []
#     for imagePath in imagePaths:
#          faceImg = Image.open(imagePath).convert('L')
#          faceNp = np.array(faceImg, 'uint8')
#          print(faceNp)
#          id = int(imagePath.split('\\')[1].split('.')[1])
#          faces.append(faceNp)
#          IDs.append(id)
#
#     return IDs, faces
#
# faces, IDs = getImagesWithID(path)
# recornized_images.train(faces, np.array(IDs))
# if not os.path.exists('recognizer'):
#     os.makedirs('recognizer')
# recornized_images.save('recognizer/trainingData.yml')
from lib import *
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'
def getImageWithId(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    #print(imagePaths)
    faces = []
    IDs= []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        print(faceNp)
        Id = int(imagePath.split('\\')[1]. split('.')[1])
        faces.append(faceNp)
        IDs. append(Id)
        cv2.imshow("training", faceNp)
        cv2.waitKey(10)


    return faces, IDs
faces, Ids = getImageWithId(path)
recognizer.train(faces, np.array(Ids))
if not os.path.exists('recognizer'):
    os.makedirs('recognizer')
recognizer.save('recognizer/trainingData.yml')
print('Training data saved to recognizer/trainingData.yml')
cv2.destroyAllWindows()