#フロントエンド部分のプログラム(ビューの作成)

import random

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    #DeleteView,
)

from .models import Card
from .forms import CardCheckForm

#カードリスト
class CardListView(ListView):
    model = Card
    #カードを取得し, ボックスの昇順, 作成日の降順で並べる
    queryset = Card.objects.all().order_by("box", "-date_created")

#カード作成
class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]      #フォームの入力項目
    success_url = reverse_lazy("card-create")   #s成功時に, ...\card-createのURLにリクエストを返す

#カード更新
class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")

#カード削除
''' class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy("card-delete")
 '''
#ボックス
class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    #box_numの値と同じボックス番号のカードを取得
    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    #テンプレートでボックス番号を使用するための処理
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        #現在のカードリスト(self.object_list)が空でないなら, ランダムで1まい選ぶ
        if self.object_list:
            #object_listの中から1枚カードを選ぶ
            context["check_card"] = random.choice(self.object_list)
        return context

    #ポストリクエスト処理
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): #フォームの有効, 無効チェック
            #カードの取得, あるいは404エラー
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"]) 
            #解けたかどうか(solvedの値)によってカードを適切なボックスへ移動
            card.move(form.cleaned_data["solved"])

         #リクエストを投稿したページと同じページにリダイレクト(チェックセッションへ戻る)
        return redirect(request.META.get("HTTP_REFERER"))
