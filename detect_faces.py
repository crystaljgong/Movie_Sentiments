import os
import boto3
import io
from PIL import Image
'''
Things to do:
-put this script in the same place where you put the folder of images
ex. /Desktop/detect_faces.py and /Desktop/imgs_lalaland
-install boto3 (don't remember the precise command)
-make a new folder in the images directory called faces
-run the script and enter the the name of the img folder
'''
# takes the input of the directory
directory = input("Enter the name of directory: ")
rekognition = boto3.client('rekognition', region_name='us-east-1')

for filename in sorted(os.listdir(directory)):
    
    if (filename.endswith('.png')):
       
        image = Image.open(directory+"/"+filename)
        image_width = image.size[0]
        image_height = image.size[1]
        stream = io.BytesIO()
        image.save(stream,format="JPEG")
        image_binary = stream.getvalue()
        filename_noExtension = filename.split('.')[0]
        
        response = rekognition.detect_faces(
            Image={'Bytes':image_binary}                                        
        )

        all_faces=response['FaceDetails']

        i = 1
        for faceDetail in all_faces:
        
            box=faceDetail['BoundingBox']
            x1 = int(box['Left'] * image_width) 
            y1 = int(box['Top'] * image_height) 
            x2 = int(box['Left'] * image_width + box['Width'] * image_width)
            y2 = int(box['Top'] * image_height + box['Height']  * image_height) 
            image_crop = image.crop((x1,y1,x2,y2))
            image_crop.save(directory + "/faces/" + filename_noExtension + "face" + str(i) + ".jpg")
            i+=1
    
    print(os.path.join(directory, filename))
