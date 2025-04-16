"""
Download the staff solution of the Commerce project and copy this file into auctions/tests.py

Run this file via `python manage.py tests`
"""

from django.test import Client, TestCase

from .models import *

users = {
    "test0": {"email": "test0@test.me", "password": "test0password"},
    "test1": {"email": "test1@test.me", "password": "test1password"},
    "test2": {"email": "test2@test.me", "password": "test2password"},
}

NUM_ITEMS = 3

# Create your tests here.
class CommerceTestCase(TestCase):

    def setUp(self):
        # make users
        for username in users:
            user = User.objects.create_user(username, users[username]["email"], users[username]["password"])

            for i in range(NUM_ITEMS):
            # make some items for them
                Listing.objects.create(
                    seller=user,
                    description=f"This is {user}'s item {i}",
                    starting_bid=10 + i,
                    title=f"{user} item {i}"
                )


    def test_user_has_items(self):      
        username = "test0"
        self.assertEqual(User.objects.get(username=username).listings.count(), NUM_ITEMS)
    

    def test_create_listing(self):
        username = "test0"
        c = Client()
        
        # Note what happens if we omit this line... arguably a user shouldn't be able to create a listing without logging in first
        c.login(username=username, password=users[username]["password"])
        
        # Make a post request
        response = c.post("/create", {
            "description": "Test create desc",
            "starting_bid": 100.01,
            "title": "Test create title"
        }, follow=True)

        # make sure that new listing has ended up in the context of the index
        self.assertIn(Listing.objects.get(title="Test create title"), response.context["listings"])


    def test_close_own_item(self):
        username = "test0"
        c = Client()
        
        c.login(username=username, password=users[username]["password"])
        listing = User.objects.get(username=username).listings.first()

        response = c.post(f"/listings/{listing.id}/close", follow=True)
        listing.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertFalse(listing.active)


    # Other things you might want to test
    # User unable to close someone else's item
    # User able to bid a valid bid
    # User unable to bid invalid bids
    # Listing max bid updates appropriately 
    # etc
    
