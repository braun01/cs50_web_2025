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

    # TODO: test that a user has items
                
    # TODO: test that a user can create a new listing
                
    # TODO: test that a user can close its own listing
