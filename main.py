import os
import tweepy
from datetime import datetime
import pytz
from dotenv import load_dotenv

load_dotenv()

# X API認証情報の取得
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET_KEY = os.getenv("X_API_SECRET_KEY") 
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

# デバッグ用のprint文を追加
print("API認証情報:")
print(f"API Key: {'*' * len(X_API_KEY)}")
print(f"API Secret: {'*' * len(X_API_SECRET_KEY)}")
print(f"Access Token: {'*' * len(X_ACCESS_TOKEN)}")
print(f"Access Token Secret: {'*' * len(X_ACCESS_TOKEN_SECRET)}")

# クライアントの初期化を確認
try:
    client = tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET_KEY,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET
    )
    
    # クライアントの認証確認
    me = client.get_me()
    print(f"認証成功: @{me.data.username}")
    
except tweepy.errors.Unauthorized:
    print("認証エラー: APIキーとトークンを確認してください")
    print("以下を確認してください:")
    print("1. .envファイルに正しいAPIキーとトークンが設定されているか")
    print("2. APIキーに書き込み権限があるか")
    print("3. APIキーが有効か")
    raise

def get_greeting():
    """現在時刻に応じた挨拶を返す"""
    # 日本時間を取得
    jst = pytz.timezone('Asia/Tokyo')
    now = datetime.now(jst)
    hour = now.hour
    
    if 5 <= hour < 12:
        return "おはよう"
    elif 12 <= hour < 18:
        return "こんにちは"
    else:
        return "こんばんは"

def post_greeting():
    """挨拶をXに投稿"""
    try:
        greeting = get_greeting()
        client.create_tweet(text=greeting)
        print(f"投稿完了: {greeting}")
    except Exception as e:
        print(f"投稿エラー: {str(e)}")

if __name__ == "__main__":
    post_greeting()