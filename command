1、ls命令

　　ls是list的缩写，常用命令为ls(显示出当前目录列表)，ls -l（详细显示当前目录列表），ls -lh(人性化的详细显示当前目录列表)，ls -a(显示出当前目录列表，包含隐藏文件)

2、cd 命令

　　cd是change direcory的缩写，常用命令为 cd 目录，cd ..为返回上级目录，cd - 返回上次所在目录

3、pwd命令

　　常用命令为pwd 显示当前所在目录

4、mkdir命令

　　mkdir命令为创建空目录命令，通常用法为mkdir 目录名，mkdir -p 目录名/目录名  可以递归创建多个不存在的目录

5、rm命令

　　rm为删除命令remove，rm 文件，谨慎操作

6、rmdir命令

　　rm为删除命令remove direcory，rm 目录，谨慎操作

7、mv命令

　　mv命令move，移动剪切命令，mv 文件 目录，mv 文件 文件（会覆盖）

8、cp命令

　　cp命令为copy命令，复制文件或目录到别的目录里面,cp 文件/目录 目录/文件

9、touch命令

　　touch命令创建空文件，比如touch xx.txt,touch 目录 文件

10、cat命令

　　cat命令查看当前文件内容，cat fi.txt f2.txt > f3.txt合并文件内容，cat -n 对所有行进行编号

11、nl命令

　　nl命令 为文件加入显示行号，nl 文件名，nl -b a 文件名，将空行也加如行号

12、more 命令

　　more命令 按页显示文件内容，more 文件名,more -2 文件名 每2行显示一页

13、less命令

　　less命令查看文件内容，可以上下翻页，less 文件名

14、head命令

　　head命令可以查看文件前几行内容，head -n 2 文件名

15、tail命令

　　tail命令可以查看文件后几行内容，tail -n 2 文件名

16、which命令

　　which 可以执行文件名称，显示路径

17、whereis命令

　　whereis -m svn 查出说明文档路径，whereis -s svn 找source源文件。

18、locate命令

　　locate /etc/m 搜索ect目录下所有m开头的文件

19、find 命令

　　find . -name "*.log"根据关键字查找

20、find exec命令

　　ls -l命令放在find命令的-exec选项中 find . -type f -exec ls -l {} \;

21、find xargs命令

　　find . -type f -print | xargs file查找系统中的每一个普通文件，然后使用xargs命令来测试它们分别属于哪类文件

22、ls -lih命令

　　详细的文件属性

23、zmodem

SecureCRT可以使用linux下的zmodem协议来快速的传送文件,使用非常方便.具体步骤：

