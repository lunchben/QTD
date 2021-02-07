import torch
import torchvision
from PIL import Image
# from .make_txt import make_txt_file

class SuchDataset(object):
    def __init__(self, dataset_type, transform=None, update_dataset=False):
        dataset_path = ''  # image path
        if update_dataset:
            make_txt_file(dataset_path)  # update datalist

        self.transform = transform
        self.sample_list = list()
        self.dataset_type = dataset_type
        f = open(dataset_path + self.dataset_type + '/txt_file.txt')
        lines = f.readlines()
        for line in lines:
            self.sample_list.append(line.strip())
        f.close()

    def __getitem__(self, item):
        item = self.sample_list[item]
        # img = cv2.imread(item.split(' _')[0])  # openCV read image
        img = Image.open(item.split(' _')[0])  # PIL read image
        if self.transform is not None:
            img = self.transform(img)
        label = int(item.split(' _')[-1])
        return img, label

    def __len__(self):
        return len(self.sample_list)

def make_txt_file(path):
    fl = []
    for _, _, files in os.walk(path):
        fl.append(files)
    with open('txt_file.txt', 'w') as f:
        for k in range(len(fl[0])):
            name = fl[0][k]
            cls = name[0]
            realname = path + '\\' + name + ' ' + '_{}'.format(cls)
            f.write("{}\n".format(realname))
        f.close()