import requests
from bs4 import BeautifulSoup
import json

# 目标网页的URL
url_list = [
    "https://www.gov.cn/gongbao/content/2018/content_5280588.htm",
    "https://www.gov.cn/flfg/2011-02/23/content_1808854.htm",
    "https://www.gov.cn/zhengce/zhengceku/2020-12/31/content_5575675.htm"
]

def get_data(url):
    response = requests.get(url)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        title = soup.find('title').get_text()
        non_empty_paragraphs = [p.get_text().strip() for p in paragraphs if p.get_text().strip()]
        paragraph_text = "\n".join(non_empty_paragraphs)
        paragraph_text = paragraph_text.replace('\u3000', '').strip() # 清除全角空格
        return title, paragraph_text
    else:
        print(f"网页请求失败，状态码: {response.status_code}")
        return None, None

# # 写入到 jsonl 文件
# with open("mycode/data/nianjin.jsonl", "w", encoding="utf-8") as f:
#     for idx, url in enumerate(url_list):
#         title, paragraph_text = get_data(url)
#         if title is not None:
#             res = {
#                 "paragraph_id": idx,
#                 "title": title,
#                 "paragraph_text": paragraph_text
#             }
#             f.write(json.dumps(res, ensure_ascii=False) + "\n")  # 写入一行

# 写入为多个 .txt 文件
for idx, url in enumerate(url_list):
    _, paragraph_text = get_data(url)
    if paragraph_text:
        with open(f"mycode/data/nianjin_{idx+1}.txt", "w", encoding="utf-8") as f:
            f.write(paragraph_text)