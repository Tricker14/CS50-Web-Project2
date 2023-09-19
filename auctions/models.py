from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class AuctionListing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="auction_category")
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image_URL = models.URLField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auction")
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auction_bidder", blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.owner}, {self.winner}"
    
class Bid(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bid")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_action")

    def __str__(self):
        return f"{self.price}: {self.product.name}"

class Comment(models.Model):
    comment = models.CharField(max_length=250)
    product = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comment")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_action")

    def __str__(self):
        return f"{self.comment} by: {self.product.name}"
    
class Watchlist(models.Model):
    product = models.ManyToManyField(AuctionListing, blank=True, related_name="watchlist")
    watcher = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="watchlist_action")

    def __str__(self):
        return f"{self.watcher}"
