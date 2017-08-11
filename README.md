# generate-signature
在纸上手写一个签名，然后拍照成图片，用该程序处理图片，生成透明背景的电子签名照

def dianziqianming(name,value):
    """"""
    im = Image.open(name).convert("L")
    im = im.point(lambda i: 255 if i>value else 0)
    '''制作透明图'''
    '''新生成一张等大小的图，通过读取灰度图值，操作新图的每一个像素(R,G,B,A)'''
    im2 = Image.new("RGBA", (im.size[0], im.size[1]))
    draw =ImageDraw.Draw(im2)
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if im.getpixel((x,y)) is 255:
                draw.rectangle((x, y, x, y),fill=(255, 255, 255, 0))
            else:
                draw.rectangle((x, y, x, y), fill=(0, 0, 0, 255))
             
    '''保存签名透明图'''
    fname, fext = os.path.splitext(name)
    path = os.path.join("透明") #在当前文件夹中生成一个“透明”子文件夹
    if not os.path.exists(path):
        os.makedirs(path)
    path = os.path.join(path,fname+'.png') #添加文件名称
    im2.save(path)
    print(path)

    '''制作缩小图'''
    ratio=float(im.size[1])/im.size[0]
    k=int(ratio*47)
    im3 = im2.resize((47, k),Image.ANTIALIAS)
    ''' 保存缩小图'''
    path2 = os.path.join("缩略")
    if not os.path.exists(path2):
        os.makedirs(path2)
    path2 = os.path.join(path2,fname+'.png')
    im3.save(path2)
    print(path2)
    
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
        dianziqianming(name,100)
