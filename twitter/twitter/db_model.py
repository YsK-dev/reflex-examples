from sqlmodel import Field

import reflex as rx


class Follows(rx.Model, table=True):
    """A table of Follows. This is a many-to-many join table.

    See https://sqlmodel.tiangolo.com/tutorial/many-to-many/ for more information.
    """

    followed_username: str = Field(primary_key=True)
    follower_username: str = Field(primary_key=True)


class User(rx.Model, table=True):
    """A table of Users."""

    username: str
    password: str
    profile_photo: str = ""  # URL or path to profile photo
    bio: str = ""  # User bio/description
    display_name: str = ""  # Display name (different from username)
    location: str = ""  # User location
    website: str = ""  # User website


class Tweet(rx.Model, table=True):
    """A table of Tweets."""

    content: str
    created_at: str

    author: str


class Like(rx.Model, table=True):
    """A table of Likes. Tracks which users liked which tweets."""

    tweet_id: int = Field(primary_key=True)
    username: str = Field(primary_key=True)
