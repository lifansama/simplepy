@echo off
:main
set /p a=�����ļ�·����
echo 1��ת��
echo 2������Ƶ��ȡĳʱ��ͼƬ
echo 3����ȡ
set /p i=��������Ӧ�����֣�
if %i%==1 goto main1
if %i%==2 goto main2
if %i%==3 goto main3
:main1
set /p b=�������֣�������׺�����ɴ�·������
ffmpeg -i "%a%" "%b%"
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit
:main2
set /p b=����ʱ�̣���ʽΪʱ:��:�루�����������λ������00:06:06����
set /p c=�������֣�������׺�����ɴ�·������
ffmpeg -i "%a%" -ss %b% -frames 1 "%c%"
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit
:main3
set /p b=���뿪ʼʱ�̣���ʽΪʱ:��:�루�����������λ������00:06:06����
set /p c=�������ʱ�̣���ʽΪʱ:��:�루�����������λ������00:06:06����
set /p d=�������֣�������׺�����ɴ�·������
ffmpeg -ss %b% -to %c% -i "%a%" "%d%"
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit