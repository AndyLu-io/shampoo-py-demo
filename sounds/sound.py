from vosk import Model, KaldiRecognizer
import wave
import json


# 加载模型路径
model_path = "/Users/luxiaobo/Desktop/vosk-model-cn-0.22"  # 替换为你下载的中文模型路径

# 检查模型是否存在
import os

if not os.path.exists(model_path):
    print("模型未找到，请先下载中文模型！")
    exit(1)

# 初始化模型
model = Model(model_path)


# 转录音频文件
def transcribe_audio(audio_path):
    # 打开音频文件
    wf = wave.open(audio_path, "rb")

    # 检查音频参数
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
        print("音频必须为单声道、16kHz、16位深度。请先转换格式！")
        exit(1)

    # 初始化识别器
    recognizer = KaldiRecognizer(model, wf.getframerate())

    results = []

    # 逐段识别音频内容
    while True:
        data = wf.readframes(4000)  # 每次读取 4000 帧
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):  # 接受完整识别结果
            result = json.loads(recognizer.Result())
            results.append(result.get("text", ""))

    # 处理最后的部分
    final_result = json.loads(recognizer.FinalResult())
    results.append(final_result.get("text", ""))

    return " ".join(results)


# 自动换行并生成 LaTeX 文件
# 自动换行并生成文本文件
def generate_text_file(text, output_path, line_width=80):
    # 自动换行
    lines = []
    while text:
        lines.append(text[:line_width])
        text = text[line_width:]

    # 写入文件
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"文本文件已生成：{output_path}")


# 调用转录函数
audio_file = "/Users/luxiaobo/Desktop/test.wav"  # 替换为你的音频文件
transcript = transcribe_audio(audio_file)
print("转录结果：", transcript)
tex_file = "../output02.txt"
generate_text_file(transcript, tex_file)
print("完成！")
