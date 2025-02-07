import re
import language_tool_python

# Step 1: 从文本文件读取内容
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# Step 2: 去除多余的空格
def clean_text(text):
    # 去除文本中多个连续的空格为一个
    text = text.replace(" ", "")
    text = re.sub(r'\s+', ' ', text).strip()
    # 删除标点符号前后的空格
    text = re.sub(r'\s([，。！？])', r'\1', text)  # 确保标点符号前没有空格
    text = re.sub(r'([，。！？])\s', r'\1', text)  # 确保标点符号后没有空格
    return text


# Step 3: 错别字修正（可以省略不使用，如果已经有LanguageTool进行了修正）
def correct_spelling(text):
    tool = language_tool_python.LanguageTool('zh-CN')
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text


# Step 4: 语法和上下文优化
def correct_grammar(text):
    tool = language_tool_python.LanguageTool('zh-CN')  # 使用中文语法检查
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text


# Step 5: 自动添加适当的标点和换行符
def add_punctuation_and_format(text):
    # 在每个句子结束后的标点符号（如句号、感叹号、问号）后加换行符
    text = re.sub(r'([。！？])', r'\1\n', text)  # 在句号、问号、感叹号后加换行符

    # 在逗号后也加入换行符（如果需要的话，可以调整或删除此规则）
    text = re.sub(r'([，])', r'\1\n', text)

    return text


# Step 6: 将优化后的文本写入文件
def write_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


# 主程序逻辑
def process_text_file(input_file, output_file):
    # Step 1: 从文件中读取文本
    input_text = read_file(input_file)

    # Step 2: 去除多余空格
    text_no_spaces = clean_text(input_text)

    # Step 3: 拼写检查
    text_corrected = correct_spelling(text_no_spaces)

    # Step 4: 语法和上下文优化
    final_text = correct_grammar(text_corrected)

    # Step 5: 自动添加标点符号和换行符
    final_text_with_punctuation = add_punctuation_and_format(final_text)

    # 最后再一次去除多余空格，确保文本清晰
    final_text_cleaned = clean_text(final_text_with_punctuation)

    # Step 6: 将优化后的文本写入输出文件
    write_to_file(output_file, final_text_cleaned)
    print(f"优化后的文本已保存到 {output_file}")


# 输入文件路径和输出文件路径
input_file = '/Users/luxiaobo/PycharmProjects/shampoo-py-demo/output02.txt'  # 输入文件（包含原始文本）
output_file = 'sounds-opt2.txt'  # 输出文件（优化后的文本）

# 调用主程序进行文本处理
process_text_file(input_file, output_file)
