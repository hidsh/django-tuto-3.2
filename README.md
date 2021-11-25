# django-tuto-3.2

- [はじめての Django アプリ作成(公式チュートリアル)](https://docs.djangoproject.com/ja/3.2/intro/tutorial01/)
- [Django公式サイトのチュートリアルを咀嚼しながらやってみる](https://www.icoro.com/2021052511846/2)

## memo

### venv お約束
```
❯❯❯ mkdir tuto
❯❯❯ cd tuto
❯❯❯ python -m venv venv
❯❯❯ . venv/bin/activate
(venv) ❯❯❯ python -m pip install --upgrade pip
```

### djanogo インストール
```
(venv) ❯❯❯ python -m pip install Django
(venv) ❯❯❯ python -m django --version
3.2.8
```

### プロジェクト/アプリ作成
```
django-admin startproject mysite <-- プロジェクト作成
cd mysite                        <-- プロジェクトトップに移動(以後のコマンドは基本ここで実行)
python manage.py startapp polls  <-- アプリ作成
```

### 開発用サーバ起動
```
python manage.py runserver
```

### アプリのビューを追加
|ファイル|内容|メモ|
|---|---|---|
| polls/views.py | pollsアプリのビュー | リクエストハンドラ関数を書く|
| polls/urls.py  | pollsアプリ内のroute定義 | リクエストハンドラを追加したらこっちにも追加 |
| mysite/urls.py | プロジェクト内のroute定義| polls/url.py をimportする |

### 
```
```


## environment

### local (macbook pro)
- python 3.9.7
- pip 21.3.1
- django 3.2.8 

### heroku
- 


