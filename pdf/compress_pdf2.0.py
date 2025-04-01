import fitz
from PIL import Image
import io
import os


def compress_pdf_images(input_pdf, output_pdf, image_quality=80):
    """
    使用 WebP 重新编码 PDF 内的图片，压缩 PDF 文件大小
    :param input_pdf: 原始 PDF 文件路径
    :param output_pdf: 压缩后输出的 PDF 文件路径
    :param image_quality: 图片质量 (1-100)，推荐 70-90 之间
    """
    doc = fitz.open(input_pdf)  # 打开 PDF
    for page in doc:  # 遍历每一页
        img_list = page.get_images(full=True)  # 获取页面中的所有图片信息
        for img in img_list:
            xref = img[0]  # 获取图片的 XREF
            base_image = doc.extract_image(xref)  # 提取图片数据
            img_bytes = base_image["image"]  # 获取原始图片数据
            img_ext = base_image["ext"]  # 图片格式（jpg/png等）

            # **使用 PIL 重新编码图片**
            image = Image.open(io.BytesIO(img_bytes))

            # **转换为 WebP（比 JPG 压缩率更高）**
            img_buffer = io.BytesIO()
            image.save(img_buffer, format="WEBP", quality=image_quality, optimize=True)
            new_img_bytes = img_buffer.getvalue()

            # **使用 update_stream() 替换原始图片数据**
            doc.update_stream(xref, new_img_bytes)

    # **保存压缩后的 PDF**
    doc.save(output_pdf)
    doc.close()
    print(f"✅ PDF 压缩完成！已保存至: {output_pdf}")


# 使用示例
input_pdf = "/Users/luxiaobo/Downloads/lowNew.pdf"  # 替换为你的输入PDF文件路径
output_pdf = "/Users/luxiaobo/Downloads/lowNew212.pdf"  # 替换为你的输出压缩后的PDF文件路径
compress_pdf_images(input_pdf, output_pdf)
