import wx

# app=wx.App() #实例化一个主循环
# frame=wx.Frame(None) #实例化一个窗口
# frame.Show() #调用窗口显示功能
# app.MainLoop() #启动主循环

# 图形化编写
app=wx.App()
frame=wx.Frame(None,title='similarity evaluation',pos=(1000,200),size=(500,400)) #创建一个窗口
path_text=wx.TextCtrl(frame,pos=(5,5),size=(350,24)) #创建输入文本框
open_button=wx.Button(frame,label='打开',pos=(370,5),size=(50,24)) #创建一个‘打开’按钮
save_button=wx.Button(frame,label='保存',pos=(430,5),size=(50,24)) #创建一个‘保存’按钮
content_text=wx.TextCtrl(frame,pos=(5,39),size=(475,300),style=wx.TE_MULTILINE) # style=wx.TE_MULTILINE实现文本换行功能，若没有此功能则内容一行显示。
frame.Show()
app.MainLoop()

#事件绑定
# 定义事件函数，函数有且只有一个参数，event

def openfile(event):  #定义打开文件事件
    path=path_text.GetValue()
    with open(path,'r',encoding='utf-8') as f: #encoding 指定打开文件为utf8编码，避免写文件时出现编码错误
        content_text.SetValue(f,read())

# 将按钮和事件绑定
open_button.Bind(wx.EVT_BUTTON,openfile())


# 完整代码
import wx

def openfile(event):  #定义打开文件事件
    path=path_text.GetValue()
    with open(path,'r',encoding='utf-8') as f: #encoding参数是为了在打开文件时将编码转为utf8
        content_text.SetValue((f.read()))

app=wx.App()
frame=wx.Frame(None,title='GUI for test',pos=(1000,200),size=(500,400))

path_text=wx.TextCtrl(frame,pos=(5,5),size=(350,24))
open_button=wx.Button(frame,label='打开',pos=(370,5),size=(50,24))
open_button.Bind(wx.EVT_BUTTON,openfile())  #绑定打开文件事件到open_button按钮上
save_button=wx.Button(frame,label='保存',pos=(430,5),size=(50,24))
content_text=wx.TextCtrl(frame,pos=(5,39),size=(475,300),style=wx.TE_MULTILINE) # we.TE_MULTILINE可以实现以滚动条方式多行显示文本，若不加此功能文本文档显示为一行

frame.Show()
app.MainLoop()


# 尺寸器，窗口随着拉长短而改变
box=wx.BoxSizer() #不带参数表示默认实例化一个水平尺寸器
box.Add(path_text,proportion=5,flag=wx.EXPAND|wx.ALL,border=3)#添加组件
box.Add(save_button,proportion=2,flag=wx.EXPAND|wx.ALL,border=3)#添加组件

v_box=wx.BoxSizer(wx.VERTICAL) #实例化一个垂直尺寸器
v_box.Add(box,proportion=1,flag=wx.EXPAND|wx.ALL,border=3)
v_box.Add(content_text,proportion=5,flag=wx.EXPAND|wx.ALL,border=3)

# 设置主尺寸器
panel.SetSizer(v_box)
frame.Show()
app.MainLoop()

