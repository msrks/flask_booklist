## 書籍購入リスト管理アプリ

[![CircleCI](https://circleci.com/gh/msrks/circle_ci_test.svg?style=svg)](https://circleci.com/gh/msrks/circle_ci_test)

初回はデータベースを新規に作成

```
$ python
>>> from app import db
>>> db.create_all()
```

アプリの起動は以下のコマンドを叩いて、http://localhost:5000にアクセス

```bash
$ python app.py
```
