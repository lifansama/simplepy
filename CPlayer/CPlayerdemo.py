import os,sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon,QImage,QPixmap
from ffpyplayer.player import MediaPlayer
from PyQt5.QtWidgets import QMessageBox,QApplication,QMainWindow,QFileDialog
from CPlayer import Ui_MainWindow
class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Listadd()
        self.step=0
        self.loop=1
        self.flag=True
    def Listadd(self):
        if os.path.isfile('CPlayerlist.txt'):
            with open('CPlayerlist.txt') as f:
                for filelist in f:
                    filelist=filelist.strip()
                    self.list.addItem(filelist)
    def Add(self):
        filelists,_=QFileDialog.getOpenFileNames(self,'添加到播放列表','.','媒体文件(*)')
        self.list.addItems(filelists)
        self.Listchanged()
    def Remove(self):
        self.list.takeItem(self.list.currentRow())
        self.Listchanged()
    def Clear(self):
        self.list.clear()
        os.remove('CPlayerlist.txt')
    def Listchanged(self):
        with open('CPlayerlist.txt','w') as f:
            for i in range(self.list.count()):
                f.write(self.list.item(i).text()+'\n')
    def Loop(self):
        if self.loop==0:
            self.loop=1
            self.bloop.setIcon(QIcon(r'img\withloop.png'))
            self.bloop.setToolTip('循环播放')
        else:
            self.loop=0
            self.bloop.setIcon(QIcon(r'img\withoutloop.png'))
            self.bloop.setToolTip('取消循环')
    def Play(self):
        try:
            if self.flag:
                self.playitem=self.list.currentItem().text()
                self.player=MediaPlayer("%s"%self.playitem)
                self.timer=QTimer()
                self.timer.start(50)
                self.timer.timeout.connect(self.Show)
                self.steptimer=QTimer()
                self.steptimer.start(1000)
                self.steptimer.timeout.connect(self.Step)
                self.flag=False
                self.bplay.setIcon(QIcon(r'img\pause.png'))
                self.bplay.setToolTip('暂停')
            else:
                if self.list.currentItem().text()==self.playitem:
                    self.player.toggle_pause()
                    if self.player.get_pause():
                        self.timer.stop()
                        self.steptimer.stop()
                        self.bplay.setIcon(QIcon(r'img\play.png'))
                        self.bplay.setToolTip('播放')
                    else:
                        self.timer.start()
                        self.steptimer.start()
                        self.bplay.setIcon(QIcon(r'img\pause.png'))
                        self.bplay.setToolTip('暂停')
                else:
                    self.step=0
                    self.stime.setValue(0)
                    self.playitem=self.list.currentItem().text()
                    self.player=MediaPlayer("%s"%self.playitem)
                    self.timer.start()
                    self.steptimer.start()
        except:
            QMessageBox.warning(self,'错误','找不到要播放的文件！')
    def Show(self):
        frame,self.val=self.player.get_frame()
        self.lmedia.setPixmap(QPixmap(''))
        if self.val!='eof' and frame is not None:
            img,t=frame
            data=img.to_bytearray()[0]
            width,height=img.get_size()
            qimg=QImage(data,width,height,QImage.Format_RGB888)
            self.lmedia.setPixmap(QPixmap.fromImage(qimg))
        self.mediatime=self.player.get_metadata()['duration']
        self.stime.setMaximum(int(self.mediatime))
        mediamin,mediasec=divmod(self.mediatime,60)
        mediahour,mediamin=divmod(mediamin,60)
        playmin,playsec=divmod(self.step,60)
        playhour,playmin=divmod(playmin,60)
        self.ltime.setText('%02d:%02d:%02d/%02d:%02d:%02d'%(playhour,playmin,playsec,mediahour,mediamin,mediasec))
    def Stop(self):
        if self.flag==False:
            self.player.close_player()
            self.timer.stop()
            self.steptimer.stop()
            self.step=0
            self.loop=1
            self.flag=True
            self.stime.setValue(0)
            self.ltime.setText('')
            self.bplay.setIcon(QIcon(r'img\play.png'))
            self.bplay.setToolTip('播放')
            self.lmedia.setPixmap(QPixmap(''))
    def Curvol(self):
        self.curvol=self.svolume.value()
    def Mute(self):
        if self.flag==False:
            if self.player.get_volume()!=0:
                self.player.set_volume(0)
                self.bmute.setIcon(QIcon(r'img\withoutvolume.png'))
                self.bmute.setToolTip('取消静音')
            else:
                if self.svolume.value()!=0:
                    self.player.set_volume(self.svolume.value())
                else:
                    self.player.set_volume(self.curvol/100)
                    self.svolume.setValue(self.curvol)
                self.bmute.setIcon(QIcon(r'img\withvolume.png'))
                self.bmute.setToolTip('静音')
    def Volume(self):
        if self.flag==False:
            if self.svolume.value()==0:
                self.bmute.setIcon(QIcon(r'img\withoutvolume.png'))
                self.bmute.setToolTip('取消静音')
            else:
                self.bmute.setIcon(QIcon(r'img\withvolume.png'))
                self.bmute.setToolTip('静音')
            self.player.set_volume(self.svolume.value()/100)
    def Step(self):
        if self.step>=int(self.mediatime):
            self.step=int(self.mediatime)
            if self.loop==0:
                self.step=0
                self.flag=True
                self.Play()
            else:
                if self.val=='eof':
                    self.timer.stop()
                    self.steptimer.stop()
                    self.step=0
                    self.loop=1
                    self.flag=True
                    self.stime.setValue(0)
                    self.player.close_player()
                    self.bplay.setIcon(QIcon(r'img\play.png'))
                    self.bplay.setToolTip('播放')
        else:
            self.step+=1
            self.stime.setValue(self.step)
    def Slidechanged(self):
        self.step=self.stime.value()
    def Slidemoved(self):
        self.timer.start()
        self.steptimer.start()
        self.player=MediaPlayer("%s"%self.playitem,ff_opts={'ss':self.step})
        self.bplay.setIcon(QIcon(r'img\pause.png'))
        self.bplay.setToolTip('暂停')
    def Fastforward(self):
        self.step+=10
        if self.step>=int(self.mediatime):
            self.stime.setValue(int(self.mediatime))
        self.timer.start()
        self.steptimer.start()
        self.player=MediaPlayer("%s"%self.playitem,ff_opts={'ss':self.step})
        self.bplay.setIcon(QIcon(r'img\pause.png'))
        self.bplay.setToolTip('暂停')
    def Fastback(self):
        self.step-=10
        if self.step<=0:
            self.step=0
        self.timer.start()
        self.steptimer.start()
        self.player=MediaPlayer("%s"%self.playitem,ff_opts={'ss':self.step})
        self.bplay.setIcon(QIcon(r'img\pause.png'))
        self.bplay.setToolTip('暂停')
if __name__=='__main__':
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())