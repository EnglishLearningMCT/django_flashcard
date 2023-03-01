#インクルードタグの作成

from django import template

from cards.models import BOXES, Card

#テンプレートタグを登録するための Library のインスタンスを作成
register = template.Library()

#Library インスタンスの .inclusion_tag() をデコレータとして使用
#デコレータ :  ある関数を修飾するための関数とその仕組み
@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count()   #現在ボックスにあるカード枚数を記録するcard_countを定義
        boxes.append({"number": box_num, "card_count": card_count}) #ボックス番号をキー, カード枚数を値とした辞書をリストへ追加

    return {"boxes": boxes} #辞書(boxes)を返す
