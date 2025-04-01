import fitz


def compress_pdf(input_path, output_path):
    # 打开PDF
    pdf_document = fitz.open(input_path)

    # **执行垃圾回收和优化**
    pdf_document.save(output_path, garbage=4, deflate=True)

    print(f"压缩完成，压缩后的PDF已保存到: {output_path}")


# 使用示例
input_pdf = "/Users/luxiaobo/Downloads/lowNew.pdf"  # 替换为你的输入PDF文件路径
output_pdf = "/Users/luxiaobo/Downloads/lowNew.pdf"  # 替换为你的输出压缩后的PDF文件路径

compress_pdf(input_pdf, output_pdf)
