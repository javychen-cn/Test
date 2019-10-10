
import re,requests,os
from lxml import etree
import subprocess
import shutil

shutil.rmtree('pictures',True)#删除原文件夹,初始化。
headers1 = {'user-agent': 'Mozilla/5.0'}
def download_pictures (url):
    response = requests.get (url,headers = headers1)
    base_link = etree.HTML (response.text).xpath ('//div[@class="main-image"]//img/@src')[0][0:-6] #提取首张图片的下载地址
    page_info = etree.HTML (response.text).xpath ('//div[@class="pagenavi"]//span/text()')    #提取当前系列图片的页码信息列表
    max_page = int(page_info[-2])   #提取图片的最大页码
    for i in range(1,max_page+1):
        page= str (i).zfill(2)
        download_link = base_link+ str(page)+'.jpg'
        headers = {'Referer':url+'{}'.format (i),'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        response = requests.get (download_link,headers = headers)
        pic_name = download_link[-9:-4]
        print ('目前第{}套图片,共{}张  正在下载第{} 张图片......'.format (list_cnt,max_page,i))
        with open ("pictures/%s.jpg"%pic_name,'wb') as f:
            f.write (response.content)

def get_pictures ():
    url = 'https://www.mzitu.com/all/'
    global list_cnt,save_path
    list_cnt = 1
    reponse = requests.get (url,headers = headers1)
    regax = '\d\d\w\:.+\>'
    list_pool = re.findall (regax,reponse.text)
    for li in list_pool:
        url = li.split(' ')[2].split('"')[1]
        save_path = 'pictures'
        if not os.path.exists('pictures'):
            os.mkdir('pictures')
        download_pictures(url)
        list_cnt += 1
        if list_cnt>=22:
            break
if __name__ == '__main__':
    get_pictures()

