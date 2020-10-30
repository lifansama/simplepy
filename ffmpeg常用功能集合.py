import os
def main():
    infile=input('输入文件路径：\n')
    print('1、转换视频\n2、转换音频\n3、从视频分离完整音频\n4、从视频截取某时刻图片\n5、截取某段视频\n6、从视频制作gif\n7、从视频截取音频\n8、从音频截取音频\n')
    i=int(input('输入分类对应的数字：\n'))
    if i==1 or i==2:
        outfile=input('输入名字（包含后缀名，可带路径）：\n')
        cmd='ffmpeg -i "%s" "%s"'%(infile,outfile)
        print(cmd)
        os.system(cmd)
    elif i==3:
        outfile=input('输入名字（包含后缀名，可带路径）：\n')
        cmd='ffmpeg -i "%s" -vn "%s"'%(infile,outfile)
        os.system(cmd)
    elif i==4:
        st=input('输入开始时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：\n')
        outfile=input('输入名字（包含后缀名，可带路径）：\n')
        cmd='ffmpeg -i "%s" -ss %s -frames 1 "%s"'%(infile,st,outfile)
        os.system(cmd)
    elif i==5 or i==6 or i==7 or i==8:
        st=input('输入开始时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：\n')
        et=input('输入结束时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：\n')
        outfile=input('输入名字（包含后缀名，可带路径）：\n')
        cmd='ffmpeg -ss %s -to %s -i "%s" "%s"'%(st,et,infile,outfile)
        os.system(cmd)
    else:
        print('请输入对应数字！')
main()
while True:
    i=input('是否继续？q：退出，其它：继续\n')
    if i=='q':
        break
    else:
        main()