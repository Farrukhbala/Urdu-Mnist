from PIL import Image
import numpy as np
import sys
import os
import csv

# default format can be changed as needed
def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList
    
# load the original image
myFileList = createFileList(r'C:\Users\Zodiac\Desktop\Urdu-Practice - Copy')

for file in myFileList:
    print(file)
    img_file = Image.open(file)
    # img_file.show()

    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    # ret,thresh2 = cv2.threshold(img_file,127,255,cv2.THRESH_BINARY_INV)
    # img_grey.save('result.png')
    # img_grey.show()

    # Save Greyscale values
    value = np.asarray(img_file.getdata(), dtype=np.int).reshape((img_file.size[1], img_file.size[0]))
    value = value.flatten()
    print(value)
    with open("urdu.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(value)

# import os

# # for root, dirs, files in os.walk(r'C:\Users\Zodiac\Desktop\Urdu-Practice - Copy'):
# #     for filename in files:
# #         data = []
# #         data.append(files)
# # print(data)

# def createFileList(myDir, format='.jpg'):
#     fileList = []
#     print(myDir)
#     for root, dirs, files in os.walk(myDir, topdown=False):
#         for name in files:
#             if name.endswith(format):
#                 fullName = os.path.join(root, name)
#                 fileList.append(fullName)
#     return fileList

# myFileList = createFileList(r'C:\Users\Zodiac\Desktop\Urdu-Practice - Copy')
# print(myFileList)