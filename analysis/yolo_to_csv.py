import os
import pandas as pd

# yolo txt file 
yolo_path = '../../data/yolo/'
yolo_file = os.listdir(yolo_path)

# train data
train_dataset = pd.DataFrame(columns={'id', 'classes', 'x_center', 'y_center', 'w', 'h'})

#=====================================
# Convert json txt to csv
#=====================================

idx = 0
for file in yolo_file:

    # Read file
    f = open(yolo_path + file, 'r')

    while True:
        # Read line in file
        line = f.readline()

        if not line:
            break
        
        # Input data (classes, x_center, y_center, w, h)
        id = file.split('.')[0]
        train_dataset.loc[idx, 'id'] = id

        train_dataset.loc[idx, 'classes'] = line.split()[0]
        train_dataset.loc[idx, 'x_center'] = line.split()[1]
        train_dataset.loc[idx, 'y_center'] = line.split()[2]
        train_dataset.loc[idx, 'w'] = line.split()[3]
        train_dataset.loc[idx, 'h'] = line.split()[4]

        idx += 1

    f.close()

print(len(train_dataset['id'].unique()))
print(len(train_dataset))
train_dataset.to_csv('train_dataset.csv')
