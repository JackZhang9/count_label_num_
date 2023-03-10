import os


def num_label():
    path=r'D:\pycharmProjects\datasets\xizhilang\labels\train2017'
    img_list=os.listdir(path)
    nums=len(set(img_list))
    print(nums)
    return 0

num_label()

