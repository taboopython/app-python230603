import csv
import os
import re
import pytesseract
from pdf2image import convert_from_path

# ファイルのパスを環境変数から取得
pdf_path = os.getenv('PDF_PATH', 'example.pdf')
csv_path = os.getenv('CSV_PATH', 'output.csv')

# PDFを画像に変換
images = convert_from_path(pdf_path)

# 画像からテキストを抽出
texts = []
for i in range(len(images)):
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    config = '--psm 6 -l jpn'
    texts.append(pytesseract.image_to_string(images[i], config=config))

# テキストを解析
lines = []
for text in texts:
    lines.extend(text.split('\n'))

# CSVファイルに書き込む
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in lines:
        writer.writerow([line])