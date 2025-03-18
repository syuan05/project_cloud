from flask import Flask, request, abort
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        try:
            payload = request.get_json()  # 解析 POST 請求的 JSON 資料
            print(payload)  # 在終端機顯示收到的資料
            return 'OK', 200  # 回應 LINE 伺服器，表示請求成功
        except Exception as e:
            print(f"Error: {e}")
            abort(400)  # 如果有錯誤，回應 400 Bad Request

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))  # 根據環境變數選擇 PORT
    app.run(host="0.0.0.0", port=port)  # 啟動 Flask 伺服器
