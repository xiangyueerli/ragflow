import json
import sys
sys.path.append("/Users/ycy/PycharmProjects/hw/ragflow/mycode/")

# 输入 jsonl 文件路径
input_path = 'test.jsonl'
# 输出 json 文件路径
output_path = 'output.json'

# 逐行读取 JSONL 文件，并解析为 JSON 对象列表
with open(input_path, 'r', encoding='utf-8') as f:
    data = [json.loads(line) for line in f if line.strip()]

# 写入 JSON 文件为数组格式
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
