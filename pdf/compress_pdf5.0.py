import subprocess


def optimize_and_compress_pdf(input_pdf, output_pdf, quality="screen"):
    """
    先使用 qpdf 优化 PDF 结构，再使用 Ghostscript 进行最大化压缩
    """
    temp_pdf = "temp_optimized.pdf"

    # **第一步：qpdf 结构优化**
    subprocess.run(["qpdf", "--linearize", "--object-streams=generate", input_pdf, temp_pdf], check=True)

    # **第二步：Ghostscript 高压缩**
    command = [
        "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS=/screen", "-dNOPAUSE", "-dBATCH",
        "-sOutputFile=" + output_pdf, temp_pdf
    ]
    subprocess.run(command, check=True)

    print(f"✅ PDF 结构优化 + 高压缩完成！已保存至: {output_pdf}")


# **示例**
input_pdf = "/Users/luxiaobo/Downloads/lowNew.pdf"  # 替换为你的输入PDF文件路径
output_pdf = "/Users/luxiaobo/Downloads/lowNew50.pdf"  # 替换为你的输出压缩后的PDF文件路径
optimize_and_compress_pdf(input_pdf, output_pdf, quality="screen")  # 最大压缩
