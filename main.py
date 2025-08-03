import os
import sys
import numpy as np
from PIL import Image

def add_color_noise(img: Image.Image, intensity=5):
    """
    向RGB图像添加轻微有色噪声
    :param img: PIL Image (RGB)
    :param intensity: 噪声强度 (推荐 3~10)
    :return: 带噪图像
    """
    arr = np.array(img).astype(np.int16)
    noise = np.random.randint(-intensity, intensity + 1, arr.shape)
    noisy_arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_arr)


def clean_image(input_path, output_format='JPEG', quality=85, noise_intensity=5):
    """
    清理隐写图像：
    - 去除 EXIF
    - 移除 Alpha 通道
    - 重采样放缩像素
    - 添加轻微噪声
    - 重编码输出
    """
    print(f"📷 处理图像: {input_path}")
    img = Image.open(input_path).convert("RGB")

    # 重采样（放大缩小）
    resized = img.resize((img.width * 2, img.height * 2), Image.BICUBIC)
    resized = resized.resize(img.size, Image.BICUBIC)

    # 添加噪声扰动
    noised = add_color_noise(resized, intensity=noise_intensity)

    # 输出路径
    dirname, filename = os.path.split(input_path)
    name, ext = os.path.splitext(filename)
    clean_name = f"cleaned_{name}.{output_format.lower()}"
    output_path = os.path.join(dirname, clean_name)

    # 保存
    if output_format.upper() == 'JPEG':
        noised.save(output_path, format='JPEG', quality=quality, optimize=True)
    else:
        noised.save(output_path, format='PNG')

    print(f"✅ 已保存: {output_path}\n")


def batch_clean(folder_path, output_format='JPEG', quality=85, noise_intensity=5):
    supported_exts = ('.jpg', '.jpeg', '.png', '.bmp')
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_exts)]

    if not files:
        print("⚠️ 该文件夹中未找到支持的图片文件。")
        return

    for file in files:
        full_path = os.path.join(folder_path, file)
        try:
            clean_image(full_path, output_format, quality, noise_intensity)
        except Exception as e:
            print(f"❌ 处理失败: {file}, 错误: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python clean_image.py <文件路径或文件夹路径>")
    else:
        path = sys.argv[1]
        if os.path.isfile(path):
            clean_image(path)
        elif os.path.isdir(path):
            batch_clean(path)
        else:
            print("❌ 路径无效，请确认输入的是图片或文件夹路径。")
