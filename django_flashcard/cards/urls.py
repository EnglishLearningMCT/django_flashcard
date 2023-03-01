#cardsアプリに渡されるURLの処理

from django.urls import path
from . import views

urlpatterns = [ #各ページのURL, ビュー, 名称を格納するリスト
    path(   #カードリスト
        "",
        #TemplateView.as_view(template_name="cards/base.html"),
        views.CardListView.as_view(),
        name="card-list"  
    ),
    path(   #カード作成
        "new",
        views.CardCreateView.as_view(),
        name="card-create"
    ),
    path(   #カード更新
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),
    path(   #ボックス内カード表示
        "box/<int:box_num>",
        views.BoxView.as_view(),
        name="box"
    ),
]