import fitz
from PIL import Image
import io

def compress_pdf_images(input_pdf, output_pdf, image_quality=75, dpi=150):
    """
    使用智能图片压缩来优化 PDF 文件大小
    :param input_pdf: 原始 PDF 文件路径
    :param output_pdf: 压缩后输出 PDF 文件路径
    :param image_quality: 图片质量 (1-100)，推荐 70-80 之间
    :param dpi: 重新采样的 DPI，150 DPI 对阅读足够
    """
    doc = fitz.open(input_pdf)  # 打开 PDF
    for page in doc:  # 遍历所有页面
        img_list = page.get_images(full=True)  # 获取所有图片信息
        for img in img_list:
            xref = img[0]  # 获取图片 XREF
            base_image = doc.extract_image(xref)  # 提取图片数据
            img_bytes = base_image["image"]  # 获取原始图片数据
            img_ext = base_image["ext"].lower()  # 图片格式（jpg/png等）

            # **加载图片**
            image = Image.open(io.BytesIO(img_bytes))

            # **调整分辨率**
            image = image.convert("RGB")  # 确保无透明通道
            new_width = int(image.width * (dpi / image.info.get("dpi", (300, 300))[0]))
            new_height = int(image.height * (dpi / image.info.get("dpi", (300, 300))[1]))
            image = image.resize((new_width, new_height), Image.LANCZOS)

            # **针对不同格式选择压缩方式**
            img_buffer = io.BytesIO()
            if img_ext in ["jpeg", "jpg"]:
                image.save(img_buffer, format="JPEG", quality=image_quality, optimize=True)
            else:
                image.save(img_buffer, format="WEBP", quality=image_quality, optimize=True)

            new_img_bytes = img_buffer.getvalue()

            # **更新 PDF**
            doc.update_stream(xref, new_img_bytes)

    # **优化 & 保存**
    doc.save(output_pdf, garbage=4, deflate=True)
    doc.close()
    print(f"✅ 压缩完成！新 PDF 大小优化，已保存至: {output_pdf}")

# **使用示例**
input_pdf = "/Users/luxiaobo/Downloads/low.pdf"  # 替换为你的输入PDF文件路径
output_pdf = "/Users/luxiaobo/Downloads/low300.pdf"  # 替换为你的输出压缩后的PDF文件路径
compress_pdf_images(input_pdf, output_pdf)
