import csv
import pytesseract
from pdf2image import convert_from_path
import os
import re

# ファイルのパスを環境変数から取得
pdf_path = os.getenv('PDF_PATH', 'example.pdf')
csv_path = os.getenv('CSV_PATH', 'output.csv')

# PDFを画像に変換
images = convert_from_path(pdf_path)

# 画像からテキストを抽出
texts = []
for i in range(len(images)):
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    texts.append(pytesseract.image_to_string(images[i], lang='jpn+eng'))

# テキストを解析
lines = []
for text in texts:
    lines.extend(text.split('\n'))

# 数字を抽出
for i in range(len(lines)):
    numbers = re.findall(r'\d+', lines[i])
    lines[i] = ' '.join(numbers)

# CSVファイルに書き込む
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in lines:
        writer.writerow([line])