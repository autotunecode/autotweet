# X自動投稿ボット

時間帯に応じて自動的に挨拶のツイートを投稿するボットです。

## 機能

- 時間帯に応じて以下の挨拶を投稿
  - 5:00-11:59 「おはよう」
  - 12:00-17:59 「こんにちは」 
  - 18:00-4:59 「こんばんは」

## セットアップ

1. 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```
    
2. .envファイルの作成

3. .envファイルにX APIキー、APIシークレットキー、アクセストークン、アクセストークンシークレットを設定
```
X_API_KEY="あなたのAPIキー"
X_API_SECRET_KEY="あなたのAPIシークレットキー"
X_ACCESS_TOKEN="あなたのアクセストークン"
X_ACCESS_TOKEN_SECRET="あなたのアクセストークンシークレット"
```


