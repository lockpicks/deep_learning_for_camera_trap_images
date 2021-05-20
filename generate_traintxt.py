''' Code generates the train.txt file necessary for getting the locations of the images '''

import os, json

path_to_metadata = 'SnapshotSerengetiS01.json'
metadata_file = open(path_to_metadata, 'r')
metadata = json.load(metadata_file)
metadata_file.close()
img_counter = 0


def get_label(fname):
    imageid = fname.replace('/dfs6/pub/hackathon/DATASETS/SERENGETI/DOWNLOADED/', '').replace('.JPG', '')
    for x in metadata['annotations']:
        if x['image_id'] == imageid:
            return x['category_id']
    print("HUGE ERROR: couldn't find category id?")
    return 0 # this should never happen



if __name__ == '__main__':
    metadata_ann = metadata['annotations']
    path_to_train = './phase1/train.txt' # path to where train.txt will be generated, will need to change based on phases
    path_to_data = '/dfs6/pub/hackathon/DATASETS/SERENGETI/DOWNLOADED/'
    f = open(path_to_train, 'w')
    
    for x in metadata_ann:
        fpath = path_to_data + x['image_id'] + '.JPG'
        f.write(fpath + " " + str(x['category_id']) + "\n")
        img_counter += 1
        if img_counter % 5000 == 0:
            print(fpath + " " + str(x['category_id']))
            
    print("total number of paths in train.txt:", img_counter)
    
    f.close()
#     for root, dirs, files in os.walk(path_to_data, topdown = True):
#         for name in files:
#             fpath = os.path.join(root, name)
#             label = get_label(fpath)
#             f.write(fpath + " " + str(label) + "\n")

    
