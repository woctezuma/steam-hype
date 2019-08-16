# Steam Hype

[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

![Illustration](https://raw.githubusercontent.com/wiki/woctezuma/steam-hype/img/ranking_2019_08_15.png)

This repository contains Python code to find upcoming Steam games with many followers.

## Requirements

-   Install the latest version of [Python 3.X](https://www.python.org/downloads/).
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

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

Results are shown [on the Wiki](https://github.com/woctezuma/steam-hype/wiki/Results).

## References

-   [A tweet by the game dev Lars Doucet](https://twitter.com/larsiusprime/status/1159475890004385793)
-   [A blog post by the indie consultant Simon Carless](https://gamediscoverability.substack.com/p/steams-follower-counts-hidden-in)
-   An official ranking of [the most wishlisted upcoming Steam games](https://store.steampowered.com/search/?filter=popularwishlist)
-   [SteamDB](https://steamdb.info/upcoming/)
-   [Steam Hype API](https://steamhype.com/calendar), which is not my work, and which my script relies on.

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

