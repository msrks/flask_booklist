## このreposをForkしてからのワークフロー

まず forkして、forkしたreposをcloneする。

```
$ git clone <forked-repos>
```

### 最新バージョンへの追従

fork元reposを remoteに追加しておく

```
$ git remote add upstream <msrks-repos>
```

定期的に最新バージョンを取り込む

```
#もしブランチで作業していたら masterに戻る
$ git checkout master

#最新バージョン取り込み
$ git fetch upstream
$ git merge upstream/master

#自分のgithubに反映
$ git push origin master
```

### 開発ブランチで作業する

開発ブランチを作る

```
$ cd socket-app
$ git checkout -b <branch-name>
```

ブランチ上で開発し、コミットする

````
$ touch hogehoge.txt
$ git add -A
$ git commit -m "hogehoge"
````

masterにマージする

```
$ git checkout master
$ git merge <branch-name>
```

ブランチをgithubにpushする

```
$ git checkout <branch-name>
$ git push origin <branch-name>
```

開発が終了して完全にmergeされたブランチを削除する

```
#ローカルブランチの削除
$ git branch -d <branch-name> 

#リモートブランチの削除
$ git push --delete origin <branch-name>
```