# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import re
from PIL import Image, ImageDraw


def process_pic(pic_file, xys):
    im = Image.open(pic_file)
    draw = ImageDraw.Draw(im)
    last_point = None
    # lines
    for xy in xys:
        point = [int(xy[1]), int(xy[2])]
        if last_point is not None:
            draw.line((last_point[0],last_point[1], point[0],point[1]), fill=(0, 255, 0))
        last_point = point
    # points
    for xy in xys:
        point = [int(xy[1]), int(xy[2])]
        draw.point(point, fill=(255, 0, 0))
    del draw
    im.save("out.png")

def process_log(log_file, stop_keyword):
    f = open(log_file, encoding='utf-8', errors='ignore')
    lines = f.read()
    f.close()
    interest_lines = lines.split(stop_keyword)[0]
    re_xy = re.compile(r"(\d): \((\d+)\.\d, (\d+)\.\d\)")
    xys = re_xy.findall(interest_lines)

    for xy in xys:
        print('坐标：', xy)
    return xys


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    log_file = 'log.txt'
    screen_png = 'Screenshot.png'
    if not os.path.exists(log_file):
        input('请将log文件改名为 log.txt')
        exit(-1)
    if not os.path.exists(log_file):
        print('请将截图改名为 Screenshot')
        exit(-1)
    stop_keyword = 'ContactsProvider: Locale has changed from'
    print('截止到 ', stop_keyword)
    xys = process_log(log_file, stop_keyword)
    process_pic(screen_png, xys)
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
