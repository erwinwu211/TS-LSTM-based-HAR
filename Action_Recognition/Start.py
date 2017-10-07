# -*- coding: utf-8 -*-

"""
Module implementing getpath.
"""
import os
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import phonon
from PyQt4.phonon import Phonon
from PyQt4.QtGui import *  
from PyQt4.QtCore import *
from mlab.releases import latest_release as matlab
#from PyQt4 import QtWidgets
from Ui_Hellowindow import Ui_Dialog
global filePath
global fileName
global predictions_RGB_LRCN
filePath = 0
fileName = 0
predictions_RGB_LRCN=[]
class getpath(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(getpath, self).__init__(parent)
        self.setupUi(self)
        global timer
        timer=QTimer(self)  
	timer.count =0.0
        self.connect(timer,SIGNAL("timeout()"),self.showTime)  
        #global t  
        #t=QTime()

    #open button
    @QtCore.pyqtSignature("")
    def on_pushButton_clicked(self):
        global filePath
	global fileName
        filePath= QFileDialog.getOpenFileName(self,
                    "QFileDialog.getOpenFileName()",
                     self.label.text(),
                    "Video File(*.avi)")
        if filePath:
            self.label.setText(filePath)
    	    self.progressBar.setProperty("value", 0)
	    fileName=0
    @QtCore.pyqtSignature("")
    def on_pushButton_5_clicked(self):
        global filePath
	global fileName
        filePath= QFileDialog.getOpenFileName(self,
                    "QFileDialog.getOpenFileName()",
                     self.label.text(),
                    "Video File(*.avi)")
        if filePath:
            self.label_2.setText(filePath)
    	    self.progressBar_2.setProperty("value", 0)
	    fileName=0

    #process button        
    @QtCore.pyqtSignature("")
    def on_pushButton_3_clicked(self):
	global fileName	 
	global filePath
	global fileNumber
	if filePath:   
		fileName=unicode(filePath).split("/")[-1]
		fileName=fileName[:-4]
		os.system('sh extract_frames.sh '+unicode(filePath)+' 10/1')
		self.progressBar.setProperty("value", 100)
		path="frames/"+fileName
		fileNumber=0
		fs=os.listdir(path)
		for i in fs:
			if os.path.isfile(os.path.join(path,i)):
				fileNumber += 1
	else:
		result=QMessageBox.information(self,"Error",  "Please choose a video file first!") 
    @QtCore.pyqtSignature("")
    def on_pushButton_9_clicked(self):
	global fileName	 
	global filePath
	global fileNumber
	if filePath:   
		fileName=unicode(filePath).split("/")[-1]
		fileName=fileName[:-4]
		os.system('sh extract_frames.sh '+unicode(filePath)+' 10/1')
		self.progressBar_2.setProperty("value", 100)
		path="frames/"+fileName
		fileNumber=0
		fs=os.listdir(path)
		for i in fs:
			if os.path.isfile(os.path.join(path,i)):
				fileNumber += 1
	else:
		result=QMessageBox.information(self,"Error",  "Please choose a video file first!") 


    #start button
    @QtCore.pyqtSignature("")
    def on_pushButton_4_clicked(self):
	global fileName	
	global filePath	
	if fileName:
		self.videoPlayer.load(phonon.Phonon.MediaSource(filePath))
		self.videoPlayer.play()

		##############################################################
		#recognition by caffe start
		import numpy as np
		import glob
		caffe_root = '../../'
		sys.path.insert(0,caffe_root + 'python')
		import caffe
		caffe.set_mode_gpu()
		caffe.set_device(0)
		import pickle
		RGB_video_path = 'frames/'		
		from classify_video import LRCN_classify_video
		from classify_video import initialize_transformer
		video = fileName
		ucf_mean_RGB = np.zeros((3,1,1))
		ucf_mean_RGB[0,:,:] = 103.939
		ucf_mean_RGB[1,:,:] = 116.779
		ucf_mean_RGB[2,:,:] = 128.68
		transformer_RGB = initialize_transformer(ucf_mean_RGB, False)

		# Extract list of frames in video
		RGB_frames = glob.glob('%s%s/*.jpg' %(RGB_video_path, video))
		
		#Models and weights
		lstm_model = 'deploy_lstm.prototxt'
		RGB_lstm = 'Lstm_model_RGB_iter_30000.caffemodel'

		#start clssify
		RGB_lstm_net =  caffe.Net(lstm_model, RGB_lstm, caffe.TEST)
		global predictions_RGB_LRCN
		class_RGB_LRCN, predictions_RGB_LRCN = \
			 LRCN_classify_video(RGB_frames, RGB_lstm_net, transformer_RGB, False)
		del RGB_lstm_net
		
		#Load activity label hash
		action_hash = pickle.load(open('action_hash_rev.p','rb'))
		#Output result
		result=QMessageBox.information(self,"Result",  "The video is classified as "+action_hash[class_RGB_LRCN[0]])
		print "Single frame classification complete!"		
		print "1.The prediction of "+action_hash[class_RGB_LRCN[0]]+" is "+str(predictions_RGB_LRCN[class_RGB_LRCN[0]])
		print "2.The prediction of "+action_hash[class_RGB_LRCN[1]]+" is "+str(predictions_RGB_LRCN[class_RGB_LRCN[1]])
		print "3.The prediction of "+action_hash[class_RGB_LRCN[2]]+" is "+str(predictions_RGB_LRCN[class_RGB_LRCN[2]])
		print "4.The prediction of "+action_hash[class_RGB_LRCN[3]]+" is "+str(predictions_RGB_LRCN[class_RGB_LRCN[3]])
		print "5.The prediction of "+action_hash[class_RGB_LRCN[4]]+" is "+str(predictions_RGB_LRCN[class_RGB_LRCN[4]])
		
	else:
		result=QMessageBox.information(self,"Error",  "PLease process the video first!")  

    #opticalflow button        
    @QtCore.pyqtSignature("")
    def on_pushButton_7_clicked(self):
	global fileName	 
	global filePath
	global predictions_RGB_LRCN
	if predictions_RGB_LRCN and filePath:
		os.system("rm -rf flow")
		timer.start(1000)
		matlab.create_flow_images_LRCN()
		
	else:
		result=QMessageBox.information(self,"Error",  "Please do the single Frame classification first!") 
    @QtCore.pyqtSignature("")
    def on_pushButton_11_clicked(self):
	global fileName	 
	global filePath
	global predictions_RGB_LRCN
	if predictions_RGB_LRCN and filePath:
		os.system("rm -rf flow")
		timer.start(1000)
		matlab.create_flow_images_LRCN()
		
	else:
		result=QMessageBox.information(self,"Error",  "Please process the single Frame first!") 

    #TS classify button        
    @QtCore.pyqtSignature("")
    def on_pushButton_10_clicked(self):
	global fileName	 
	global filePath
	global predictions_RGB_LRCN
	if predictions_RGB_LRCN:   
		##############################################################
		#recognition by caffe start
		import numpy as np
		import glob
		caffe_root = '../../'
		sys.path.insert(0,caffe_root + 'python')
		import caffe
		caffe.set_mode_gpu()
		caffe.set_device(0)
		import pickle
		flow_video_path = 'flow/'		
		from classify_video import LRCN_classify_video
		from classify_video import initialize_transformer
		video = fileName
		ucf_mean_flow = np.zeros((3,1,1))
		ucf_mean_flow[:,:,:] = 128
		transformer_flow = initialize_transformer(ucf_mean_flow,True)

		# Extract list of frames in video
		flow_frames = glob.glob('%s%s/*.jpg' %(flow_video_path, video))
		
		#Models and weights
		lstm_model = 'deploy_lstm.prototxt'
		flow_lstm = 'Lstm_model_flow_iter_50000.caffemodel'

		#start clssify
		flow_lstm_net =  caffe.Net(lstm_model, flow_lstm, caffe.TEST)
		class_flow_LRCN, predictions_flow_LRCN = \
			 LRCN_classify_video(flow_frames, flow_lstm_net, transformer_flow, True)
		del flow_lstm_net
		
		#model fusion
		
		for i in range(len(predictions_RGB_LRCN)):
			predictions_flow_LRCN[i]= 0.5*predictions_flow_LRCN[i]+0.5*predictions_RGB_LRCN[i]

		#Load activity label hash
		action_hash = pickle.load(open('action_hash_rev.p','rb'))	
		#Output result
		result=QMessageBox.information(self,"Result",  "The video is classified as "+action_hash[class_flow_LRCN[0]])
		print "Two-Stream classification complete!"		
		print "1.The prediction of "+action_hash[class_flow_LRCN[0]]+" is "+str(predictions_flow_LRCN[class_flow_LRCN[0]])
		print "2.The prediction of "+action_hash[class_flow_LRCN[1]]+" is "+str(predictions_flow_LRCN[class_flow_LRCN[1]])
		print "3.The prediction of "+action_hash[class_flow_LRCN[2]]+" is "+str(predictions_flow_LRCN[class_flow_LRCN[2]])
		print "4.The prediction of "+action_hash[class_flow_LRCN[3]]+" is "+str(predictions_flow_LRCN[class_flow_LRCN[3]])
		print "5.The prediction of "+action_hash[class_flow_LRCN[4]]+" is "+str(predictions_flow_LRCN[class_flow_LRCN[4]])
		
	else:
		result=QMessageBox.information(self,"Error",  "Please compute the optical flow frames first!")  
   

    #Train button        
    @QtCore.pyqtSignature("")
    def on_pushButton_6_clicked(self):
	global fileName	 
	global filePath
	if filePath:
		os.system("cp train/run_lstm_flow.sh ./")
		os.system("sh run_lstm_flow.sh")


    def showTime(self):
	global fileNumber
	timer.count += 100.0/(fileNumber*1.1)
	self.progressBar_3.setProperty("value", timer.count)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = getpath()
    dlg.show()
    sys.exit(app.exec_())
