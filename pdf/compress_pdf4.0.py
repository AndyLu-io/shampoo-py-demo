import subprocess

def compress_pdf_ghostscript(input_pdf, output_pdf):
    """
    使用 Ghostscript 进行高质量 PDF 压缩，减少文件大小但尽量保持图片清晰度
    """
    command = [
        "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",  # 可选：/screen, /ebook, /printer, /prepress
        "-dNOPAUSE", "-dBATCH", "-sOutputFile=" + output_pdf, input_pdf
    ]
    subprocess.run(command, check=True)
    print(f"✅ PDF 高质量压缩完成！已保存至: {output_pdf}")

# **示例**
input_pdf = "/Users/luxiaobo/Downloads/lowNew.pdf"  # 替换为你的输入PDF文件路径
output_pdf = "/Users/luxiaobo/Downloads/lowNew42.pdf"  # 替换为你的输出压缩后的PDF文件路径
compress_pdf_ghostscript(input_pdf, output_pdf)
