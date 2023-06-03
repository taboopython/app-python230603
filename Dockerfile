# ベースとなるDockerイメージ指定
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /app

# ホストのファイルを/appにコピー
COPY . /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    tesseract-ocr-jpn

# 必要なpythonパッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# 環境変数を設定
ENV PDF_PATH=/app/data/example.pdf
ENV CSV_PATH=/app/data/output.csv

# コマンド実行
CMD ["python", "./src/main.py"]
