# PythonBasicB

## ファイルの取り扱い
```
//ファイルを開いて中身を読み取る
with open ("sample.txt","r",encoding="utf-8") as file:
    data = file.read()
    print(data)
```
| mode | 説明 | 例 |
| ---------------- | ---------------- | ---------------- |
| r | 読み込み |  |
| w | 書き込み(新規作成) |  |
| a | 追記 |  |
| r+ | 読み書き |　 | 
| w+ | 読み書き(新規作成) |　 | 
| a+ | 追記・読み書き |　 | 
| t | テキストモード |　 | 
| b | バイナリモード |　画像など | 

```
//ファイルを新規作成して、文字列を書き込んで保存
with open ("data.txt", "w", encoding="utf-8") as file:
    file.write("Python\n") #\nは改行を意味します
    file.write("保存")
```
- with 文を使用しない場合はclose()メソッドでファイルを閉じる必要があります。

## ディレクトリからファイルを取得する
globライブラリを使用する場合
```
import glob

files = glob.glob("./sample_dir/*")
print(files)
for file in files:
    print(file)
```

osライブラリを使用する場合
```
import os 

files = os.listdir("./sample_dir")
print(files)
for file in files:
    print(file)
```

練習問題：ファイルに保存する機能を使って、アプリケーションを永続化する

## クラスとオブジェクト

クラスはオブジェクトの設計図であり、保持するデータ(変数)と振る舞い(関数・メソッド)をひとまとめにしたもの。  
```
# クラス定義
class Ticket:
    event_name = "肥後橋夏フェス"
    sheet_no = "A200"
    price = 5000

    def show_detail(self):
        return f"公演名:{self.event_name} 座席番号:{self.sheet_no} チェット代金:{self.price}"
    
# 変数tiにクラス設計図から生成したオブジェクトを代入(インスタンス化)
ti = Ticket()
# インスタンスのメソッドを実行
print(ti.show_detail())
```

### コンストラクター
クラスをインスタンス化する時にだけ自動的に実行されるメソッドをコンストラクタという。  
逆にインスタンスが消滅するときにだけ自動的に実行されるメソッドをデストラクタという。 
```
class Ticket:
    # コンストラクタ
    def __init__(self, event_name,sheet_no,price):
        self.event_name = event_name
        self.sheet_no = sheet_no
        self.price = price

    def show_detail(self):
        return f"公演名:{self.event_name} 座席番号:{self.sheet_no} チェット代金:{self.price}"
```

### 継承
クラス(オブジェクトの設計図)からその属性を受け継ぎ、派生したオブジェクト作るとこを継承という。  
```
# Ticketを継承してVipTicket(招待チケット)を作る
class VipTicket(Ticket):
    # コンストラクタ
    def __init__(self, event_name,sheet_no):
        self.event_name = event_name
        self.sheet_no = sheet_no
        self.price = 0

vti = VipTicket("肥後橋夏フェス","Z001")
# Ticketを継承しているため、show_detailメソッドはVipTicketクラスに定義しなくても備えている
print(vti.show_detail())
```
### メソッドのオーバーライド
```
class VipTicket(Ticket):
    # コンストラクタ
    def __init__(self, event_name,sheet_no):
        self.event_name = event_name
        self.sheet_no = sheet_no
        self.price = 0
    # メソッドを上書き(オーバーライド)
    def show_detail(self):
        return f"公演名:{self.event_name} 座席番号:{self.sheet_no} チェット代金:招待"
# 継承クラスのインスタンス化
vti = VipTicket("肥後橋夏フェス","Z001")
# 継承クラスのメソッド実行
print(vti.show_detail())
# 親クラスのメソッド実行
print(super(VipTicket,vti).show_detail())
```

## アルゴリズム
調理に置き換えると....
文法は「食材を切断する道具を包丁という」や「包丁の握り方」など調理道具の名称や使い方です。  
アルゴリズムは「出汁の取り方」「肉じゃがの作り方」などレシピに該当します。  
また「肉じゃがの作り方」が調理者や材料により複数存在するように同じ目的のアルゴリズムも複数存在します。  

## 基本のアルゴリズム
例：1からnまで足し合わせる
```
# ひたすら足すアルゴリズム(簡単だけど100とか1000になると大変)
total = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10

# 繰返しを利用するアルゴリズム
n = 10
total = 0
for i in range(1,n+1):
    total += i
```
別の解釈をすると  
1 + 10 = 11  
2 + 9 = 11
3 + 8 = 11
一番先頭と一番最後の数
二番目と後ろから二番目の数
三番目と後ろから三番目の数
を加えてもすべて11となります。

```
# 繰返しを使わず、計算で求めるアルゴリズム
total = (1 + n) * n / 2
```
と複数の計算方法があります。
この計算方法がアルゴリズムです。

料理のレシピも複数ありますが、正しいかどうかは目的で異なります。
- 調理時間を短くしたい
- 材料費、光熱費を安くしたい
- 味を最優先

プログラムのアルゴリズムも目的で正解は異なります。
- 計算が早く終わる
- 修正が容易

## 素数を求める
素数とは1とその数以外に約数を持たない2以上の自然数です。  
2,5,7,11,13...と無数に存在します。  
素数の求め方にも複数の方法(アルゴリズム)があります。  
プログラム初心者向けに繰返しと条件分岐を使って求める方法を学びます。  
2 から 100 までの自然数nを 2 から n/2 まで順番に割って割り切れなければ素数と判断します。n/2までとするのは n/2より大きな数では割れないからです。  
例) 50 は 25より大きな数字では割れません。  

## n!と再帰関数
nの階乗(1 x 2 x 3 x 4 x 5 .... x n)をn!と表します。
n! の計算方法(アルゴリズム)には繰返しを使う方法と再起関数を使うほうがあります。  
```
# 繰返しを使う方法
n = 10
n = 10
total = n
for i in range(n-1, 0, -1):
    total = total * i
print(total)
```
再起とは自分自身を実行中で呼び出すプログラミング手法です。  
```
def factorial(n):
    if n = 0:
        return 1 # 0!は1のため
    return n * factorial(n - 1)
```

## Excelの操作

## 課題イメージ
<img src="./images/PythonB.png" width="50%">
