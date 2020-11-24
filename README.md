# Steam Hype

[![Build status with Github Action][build-image-action]][build-action]
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

Previously, when SteamHype.com was up, usage was as follows.

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
-   [Spearman rho][scipy-rho] coefficient ~ 0.28
-   [Kendall's tau][scipy-tau] coefficient ~ 0.19
-   [Weighted Kendall's tau][scipy-wtau] coefficient ~ 0.60
-   Average overlap ~ 61.7%
-   [Rank-biased overlap][github-rbo] ~ 62.3%

As of November 2020, using SteamDB's hype (depth=250), as SteamHype.com is down:
-   Spearman rho coefficient ~ 0.44
-   Kendall's tau coefficient ~ 0.33
-   Weighted Kendall's tau coefficient ~ 0.64
-   Average overlap ~ 66.5%
-   Rank-biased overlap ~ 68.0%

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

[build-action]: <https://github.com/woctezuma/steam-hype/actions>
[build-image-action]: <https://github.com/woctezuma/steam-hype/workflows/Python application/badge.svg?branch=master>

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
[scipy-rho]: <http://scipy.github.io/devdocs/generated/scipy.stats.spearmanr.html#scipy.stats.spearmanr>
[scipy-tau]: <http://scipy.github.io/devdocs/generated/scipy.stats.kendalltau.html#scipy.stats.kendalltau>
[scipy-wtau]: <http://scipy.github.io/devdocs/generated/scipy.stats.weightedtau.html#scipy.stats.weightedtau>
[github-rbo]: <https://github.com/dlukes/rbo>

[larsiusprime-tweet]: <https://twitter.com/larsiusprime/status/1159475890004385793>
[gamediscoverability]: <https://gamediscoverability.substack.com/p/steams-follower-counts-hidden-in>
[steam-popularwishlist]: <https://store.steampowered.com/search/?filter=popularwishlist>
[steamdb-upcoming]: <https://steamdb.info/upcoming/>
[steamhype-api]: <https://steamhype.com/calendar>

[thexpaw-tweet]: <https://twitter.com/thexpaw/status/1330805825355591681>
[steamdb-hype]: <https://steamdb.info/upcoming/?hype>

[colab-notebook-steam-hype]: <https://colab.research.google.com/github/woctezuma/steam-hype/blob/master/steam_hype.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
