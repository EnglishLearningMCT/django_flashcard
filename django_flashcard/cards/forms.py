#カードチェック(単語確認)ページのフォーム

from django import forms


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True) #チェックするカードの主キー
    solved = forms.BooleanField(required=False) #答えわかる→True, そうでないならFalse
