# %%

import matplotlib.pyplot as plt
import seaborn as sns

import os
import json
import cv2

# 레이블이랑 이미지 경로 저장
label_path = '../../data/0804_label'
image_path = '../../data/0804_train'

# 레이블 파일 리스트와 이미지 파일 리스트 저장
label_list = os.listdir(label_path)
image_list = os.listdir(image_path)

# 라벨 파일명과 이미지 파일명을 오름차순 정렬
label_list.sort()
image_list.sort()

#=======================================
# Graph 2
#=======================================

# ex) plastic_cup 

plastic_cup_points = []
plastic_cup_images = []
num = 1 

for i in range(len(label_list)):
    with open(label_path + '/' + label_list[i], 'r') as json_file: 
        json_data = json.loads(json_file.read())
        labels = json_data['shapes']

        # 플라스틱 컵들의 포인트들 확인
        for label in labels:
            if label['label'] == 'plastic_cup':
    
                plastic_cup_points.append(label['points'])
                plastic_cup_images.append(image_list[i])

# print(len(plastic_cup_points)) # 196
# print(len(plastic_cup_images)) # 196

# 플라스틱 컵에 해당하는 레이블 이미지만 출력
for i in range(len(plastic_cup_images)):
    img = image_path + '/' + plastic_cup_images[i]
    read_img = cv2.imread(img)

    x1, y1 = list(map(int, plastic_cup_points[i][0]))
    x2, y2 = list(map(int, plastic_cup_points[i][1]))

    # 사각형 모양대로 자름
    rect_img = read_img[y1:y2, x1:x2]
    plt.subplot(5, 5, i+1)
    plt.imshow(rect_img)
    plt.axis('off')

    # 예시로 25장만 출력
    if i == 24:
        break

plt.tight_layout(h_pad=0.5, w_pad=0.1)
plt.show()

###### 이미지 좌표값 마이너스인 것 예외 처리해야함
