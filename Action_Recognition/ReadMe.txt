#本系统由上海交通大学2013级电子信息与电气工程学院信息安全专业的吴烔Erwin Wu（学号5130369026）在伯克利大学Jeff Donahue等人的LRCN模型的基础上进行改良后所设计，未经允许严禁转载。

本系统由Python和Matlab所编写，需要64位Ubuntu环境下运行，此外还必须有caffe，cuda，cudnn和opencv等环境支持。

文件目录内容介绍：
Start.py：系统的python启动接口，从这里启动整个系统。
Start.sh：系统的启动运行程序，调用python启动Start.py。
Ui_Hellowindow.py:系统的python窗体界面，基于pyQT实现。
extract_frames.sh：视频文件的单帧提取预处理程序，调用ffmpeg逐帧提取视频。
classify_video.py：系统的识别调用程序，调用caffe实现正向传播和分类，识别的启动接口。
action_hash_rev.p：行为类型的哈希值pickel文件，保存各种行为对应的数字代码。
create_flow_images_LRCN.m：光流帧提取的matlab程序，通过调用Brox光流的matlab程序实现。
mex_OF.m等文件：Brox提供的光流算法的matlab实现，在其官方Github中获得。
各种.prototxt文件：caffe的相关参数文件，详见论文算法设计章节。

实际运行系统还需要训练好的caffemodel文件，由于文件较大此处不附上。
