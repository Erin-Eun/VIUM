
#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from PIL import Image

import os
import json
import cv2

# 레이블이랑 이미지 경로 저장
label_path = '../../data/label'
image_path = '../../data/train'

# 레이블 파일 리스트와 이미지 파일 리스트 저장
label_list = os.listdir(label_path)
image_list = os.listdir(image_path)

# 라벨 파일명과 이미지 파일명을 오름차순 정렬
label_list.sort()
image_list.sort()

# print(len(label_list)) # 1779
# print(len(image_list)) # 1779



# #=======================================
# # Image Size 
# #=======================================
# img_size_list = []
# img_size = {(1920, 1080):0, (960, 1280):0, (1440, 1080):0, (1079, 1440):0, 
#             (4032, 3024):0, (3024, 4032):0, (1280, 961):0, (1280, 960):0,
#             (852, 480):0, (3024, 3024):0, (959, 1280):0, (1080, 1920):0}

# for image in image_list:
#     img = image_path + '/' + image
    
#     img = Image.open(img)
#     img_size_list.append(img.size)

#     img_size[img.size] += 1


# print(len(list(set(img_size_list)))) # 이미지 사이즈 규격 종류 12가지
# print(img_size)

# # Sort Decending
# img_size = dict(sorted(img_size.items(), key=lambda x : x[1], reverse=True))

# # Plot
# x = [str(i) for i in img_size.keys()]
# y = list(img_size.values())

# plt.title('Image Size')
# sns.barplot(y, x)

# # plt.barh(x, y, color="darksalmon")
# # plt.grid(True, axis='x')
# plt.grid(color='#EAEAEA')
# plt.show()



# #=======================================
# # Box Size 
# #=======================================

# idx = 1
# df = pd.DataFrame(index=range(1,18049), columns=['width', 'height', 'class']) # 데이터프레임 생성

# for i in range(len(label_list)):

#     # Open json file
#     with open(label_path + '/' + label_list[i], 'r') as json_file:
#         json_data = json.loads(json_file.read())

#         labels = json_data['shapes']

#         # Input Data into the dataframe
#         for label in labels:
#             (x1, y1), (x2, y2) = label['points']
#             df.loc[idx, 'width'] = x2-x1
#             df.loc[idx, 'height'] = y2-y1
#             df.loc[idx, 'class'] = label['label']

#             idx += 1

# #----- subplots: 전체 레이블을 각각 그래프로 살펴봄
# classes = df['class'].unique() # 클래스 종류

# fig, axes = plt.subplots(5, 3, figsize=(10, 10), constrained_layout=True) # 레이블이 15개임
# fig.suptitle('Size of box', size=30, )

# for i in range(len(classes)):
#     tmp = df[df['class'] == classes[i]] # 하나의 레이블만 담긴 데이터프레임

#     axes[i//3, i%3].set_title(classes[i])
#     sns.scatterplot(data=tmp, x='width', y='height', ax=axes[i//3, i%3])

#     # Remove y label
#     if i%3 != 0:
#         axes[i//3, i%3].set_ylabel("")

#     # Remove x label 
#     if i//3 != 4:
#         axes[i//3, i%3].set_xlabel("")



# #=======================================
# # Box Size By Category
# #=======================================
# # plastic : lid, dipping_sauce
# # garbage : garbage, ketchup
# # paper : potato_chip_box, nuggets_box
# # food waste : potato_chip, hamburger
# #=======================================

# idx = 1
# df = pd.DataFrame(index=range(1,18049), columns=['width', 'height', 'class']) # 데이터프레임 생성

# for i in range(len(label_list)):

#     # Open json file
#     with open(label_path + '/' + label_list[i], 'r') as json_file:
#         json_data = json.loads(json_file.read())

#         labels = json_data['shapes']

#         # Input Data into the dataframe
#         for label in labels:
#             (x1, y1), (x2, y2) = label['points']
#             df.loc[idx, 'width'] = x2-x1
#             df.loc[idx, 'height'] = y2-y1
#             df.loc[idx, 'class'] = label['label']

#             idx += 1

# #----- By category

# # plastic
# plastic = df[(df['class'] == 'lid') | (df['class'] == 'dipping_sauce')]
# graph = sns.scatterplot(data=plastic, x='width', y='height', hue='class', palette='colorblind')
# graph.legend_.set_title(None)
# plt.title('Plastic')
# plt.legend(loc='upper left')
# plt.show()

# # garbage
# garbage = df[(df['class'] == 'garbage') | (df['class'] == 'ketchup')]
# graph = sns.scatterplot(data=garbage, x='width', y='height', hue='class', palette='colorblind')
# graph.legend_.set_title(None)
# plt.title('Garbage')
# plt.legend(loc='upper left')
# plt.show()

# # paper
# paper = df[(df['class'] == 'potato_chip_box') | (df['class'] == 'nuggets_box')]
# graph = sns.scatterplot(data=paper, x='width', y='height', hue='class', palette='colorblind')
# graph.legend_.set_title(None)
# plt.title('Paper')
# plt.legend(loc='upper left')
# plt.show()

# # food waste
# food_waste = df[(df['class'] == 'potato_chip') | (df['class'] == 'hamburger')]
# graph = sns.scatterplot(data=food_waste, x='width', y='height', hue='class', palette='colorblind')
# plt.title('Food Waste')
# graph.legend_.set_title(None)
# plt.legend(loc='upper left')
# plt.show()



# #=======================================
# # Object Count (duplicated)
# #=======================================

# cnt = 0 # 총 객체 개수

# label_set = {'tray':0, 'paper':0, 'plastic_cup':0, 'lid':0, 'ketchup':0,
#              'garbage':0, 'can':0, 'potato_chip':0, 'potato_chip_box':0,
#              'hamburger':0, 'dipping_sauce':0, 'nuggets_box':0, 'paper_cup':0,
#              'glass':0, 'straw':0}

# for i in range(len(label_list)):

#     with open(label_path + '/' + label_list[i], 'r') as json_file:
#         json_data = json.loads(json_file.read())

#         labels = json_data['shapes']
        
#         # 한 이미지 내 레이블 저장
#         for label in labels: 
#             label_set[label['label']] += 1
#             cnt += 1

# print(cnt) # 18048개
# print(label_set)
# print(cnt/14) # 약 1289개 (각 라벨별 개수)



# #=======================================
# # Graph 1 (no duplicated)
# #=======================================

# # label_set : 한 파일 내에 몇 개의 종류가 존재하는지 개수 확인
# label_set = {'tray':0, 'paper':0, 'plastic_cup':0, 'lid':0, 'ketchup':0,
#              'garbage':0, 'can':0, 'potato_chip':0, 'potato_chip_box':0,
#              'hamburger':0, 'dipping_sauce':0, 'nuggets_box':0, 'paper_cup':0,
#              'glass':0, 'straw':0}

# # 각 이미지에 존재하는 레이블 종류 저장
# for i in range(len(label_list)):
#     tmp = [] # tmp : 레이블 저장 리스트 

#     with open(label_path + '/' + label_list[i], 'r') as json_file:
#         json_data = json.loads(json_file.read())

#         labels = json_data['shapes']
        
#         # 한 이미지 내 레이블 저장
#         for label in labels: 
#             tmp.append(label['label'])

#     # 레이블 중복 제거 
#     tmp = list(set(tmp)) 

#     # 레이블명 개수 저장 
#     for item in tmp:
#         label_set[item] += 1

# print(label_set)





# %%
