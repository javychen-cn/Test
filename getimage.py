import os
import random
import shutil

shutil.rmtree('images',True)#删除原文件夹,初始化。
def img_list():
    global old_img_path
    old_img_path = 'pictures'
    old_img_list = os.listdir(old_img_path)
    new_img_list = []
    for i in range(20):
        random_img = random.choice(old_img_list)
        new_img_list.append(random_img)
        i += 1
    return new_img_list
def copyimg():
    new_img_list = img_list()
    new_img_path = 'images'
    if not os.path.exists('images'):
        os.mkdir('images')
    for filename in new_img_list:
        shutil.copyfile(os.path.join(old_img_path, filename), os.path.join(new_img_path, filename))

if __name__ == '__main__':
    copyimg()