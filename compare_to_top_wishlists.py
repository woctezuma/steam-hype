# References:
# -   https://en.wikipedia.org/wiki/Rank_correlation
# -   https://stackoverflow.com/questions/13574406/how-to-compare-ranked-lists
# -   http://scipy.github.io/devdocs/stats.html#correlation-functions
# -   https://github.com/dlukes/rbo

from scipy import stats

from parse_steam import load_steam_ranking
from parse_steamdb import load_steamdb_ranking
from rbo import average_overlap, rbo
from utils import load_manual_wishlist_snapshot, sort_by_followers


def trim_rankings(ranking_A, ranking_B, depth=None, verbose=True):
    if depth is None:
        depth = min(len(ranking_A), len(ranking_B))

    ranking_A = ranking_A[:depth]
    ranking_B = ranking_B[:depth]

    if verbose:
        print(f'\nTrimming rankings to depth = {depth}.')

    return ranking_A, ranking_B


from convert_ranking import (
    convert_ranking_to_vector_of_ranks,
    convert_ranking_to_vector_of_scores,
    list_app_ids,
)


def compute_rho(ranking_A, ranking_B):
    # Arrays of ranks
    app_ids = list_app_ids(ranking_A, ranking_B, verbose=True)
    x = convert_ranking_to_vector_of_ranks(ranking_A, app_ids=app_ids)
    y = convert_ranking_to_vector_of_ranks(ranking_B, app_ids=app_ids)
    # NB: we would get the same rho with arrays of scores.

    rho, p_value = stats.spearmanr(x, y)

    print(f'Spearman rank-order correlation coefficient: {rho:.4f}')
    print(f'p-value to test for non-correlation: {p_value:.4f}')

    return rho, p_value


def compute_tau(ranking_A, ranking_B):
    # Arrays of ranks
    app_ids = list_app_ids(ranking_A, ranking_B)
    x = convert_ranking_to_vector_of_ranks(ranking_A, app_ids=app_ids)
    y = convert_ranking_to_vector_of_ranks(ranking_B, app_ids=app_ids)
    # NB: we would get the same tau with arrays of scores.

    tau, p_value = stats.kendalltau(x, y)

    print(f'Kendall rank-order correlation coefficient: {tau:.4f}')
    print(f'p-value to test for non-correlation: {p_value:.4f}')

    return tau, p_value


def compute_weighted_tau(ranking_A, ranking_B):
    # Arrays of scores
    app_ids = list_app_ids(ranking_A, ranking_B)
    x = convert_ranking_to_vector_of_scores(ranking_A, app_ids=app_ids)
    y = convert_ranking_to_vector_of_scores(ranking_B, app_ids=app_ids)
    # NB: it is important NOT to feed arrays of ranks for the weighted tau!
    #
    # > Note that if you are computing the weighted on arrays of ranks, rather than of scores (i.e., a larger value
    # > implies a lower rank) you must negate the ranks, so that elements of higher rank are associated with a larger
    # > value.
    #
    # Reference: http://scipy.github.io/devdocs/generated/scipy.stats.weightedtau.html#scipy.stats.weightedtau

    weighted_tau, p_value = stats.weightedtau(x, y)

    print(
        'Weighted Kendall rank-order correlation coefficient: {:.4f}'.format(
            weighted_tau,
        ),
    )
    print(f'p-value to test for non-correlation: {p_value:.4f}')

    return weighted_tau, p_value


def compute_rank_biased_overlap(ranking_A, ranking_B, rbo_parameter=0.99):
    rbo_output = rbo(ranking_A, ranking_B, p=rbo_parameter)

    rbo_lower_bound = rbo_output.min
    rbo_residual = rbo_output.res
    rbo_estimate = rbo_output.ext

    reference_overlap = average_overlap(ranking_A, ranking_B)

    print(f'Rank-biased overlap estimate: {rbo_estimate:.4f}')
    print(f'Average overlap = {reference_overlap:.4f}')

    return rbo_estimate, reference_overlap


def compute_several_rank_correlations(ranking_A, ranking_B, rbo_parameter=0.99):
    rho, p_value = compute_rho(ranking_A, ranking_B)
    tau, p_value = compute_tau(ranking_A, ranking_B)
    weighted_tau, p_value = compute_weighted_tau(ranking_A, ranking_B)
    rbo_estimate, reference_overlap = compute_rank_biased_overlap(
        ranking_A,
        ranking_B,
        rbo_parameter=rbo_parameter,
    )

    return True


def load_data_v1():
    top_follows = sort_by_followers()

    top_wishlists = load_manual_wishlist_snapshot()

    return top_follows, top_wishlists


def load_data_v2():
    top_follows = load_steamdb_ranking()
    top_wishlists = load_steam_ranking()

    return top_follows, top_wishlists


def run_statistical_analysis(top_follows, top_wishlists, verbose=False):
    if verbose:
        print(f'Top follows: {top_follows}')
        print(f'Top wishlists: {top_wishlists}')

    top_follows, top_wishlists = trim_rankings(top_follows, top_wishlists, depth=None)

    compute_several_rank_correlations(top_follows, top_wishlists, rbo_parameter=0.99)
    return True


def main(version=1, verbose=True):
    if version > 1:
        top_follows, top_wishlists = load_data_v2()
    else:
        top_follows, top_wishlists = load_data_v1()

    run_statistical_analysis(top_follows, top_wishlists, verbose=verbose)

    return True


if __name__ == '__main__':
    main(version=2)
