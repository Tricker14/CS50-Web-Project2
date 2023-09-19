from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, AuctionListing, Bid, Comment, Watchlist, Category

def index(request):
    return render(request, "auctions/index.html", {
        "auctions": AuctionListing.objects.all()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
@login_required
def auction(request, auction_id):
    auction = AuctionListing.objects.get(pk=auction_id)
    highest_bidder = None
    count = 0
    if auction.bid.all():
        for bid in auction.bid.all():
            final_bid = bid.price
            highest_bidder = bid.bidder
            count += 1
    else:
        final_bid = auction.starting_bid
    return render(request, "auctions/auction.html", {
        "auction": auction,
        "bid": final_bid,
        "highest_bidder": highest_bidder,
        "total_bid": count
    })

@login_required
def create(request):
    if request.method == "POST":
        name = request.POST["title"]
        description = request.POST["description"]

        category_id = request.POST["category"]
        if category_id == "":
            category = Category.objects.get(name="Others")
        else:
            category = Category.objects.get(pk=category_id)

        starting_bid = request.POST["starting_bid"]
        image_URL = request.POST["image_URL"]
        owner = request.user

        new_auction = AuctionListing(
            name = name,
            description = description,
            category = category, 
            starting_bid = starting_bid,
            image_URL=image_URL,
            owner = owner
        )
        new_auction.save()
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "auctions/create.html", {
        "categories": Category.objects.all()
    })

@login_required
def add_comment(request, auction_id):
    if request.method == "POST":
        comment = request.POST["comment"]
        if comment:
            new_comment = Comment(
                comment=comment,
                product=AuctionListing.objects.get(pk=auction_id),
                commenter = request.user,
            )
            new_comment.save()
            return HttpResponseRedirect(reverse("auction", args=[auction_id]))
    
    return auction(request, auction_id)

@login_required
def place_bid(request, auction_id):
    if request.method == "POST":
        bid = request.POST["bid"]
        count = 0
        highest_bidder = None
        if bid:     # User type bid
            auction = AuctionListing.objects.get(pk=auction_id)
            if auction.bid.all():   # There are >= 1 bid
                for bid_item in auction.bid.all():
                    highest_bid = bid_item.price
                    highest_bidder = bid_item.bidder
                    count += 1
                if float(bid) > highest_bid:
                    new_bid = Bid(
                        price=bid,
                        product=AuctionListing.objects.get(pk=auction_id),
                        bidder = request.user,
                    )
                    new_bid.save()
                    return HttpResponseRedirect(reverse("auction", args=[auction_id]))
                else:
                    return render(request, "auctions/bid_error.html", {
                        "auction": auction,
                        "bid": highest_bid,
                        "highest_bidder": highest_bidder,
                        "total_bid": count
                    })
            else:   # There are no bids currently
                if float(bid) >= auction.starting_bid:
                    new_bid = Bid(
                        price=bid,
                        product=AuctionListing.objects.get(pk=auction_id),
                        bidder = request.user,
                    )
                    new_bid.save()
                    return HttpResponseRedirect(reverse("auction", args=[auction_id]))
                else:
                    return render(request, "auctions/bid_error.html", {
                        "auction": auction,
                        "bid": auction.starting_bid
                    })
        else:   # User dont type bid but still hit "Enter"
            auction = AuctionListing.objects.get(pk=auction_id)
            if auction.bid.all():
                for bid in auction.bid.all():
                    final_bid = bid.price
                    highest_bidder = bid.bidder
                    count += 1
            else:
                final_bid = auction.starting_bid
            return render(request, "auctions/bid_error.html", {
                "auction": auction,
                "bid": final_bid,
                "highest_bidder": highest_bidder,
                "total_bid": count
            })
    
    return auction(request, auction_id)

@login_required
def close_auction(request, auction_id):
    if request.method == "POST":
        auction = AuctionListing.objects.get(pk=auction_id)
        highest_bidder = None
        count = 0
        if auction.bid.all():
            for bid in auction.bid.all():
                final_bid = bid.price
                highest_bidder = bid.bidder
                count += 1
        else:
            final_bid = auction.starting_bid
            highest_bidder = auction.owner
        auction.winner = highest_bidder
        auction.save()
        return render(request, "auctions/auction.html", {
            "auction": auction,
            "bid": final_bid,
            "highest_bidder": highest_bidder,
            "total_bid": count
        })

    return auction(request, auction_id)

@login_required
def watchlist(request):
    watchlist = Watchlist.objects.filter(watcher=request.user).first()
    if watchlist:
        auctions = watchlist.product.all() 
        return render(request, "auctions/watchlist.html", {
            "auctions": auctions,
        })
    else:
        return render(request, "auctions/watchlist.html", {
            "auctions": None,
        })

@login_required
def add_watchlist(request, auction_id):
    if request.method == "POST":
        item = AuctionListing.objects.get(pk=auction_id)
        watchlist, created = Watchlist.objects.get_or_create(watcher=request.user)
        watchlist.product.add(item)
        return HttpResponseRedirect(reverse("watchlist"))
    return auction(request, auction_id)

@login_required
def remove_watchlist(request, auction_id):
    if request.method == "POST":
        item = AuctionListing.objects.get(pk=auction_id)
        watchlist, _ = Watchlist.objects.get_or_create(watcher=request.user)
        watchlist.product.remove(item)
        return HttpResponseRedirect(reverse("watchlist"))
    return auction(request, auction_id)

@login_required
def category(request):
    categories = Category.objects.all()
    return render(request, "auctions/category.html", {
        "categories": categories
    })

@login_required
def get_category(request, category_id):
    categories = Category.objects.get(pk=category_id)
    # auctions = AuctionListing.objects.filter(category=categories)
    auctions = categories.auction_category.all()
    return render(request, "auctions/index.html", {
        "auctions": auctions
    })



