from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:auction_id>", views.auction, name="auction"),
    path("create", views.create, name="create"),
    path("add_comment/<int:auction_id>", views.add_comment, name="add_comment"),
    path("place_bid/<int:auction_id>", views.place_bid, name="place_bid"),
    path("close_auction/<int:auction_id>", views.close_auction, name="close_auction"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_watchlist/<int:auction_id>", views.add_watchlist, name="add_watchlist"),
    path("remove_watchlist/<int:auction_id>", views.remove_watchlist, name="remove_watchlist"),
    path("category", views.category, name="category"),
    path("category/<int:category_id>", views.get_category, name="get_category")
]
