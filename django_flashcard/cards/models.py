#カードの型, 動きを定義するプログラム

from django.db import models

NUM_BOXES = 5   #カードボックス数
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model): 
    #djangoのモデルフィールドを使って, 質問, 回答, ボックスのフィールドを作成
    #モデルフィールドは, データベーステーブルのカラムに相当
    question = models.CharField(max_length=100)             #最大文字数100のchar型field
    answer = models.CharField(max_length=100)               #上に同じ
    box = models.IntegerField(                              #カードのボックス番号を記録するフィールド
        choices=zip(BOXES, BOXES),                          #BOX_NUMの範囲内のセレクトボックス
        default=BOXES[0],                                   #デフォルトは最初のボックスに設定
    )
    date_created = models.DateTimeField(auto_now_add=True)  #カードのタイムスタンプ

    def __str__(self):
        return self.question

    #カード移動
    def move(self, solved):
        #答えがわかる → solved == True → 次のボックスへ
        #わからない → solved == False → 最初のボックス(1st BOX)へ
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:    #5番目のBoxのカードはそれ以上移動がないようにする
            self.box = new_box
            self.save()

        return self
