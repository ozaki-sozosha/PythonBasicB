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

## Excelの操作

## 課題イメージ
<img src="./images/PythonB.png" width="50%">
