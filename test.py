# 必要なライブラリのインポート
import os  # 環境変数へのアクセスに使用
import tweepy  # X API操作用のライブラリ
from datetime import datetime  # 日時操作用
import pytz  # タイムゾーン処理用
import functions_framework  # GCP Cloud Functions用のフレームワーク

# GCPの変更点1: 環境変数の読み込み方法
# - dotenvによる.envファイルの読み込みを削除
# - os.environを直接使用してGCPの環境変数にアクセス
def init_client():
    """X APIクライアントの初期化"""
    client = tweepy.Client(
        consumer_key=os.environ.get("X_API_KEY"),
        consumer_secret=os.environ.get("X_API_SECRET_KEY"),
        access_token=os.environ.get("X_ACCESS_TOKEN"), 
        access_token_secret=os.environ.get("X_ACCESS_TOKEN_SECRET")
    )
    return client

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

# GCPの変更点2: Cloud Functions用のエントリーポイント
# - @functions_framework.httpデコレータを追加してHTTPトリガーを設定
# - requestパラメータを受け取る形式に変更
# - レスポンスをCloud Functions形式のディクショナリに変更
@functions_framework.http
def post_greeting(request):
    """Cloud Functions用のエントリーポイント"""
    try:
        # クライアントの初期化
        client = init_client()
        
        # 挨拶の投稿
        greeting = get_greeting()
        client.create_tweet(text=greeting)
        
        return {
            'statusCode': 200,
            'body': f'投稿完了: {greeting}'
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'エラーが発生しました: {str(e)}'
        }