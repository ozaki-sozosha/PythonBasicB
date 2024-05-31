import os, csv

class Parrot:
    filename = "parrot.csv" # 永続化のためのCCSV
    words = [] # 答えを格納する配列

    # コンストラクタ
    def __init__(self):
        if os.path.isfile(self.filename):
            #csvファイルを読み出す
            with open(self.filename, encoding='utf8') as f:
                csvreader = csv.reader(f)
                for row in csvreader:
                    self.words.extend(row)
    # 質問するメソッド
    def requireWord(self):
        return input("何か話かけてください").strip()
    
    # 返事をするメソッド        
    def reply(self,newWord):
        #無言チェック
        if not newWord:
            print("なんか言え！")
        if newWord in self.words:
            print("それさっき聞いた")
        else:
            print(newWord)
            self.words.append(newWord)

    # 返事を格納するメソッド
    def store(self):
        with open(self.filename, 'w',encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow(self.words)

    # 終了メソッド
    def sayGoobBye(self,newWord):
        if newWord == "さようなら":
            #データを格納
            self.store()
            #終了
            print("さようなら")
            return True
        return False

    