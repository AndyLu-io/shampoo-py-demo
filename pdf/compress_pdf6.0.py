import subprocess

def extreme_compress_pdf(input_pdf, output_pdf):
    """
    使用 Ghostscript 进行极限压缩，手动调整图片降采样和 JPEG 压缩参数
    """
    command = [
        "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/screen",  # 最大压缩
        "-dDownsampleColorImages=true",  # 强制降采样
        "-dDownsampleGrayImages=true",
        "-dDownsampleMonoImages=true",
        "-dColorImageResolution=50",  # 颜色图片降低到 50 DPI
        "-dGrayImageResolution=50",  # 灰度图片降低到 50 DPI
        "-dMonoImageResolution=50",  # 黑白图片降低到 50 DPI
        "-dJPEGQ=40",  # 强制降低 JPEG 质量
        "-dNOPAUSE", "-dBATCH",
        "-sOutputFile=" + output_pdf, input_pdf
    ]
    subprocess.run(command, check=True)
    print(f"✅ 极限压缩完成！已保存至: {output_pdf}")

# **示例**
input_pdf = "/Users/luxiaobo/Downloads/lowNew.pdf"
output_pdf = "/Users/luxiaobo/Downloads/lowNew61.pdf"
extreme_compress_pdf(input_pdf, output_pdf)
