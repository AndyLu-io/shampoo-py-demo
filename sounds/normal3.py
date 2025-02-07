from sounds.texOpt import clean_text


def add_punctuation(text):
    """添加标点符号"""
    if not text.endswith("。"):
        text += "。"
    return text

def process_text(text):
    """清理空格并添加标点"""
    cleaned_text = clean_text(text)
    return add_punctuation(cleaned_text)

# 示例
input_text = "大家 好 我 是 安徽省 税务局 税收 经济 分析 出 的 彦硕 爪 今天 要 和 大家 分享 的 主题 是 双 叹 分析 思路 及 分析 案例 解析 今天 的 分享 呢 主要 包括 四 个 方面 分别 是 选题 背景 "
processed_text = process_text(input_text)

print("处理后的文本:", processed_text)
