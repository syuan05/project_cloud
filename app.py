import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, GitHub!"

if __name__ == "__main__":
    # 使用 Render 提供的 PORT 環境變數
    port = int(os.environ.get("PORT", 5000))  # 預設端口是 5000，如果沒有環境變數
    app.run(host="0.0.0.0", port=port)
