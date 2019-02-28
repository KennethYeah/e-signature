from PIL import Image
import os,sys

def dianziqianming(name,value):
    im = Image.open(name).convert("L")
    im = im.point(lambda pixel: 255 if pixel > value else 0)
    alpha = im.point(lambda pixel: 255 if pixel==0 else 0)
    im = im.convert('RGBA')
    im.putalpha(alpha)
    im.save(os.path.join('签名',os.path.splitext(name)[0]+'.png'))
    return '处理完成签名%s'%name
             

def GetFileList():
    FileList = []
    filenames = os.listdir(sys.path[0])
    for fn in filenames:
        try:
            hz = fn.split('.')[1]
        except:
            pass
        else:
            if hz in ['jpg','png','JPG','PNG']:
                FileList.append(fn)
    return FileList

if __name__=='__main__':
    names = GetFileList()
    for name in names:
        dianziqianming(name,110)
