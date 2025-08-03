# 🧼 CleanPic

**CleanPic** 是一个轻量级的 Python 工具，旨在帮助你**清除图像中的隐写信息、隐私元数据和追踪指纹**，为图像分享、归档或敏感信息发布提供安全保障。

---

## 🛡️ 项目亮点

- ✅ **去除 EXIF 元数据**（拍摄时间、GPS、设备信息等）
- ✅ **移除 Alpha 通道**，防止透明图层藏数据
- ✅ **破坏 LSB、像素隐写结构**（通过重采样）
- ✅ **随机添加轻微有色噪声**，扰乱图像指纹识别与高级隐写
- ✅ 支持单图/文件夹批量处理
- ✅ 支持输出为 JPEG 或 PNG 格式

---

## 📦 安装依赖

```bash
pip install pillow numpy
```
---

## 🚀 使用方式

### ▶ 处理单张图片

```bash
python clean_image.py /path/to/image.jpg
```

### ▶ 批量处理整个文件夹

```bash
python clean_image.py /path/to/folder/
```