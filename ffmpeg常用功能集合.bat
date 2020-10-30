@echo off
:main
set /p a=输入文件路径：
echo 1、转换
echo 2、从视频截取某时刻图片
echo 3、截取
set /p i=输入分类对应的数字：
if %i%==1 goto main1
if %i%==2 goto main2
if %i%==3 goto main3
:main1
set /p b=输入名字（包含后缀名，可带路径）：
ffmpeg -i "%a%" "%b%"
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit
:main2
set /p b=输入时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：
set /p c=输入名字（包含后缀名，可带路径）：
ffmpeg -i "%a%" -ss %b% -frames 1 "%c%"
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit
:main3
set /p b=输入开始时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：
set /p c=输入结束时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：
set /p d=输入名字（包含后缀名，可带路径）：
ffmpeg -ss %b% -to %c% -i "%a%" "%d%"
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit