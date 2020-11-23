# Steam Hype

[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

![Illustration][wiki-illustration]

This repository contains Python code to find upcoming Steam games with many followers.

## Requirements

-   Install the latest version of [Python 3.X](https://www.python.org/downloads/).
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

As of November 2020, SteamHype.com is down.
Please refer to [this Colab notebook][colab-notebook-steam-hype] to rely on SteamDB.
[![Open In Colab][colab-badge]][colab-notebook-steam-hype]

---

To download data:

```bash
python download_hype.py
```

To print formatted output:

```bash
python utils.py
```

To compare top followed games to top wishlisted games:

```bash
python compare_to_top_wishlists.py
``` 

## Results

Results are shown [on the Wiki][wiki-results].

The [rank-order correlation][wikipedia-correlation] between the top followed games (depth=166) and the top wishlisted games is slightly positive:
-   [Spearman rho](http://scipy.github.io/devdocs/generated/scipy.stats.spearmanr.html#scipy.stats.spearmanr) coefficient ~ 0.130
-   [Kendall's tau](http://scipy.github.io/devdocs/generated/scipy.stats.kendalltau.html#scipy.stats.kendalltau) coefficient ~ 0.087
-   [Weighted Kendall's tau](http://scipy.github.io/devdocs/generated/scipy.stats.weightedtau.html#scipy.stats.weightedtau) coefficient ~ 0.009
-   Average overlap ~ 61.7%
-   [Rank-biased overlap](https://github.com/dlukes/rbo) ~ 62.3%

## References

-   [A tweet by the game dev Lars Doucet][larsiusprime-tweet]
-   [A blog post by the indie consultant Simon Carless][gamediscoverability]
-   An official ranking of [the most wishlisted upcoming Steam games][steam-popularwishlist]
-   SteamDB:
    - upcoming games [clustered by release date][steamdb-upcoming],
    - upcoming games [sorted by descending number of followers][steamdb-hype], after [this tweet][thexpaw-tweet] in November 2020.
-   [Steam Hype API][steamhype-api], which is not my work, and which my script relies on. **Edit**: As of November 2020, the API is unavailable.

<!-- Definitions -->

[build]: <https://travis-ci.org/woctezuma/steam-hype>
[build-image]: <https://travis-ci.org/woctezuma/steam-hype.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/steam-hype/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/steam-hype/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/steam-hype/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/steam-hype>
[codecov-image]: <https://codecov.io/gh/woctezuma/steam-hype/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/steam-hype>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/dee72123ee614a8c9f38590830803a44>

[wiki-illustration]: <https://raw.githubusercontent.com/wiki/woctezuma/steam-hype/img/ranking_2019_08_15.png>
[wiki-results]: <https://github.com/woctezuma/steam-hype/wiki/Results>

[wikipedia-correlation]: <https://en.wikipedia.org/wiki/Rank_correlation>

[larsiusprime-tweet]: <https://twitter.com/larsiusprime/status/1159475890004385793>
[gamediscoverability]: <https://gamediscoverability.substack.com/p/steams-follower-counts-hidden-in>
[steam-popularwishlist]: <https://store.steampowered.com/search/?filter=popularwishlist>
[steamdb-upcoming]: <https://steamdb.info/upcoming/>
[steamhype-api]: <https://steamhype.com/calendar>

[thexpaw-tweet]: <https://twitter.com/thexpaw/status/1330805825355591681>
[steamdb-hype]: <https://steamdb.info/upcoming/?hype>

[colab-notebook-steam-hype]: <https://colab.research.google.com/github/woctezuma/steam-hype/blob/master/steam_hype.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
