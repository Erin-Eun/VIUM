'''
https://jjeongil.tistory.com/653
'''
#%%
import os
import cv2
import time
import seaborn as sns
import matplotlib.pyplot as plt

# 레이블이랑 이미지 경로 저장
label_path = '../../data/label/'
image_path = '../../data/train/'

# 레이블 파일 리스트와 이미지 파일 리스트 저장
label_list = os.listdir(label_path)
image_list = os.listdir(image_path)

# 라벨 파일명과 이미지 파일명을 오름차순 정렬
label_list.sort()
image_list.sort()

#==================================
# Total image rgb average
#==================================
# Blue, Green, Red
#==================================

# blue = 0
# green = 0
# red = 0
# cnt = 0

# start_time = time.time()

# for image in image_list:

#     # Open image file
#     img = cv2.imread(image_path + image)

#     # Select size (1920 x 1080), (1080, 1920)
#     if (img.shape[0] == 1080) and (img.shape[1] == 1920):
#         blue += cv2.mean(img)[:3][0]
#         green += cv2.mean(img)[:3][1]
#         red += cv2.mean(img)[:3][2]
#         cnt += 1

# print(blue, green, red)
# print(cnt)

# print('Average of Blue : ', blue/cnt)
# print('Average of Green : ', green/cnt)
# print('Average of Red : ', red/cnt)

# print(time.time() - start_time, '초 걸렸습니다.')

# #----- Plot
# x = ['Blue', 'Green', 'Red']
# y = [98.35975792550558, 110.27690571088444, 140.04454807379514]

# plt.figure(figsize=(6, 6))
# plt.title('Average of RGB in total image')
# sns.barplot(x, y, palette=["#1D63A5", "#2B9322", "#D90016"])
# plt.text(-0.04, 102, 98)
# plt.text(0.9, 114, 110)
# plt.text(1.9, 144, 140)
# plt.ylim(0, 150)
# plt.show()
# %%
