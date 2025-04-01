import subprocess

def optimize_and_extreme_compress(input_pdf, output_pdf):
    """
    先使用 qpdf 进行流数据压缩，再使用 Ghostscript 极限压缩
    """
    temp_pdf = "temp_qpdf_optimized.pdf"

    # **第一步：qpdf 结构优化**
    subprocess.run([
        "qpdf", "--linearize", "--object-streams=generate",
        "--stream-data=compress",  # 进一步压缩流数据
        input_pdf, temp_pdf
    ], check=True)

    # **第二步：Ghostscript 极限压缩**
    command = [
        "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/screen",
        "-dDownsampleColorImages=true",
        "-dDownsampleGrayImages=true",
        "-dDownsampleMonoImages=true",
        "-dColorImageResolution=50",
        "-dGrayImageResolution=50",
        "-dMonoImageResolution=50",
        "-dJPEGQ=40",
        "-dNOPAUSE", "-dBATCH",
        "-sOutputFile=" + output_pdf, temp_pdf
    ]
    subprocess.run(command, check=True)
    print(f"✅ qpdf 结构优化 + Ghostscript 极限压缩完成！已保存至: {output_pdf}")

# **示例**
input_pdf = "/Users/luxiaobo/Downloads/lowNew.pdf"
output_pdf = "/Users/luxiaobo/Downloads/lowNew70.pdf"
optimize_and_extreme_compress(input_pdf, output_pdf)
g