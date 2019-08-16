# Data

This repository contains data about games with:
-   most wishlists,
-   the highest number of followers.

## Source

### Wishlists

The file `top_wishlists.json` is a manual compilation of [the top 100 most wishlisted upcoming Steam games](https://store.steampowered.com/search/?filter=popularwishlist)
(the first four pages), as of August 16, 2019.

### Followers

The file `upcoming_games.json` is the output of `download_hype.py`, and consists of the most followed upcoming Steam
games, with the minimum number of followers arbitrarily set to `5000`.
