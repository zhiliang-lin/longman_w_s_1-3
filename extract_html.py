from bs4 import BeautifulSoup

input_file = r"D:\work\github\longman_w_s_1-3\longman_words_s_w.html"
output_file = r"D:\work\github\longman_w_s_1-3\index.html"

# 1. 读取 HTML
with open(input_file, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# 2. 准备新文件的头部 (保留手机端自适应)
new_html = """<!DOCTYPE html><html><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style> body { padding: 15px; font-family: sans-serif; } .entry { border-bottom: 1px solid #ccc; padding: 15px 0; } </style>
</head><body>"""

# 3. 核心提取逻辑：找到所有表格行
for row in soup.find_all("tr"):
    cells = row.find_all("td") # 只查找包含数据的 td，自动过滤掉由 th 组成的表头
    
    # 确保这一行确实有至少 5 列数据
    if len(cells) >= 5:
        # 获取第 5 列 (索引 4) 的所有内部 HTML，转成字符串并合并
        explanation_html = "".join(str(content) for content in cells[4].contents)
        
        # 将提取出的这块精美排版，用 div 包裹起来塞进新网页
        if explanation_html.strip():
            new_html += f'\n<div class="entry">\n{explanation_html}\n</div>\n'

new_html += "</body></html>"

# 4. 保存为新文件
with open(output_file, "w", encoding="utf-8") as f:
    f.write(new_html)