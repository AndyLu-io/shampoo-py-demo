import language_tool_python


def correct_spelling(text):
    # 创建一个语言工具实例，设置语言为中文（简体）
    tool = language_tool_python.LanguageTool('zh-CN')

    # 检查文本并获取错误和建议
    matches = tool.check(text)

    # 使用修正建议生成新的文本
    corrected_text = language_tool_python.utils.correct(text, matches)

    return corrected_text


# 测试
text = "对 生产 工作 的 具体 要求 进行 梳理 大家 可以 通过 这 张 PPT 看到 自从 习 总书记 在 二 零 二 零 年 九月 第一 次 公开 提出 双"
corrected_text = correct_spelling(text)
print("修改后的文本:", corrected_text)
