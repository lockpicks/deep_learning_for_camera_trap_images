''' Code generates the train.txt file necessary for getting the locations of the images '''

import os

path_to_train = './phase1/train.txt' # path to where train.txt will be generated, will need to change based on phases
path_to_data = '/dfs6/pub/hackathon/DATASETS/SERENGETI/DOWNLOADED/S8' # Change S10 to whatever season you need
f = open(path_to_train, 'w')

for root, dirs, files in os.walk(path_to_data, topdown = True):
    for name in files:
        f.write(os.path.join(root, name) + "\n")

f.close()