import os

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

# if __name__ == '__main__':
#     path = r'F:\360MoveData\Users\Administrator\Desktop\xuanchuan\raw_faces'
#     make_txt_file(path)