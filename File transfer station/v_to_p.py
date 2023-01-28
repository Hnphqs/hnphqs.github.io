print("加载os中...")
import os
print("完成")
print("加载opencv中...")
import cv2
print("完成")

print("加载主函数")
def decode_video(video_path, save_dir, target_num=None):
    '''
    video_path: 待解码的视频
    save_dir: 抽帧图片的保存文件夹
    target_num: 抽帧的数量, 为空则解码全部帧, 默认抽全部帧
    '''
    time=0
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    video = cv2.VideoCapture()
    if not video.open(video_path):
        print("找不到视频或视频已损坏")
        exit(1)
    count = 0
    index = 0
    frames_num = video.get(7)
    # 如果target_num为空就全部抽帧,不为空就抽target_num帧
    if target_num is None:
        step = 1
        print('all frame num is {}, decode all'.format(int(frames_num)))
    else:
        step = int(frames_num/target_num)
        print('all frame num is {}, decode sample num is {}'.format(int(frames_num), int(target_num)),)
    print("开始...")
    while True:
        time+=1
        print("进度:",time,"/",frames_num)
        _, frame = video.read()
        if frame is None:
            break
        if count % step == 0:
            save_path = "{}/{:>04d}.png".format(save_dir, index)
            cv2.imwrite(save_path, frame)
            index += 1
        count += 1
        if index == frames_num and target_num is None:
            # 如果全部抽，抽到所有帧的最后一帧就停止
            break
        elif  index == target_num and target_num is not None: 
            # 如果采样抽，抽到target_num就停止
            break
        else:
            pass
    video.release()
    print("完成...")
    print("文件保存在:",save_dir)
print("完成")

print("运行...","\n"*50)
print("■□□■□■□□■□■■■■")
print("■□□■□■■□■□■□□■")
print("■■■■□■■□■□■■■■")
print("■□□■□■□■■□■□□□")
print("■□□■□■□■■□■□□□")
print("视频抽帧器1.0","\n"*3)

if __name__ == '__main__':
    video_path = input("视频的路径:")
    save_dir_1 = input("保存的路径:")
    num = input("写入抽取的数量或回车(数字，默认全部):")
    if num == '':
        decode_video(video_path, save_dir_1)
    else:
        num=int(num)
        decode_video(video_path, save_dir_1,num)