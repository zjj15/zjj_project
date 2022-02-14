一，车机初始状态设置：
ipod蓝牙连接成功，并重复播放一曲歌曲
USB根目录下放至少一首歌曲和一个视频
ipod：用USB线连接车机
ill：亮屏状态

二,执行顺序：
1，根目录下的文件不能重复多次运行，各个子目录可以多次运行
2，测试Case时，先执行一遍00_env_setup.tcs
如，01_SourceAccOffOn:执行一次500回case：即00_env_setup.tcs：一回，2：500回

三，外设
1，Action的case执行时，必须连接高清摄像头
（1）设备名及其他参数定义在以下文件，可以修改：
	..\00_env_setup.tcs\00_env_setup.py
（2）backCamera的照片，可以通过以下路径修改：
	..\common\rev_on_off.tcs\pic\BackCamera_Normal.png