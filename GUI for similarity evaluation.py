# from similarity_flann import *
import wx
import cv2
import os,re
import numpy as np
from os import walk
from os.path import join


def show_image(event):
    dir=content_text2.GetValue()
    file_name=event.GetItem();file_name=file_name.GetText()
    image=cv2.imread(dir+file_name)
    image=cv2.resize(image,(300,300))
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    h,w=image.shape[:2]
    wxbmp = wx.BitmapFromBuffer(w, h, image)
    bitmap=wx.StaticBitmap(frame, bitmap=wxbmp,pos=(600,350))

    # cv2.namedWindow("show", 0)
    # cv2.imshow('show',image)


def OnButton1(event):
    """"""
    dlg = wx.DirDialog(frame,message=u"选择文件夹",
                        style=wx.DD_DEFAULT_STYLE)
    if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        content_text2.SetValue(path+'/')
    dlg.Destroy()

def OnButton2(event):
    """"""
    dlg = wx.FileDialog(frame,message=u"选择文件",
                        defaultDir=os.getcwd(),
                        defaultFile="",
                        style=wx.FD_OPEN)
    if dlg.ShowModal() == wx.ID_OK:
        name = dlg.GetFilename()
        content_text3.SetValue(name)
    dlg.Destroy()

def run_program(event):
    # str = input('your photo name:')#得是带图片格式的那种
    # std=input('your standard:')
    path=content_text2.GetValue()
    # if '1' in p:
    #     path='F:/python/codes/gamma-AI/ph/'
    # else:path='F:/python/codes/gamma-AI/pictures for assessment/'
    content_text1.DeleteAllItems()
    str=content_text3.GetValue()
    std=Slider_box.GetValue()
    cut1 = str.split('.')
    cut1 = cut1[0]
# your_photo_path = 'F:/python/codes/gamma-AI/ph(new)/'+str
    your_photo_path=path+str
    query = cv2.imread(your_photo_path, 0)
    sift = cv2.xfeatures2d.SIFT_create()
    query_kp, query_ds = sift.detectAndCompute(query, None)

    # folder = 'F:/python/codes/gamma-AI/ph(new)/'
    #     folder='F:/ph/'
    folder = path
    descriptors = [];descriptors_other=[]
    # 获取特征数据文件名
    for (dirpath, dirnames, filenames) in walk(folder):
        for f in filenames:
            if f.endswith("npy") :descriptors.append(f)
            else:descriptors_other.append(f)
            L=[x.split('.') for x in descriptors_other];D={key:value for key,value in L}
        for desc in range(len(descriptors)):
            strr = ''.join(descriptors[desc])
            cut2 = strr.split('.')
            cut2 = cut2[0]
            st = folder + strr
            if (cut1 == cut2):
                index_params = dict(algorithm=0, trees=5)
                search_params = dict(checks=50)
                flann = cv2.FlannBasedMatcher(index_params, search_params)
                potential_culprits = {}
                for d in descriptors:
                    # 将图像query与特征数据文件的数据进行匹配
                    matches = flann.knnMatch(np.load(st), np.load(join(folder, d)), k=2)
                    # 清除错误匹配
                    good = []
                    for m, n in matches:
                        if m.distance < 0.7 * n.distance:
                            good.append(m)
                    # 输出每张图片与目标图片的匹配数目
                    potential_culprits[d] = len(good)

                # 获取最多匹配数目的图片
                max_matches = max(potential_culprits.values())
                potential_suspect = None


                for culprit, matches in potential_culprits.items():
                    matching_ratio = matches / max_matches
                    if matching_ratio > std/100:
                        potential_suspect = culprit
                        k=potential_suspect.split('.')[0]
                        K=D[k]
                        content_text1.InsertItem(0,'%s'%(potential_suspect.replace("npy", K)))
                        content_text1.SetItem(0,1,'%d%%'%(matching_ratio*100))

def creat_npy(event):
    path=content_text2.GetValue()
    files = []
    for (dirpath1, dirnames1, filenames1) in walk(path):
        files.extend(filenames1)
    for f in files:
            img = cv2.imread(join(path, f), 0)
            keypoints1, descriptors1 = cv2.xfeatures2d.SIFT_create().detectAndCompute(img, None)
            descriptor_file=re.sub(r'([a-zA-Z]{3})$','npy',f)
            np.save(join(path, descriptor_file), descriptors1)


app=wx.App()
frame=wx.Frame(None,title='similarity evaluation',pos=(100,0),size=(1000,800))
text_1_name=wx.StaticText(frame,label='选择图片库：',pos=(5,25),size=(100,20))
content_text2=wx.TextCtrl(frame,pos=(5,50),size=(200,30))
FIle_chose1=wx.FileDialog(frame,'图片库选择',style=wx.FD_OPEN,pos=(5,50))
button_5=wx.Button(frame,label='选择图片库',pos=(225,50),size=(80,24))
content_name=wx.StaticText(frame,label='搜寻结果：',pos=(5,175),size=(100,20))
content_text1=wx.ListCtrl(frame,pos=(5,190),size=(1000,600),style=wx.LC_REPORT|wx.LC_VRULES|wx.LC_HRULES)
content_text1.InsertColumn(1,'matching rate',width=100)
content_text1.InsertColumn(0,'matching pictures',format=wx.LIST_FORMAT_CENTRE,width=300)
content_text1.InsertColumn(2,'showing pictures',format=(wx.LIST_FORMAT_CENTRE),width=600)
content_text3=wx.TextCtrl(frame,pos=(5,120),size=(200,30))
button_6=wx.Button(frame,label='选择图片',pos=(225,120),size=(80,24))
FIle_chose2=wx.FileDialog(frame,'图片选择',style=wx.FD_OPEN,pos=(5,120))
text_2_name=wx.StaticText(frame,label='图片名称：',pos=(5,100),size=(100,20))
Slider_box=wx.Slider(frame,value=10,minValue=10,maxValue=100,pos=(400,50),size=(300,-1),style=wx.SL_LABELS|wx.SL_HORIZONTAL|wx.SL_AUTOTICKS)
Slider_box.SetTickFreq(1)
text_3_name=wx.StaticText(frame,label='选择标准(matching rate)：',pos=(400,25),size=(200,-1))
button_7=wx.Button(frame,label='开始检索',pos=(470,150),size=(80,24))
button_8=wx.Button(frame,label='生成npy文件',pos=(370,150),size=(80,24))

# 事件绑定
button_8.Bind(wx.EVT_BUTTON,creat_npy)
button_7.Bind(wx.EVT_BUTTON,run_program)
button_6.Bind(wx.EVT_BUTTON,OnButton2)
button_5.Bind(wx.EVT_BUTTON,OnButton1)
content_text1.Bind(wx.EVT_LIST_ITEM_SELECTED,show_image)

frame.Show()
app.MainLoop()