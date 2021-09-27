import os
import json
from PIL import Image

# 레이블이랑 이미지 경로 저장

# train image
# label_path = '../../data/label/'
# image_path = '../../data/train/'
# txt_path = '../../data/test_yolo/'

# test image
image_path = '../../test_image_1_193/'
label_path = '../../test_label_json_1_193/'
txt_path = '../../data/test_yolo/'

# 레이블 파일 리스트와 이미지 파일 리스트 저장
label_list = os.listdir(label_path)
image_list = os.listdir(image_path)

# 라벨 파일명과 이미지 파일명을 오름차순 정렬
label_list.sort()
image_list.sort()

# print(len(label_list)) # 1779
# print(len(image_list)) # 1779

# Labeling list
label_name = {'tray':'0', 'paper':'1', 'plastic_cup':'2', 'lid':'3', 'ketchup':'4', 'garbage':'5',
              'can':'6', 'potato_chip_box':'7', 'potato_chip':'8', 'hamburger':'9', 'dipping_sauce':'10', 
              'nuggets_box':'11', 'paper_cup':'12', 'glass':'13', 'straw':'14'}

#=====================================
# Convert json to yolo format
#=====================================

# Function converted json to yolo
def convert(size, box):
    dw = 1./size[0] # w
    dh = 1./size[1] # h

    x = (box[0] + box[1])/2.0 # xmin, xmax, ymin, ymax
    y = (box[2] + box[3])/2.0
    
    w = box[1] - box[0]
    h = box[3] - box[2]

    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    
    return (x,y,w,h)


for label in label_list:

    image_file = label.replace('.json', '.jpg') # image file name
    
    txt_name = label.replace('.json', '.txt') # text file name
    txt_file = txt_path + txt_name

    # Open json file
    with open(label_path + label, 'r') as json_file:
        json_data = json.loads(json_file.read())
        
        # Open Image
        img = Image.open(image_path + image_file) 
        tmp1 = int(img.size[0])
        tmp2 = int(img.size[1])
        
        # 1. 이미지를 세로로 돌린 경우 -> 큰 값을 width로 지정함 
        if tmp1 >= tmp2:
            w = tmp1
            h = tmp2
        else:
            w = tmp2
            h = tmp1

        for label in json_data['shapes']: 
            (x1, y1), (x2, y2) = label['points']

            xmin = min(x1, x2)
            xmax = max(x1, x2)
            ymin = min(y1, y2)
            ymax = max(y1, y2)

            # 2. json과 yolo에서 이미지 레이블링 값이 1이 넘는 경우-> <0 >height or width 
            if xmin < 0:
                xmin = 0
            if ymin < 0:
                ymin = 0
            if xmax > w:
                xmax = w
            if ymax > h:
                ymax = h

            # Convert json to yolo format
            box = (xmin, xmax, ymin, ymax)
            result = convert((w, h), box)

            # Save yolo format in text file
            f = open(txt_file, 'a')
            data = label_name[label['label']] + " " + " ".join([str(r) for r in result]) + "\n"
            print(label['label'], label_name[label['label']], " " + " ".join([str(r) for r in result]) + "\n" )
            
            f.write(data)
            f.close()


        




