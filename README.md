python控制minecraft
1.安装JAVA
这里我就不说了，自己上网搜教程（releases里有安装包）
2.建立minecraftJAVA版服务器
在某某位置新建一个文件夹，将spigot-1.21.jar文件放入文件夹，新建start.bat，将以下代码粘贴到start.bat里：
java -Xms1024M -Xmx1024M -jar spigot-1.21.jar nogui
PAUSE
保存编辑，双击打开
文件夹里会刷新出一些文件，打开eula.txt，将eula=false改为eula=true，保存关闭
再次运行start.bat，这个时候服务器就安装好了
在mc服务器终端输入stop,关闭服务器
编辑server.properties文件
将online-mode=true改为online-mode=false
再次运行start.bat，这个时候服务器就配置好了好了
3.给mc服务器安装控制插件
在mc服务器终端输入stop,关闭服务器
将RaspberryJuice.zip解压，打开jars文件夹，选择一个jar包，这里以raspberryjuice-1.12.1.jar为例
打开mc服务器文件夹，再打开plugins文件夹，将raspberryjuice-1.12.1.jar放到这里，在次运行start.bat
如果能在plugins文件夹里发现RaspberryJuice文件夹，那就成功了
4.安装python
这里我就不说了，自己上网搜教程（releases里有安装包）
5.python安装mcpi
按win+R打开运行框，输入cmd回车，在黑窗口中输入：pip install mcpi，就安装成功了
6.打开Minecraft
解压PCL2.zip，运行Plain Craft Launcher 2.exe
点击上方的下载，在里面找到1.21.1版本，点击它，再点开始安装，等待安装完成
来到启动，选择离线，输入用户名，点击启动游戏
点击多人游戏，再创建一个服务器，服务器地址填：127.0.0.1，点击完成，再加入服务器
7.运行第一个文件
打开python IDLE，依次点击File>open，打开我给你提供pymc_texe.py,按F5运行(有些笔记本电脑要按 Fn +F5)，在切到Minecraft，此时游戏角色旁边会出现一个石头，至此，整个控制就完成了
8.其他
你可以下载我仓库里的.py文件，我以后还会在里面放上更多的python控制文件。
