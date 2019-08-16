# References:
# -   https://en.wikipedia.org/wiki/Rank_correlation
# -   https://stackoverflow.com/questions/13574406/how-to-compare-ranked-lists
# -   http://scipy.github.io/devdocs/stats.html#correlation-functions
# -   https://github.com/dlukes/rbo

from scipy import stats

from rbo import rbo, average_overlap
from utils import sort_by_followers, load_manual_wishlist_snapshot


def trim_rankings(ranking_A,
                  ranking_B,
                  depth=None,
                  verbose=True):
    if depth is None:
        depth = min(len(ranking_A),
                    len(ranking_B))

    ranking_A = ranking_A[:depth]
    ranking_B = ranking_B[:depth]

    if verbose:
        print('\nTrimming rankings to depth = {}.'.format(depth))

    return ranking_A, ranking_B


def compute_several_rank_correlations(ranking_A,
                                      ranking_B,
                                      rbo_parameter=0.99):
    rho, p_value = stats.spearmanr(ranking_A,
                                   ranking_B)

    print('\nSpearman rank-order correlation coefficient: {:.4f}'.format(rho))
    print('p-value to test for non-correlation: {:.4f}'.format(p_value))

    tau, p_value = stats.kendalltau(ranking_A,
                                    ranking_B)

    print('\nKendall rank-order correlation coefficient: {:.4f}'.format(tau))
    print('p-value to test for non-correlation: {:.4f}'.format(p_value))

    weighted_tau, p_value = stats.weightedtau(ranking_A,
                                              ranking_B)

    print('\nWeighted Kendall rank-order correlation coefficient: {:.4f}'.format(weighted_tau))
    print('p-value to test for non-correlation: {:.4f}'.format(p_value))

    rbo_output = rbo(ranking_A,
                     ranking_B,
                     p=rbo_parameter)

    rbo_lower_bound = rbo_output['min']
    rbo_residual = rbo_output['res']
    rbo_estimate = rbo_output['ext']

    reference_overlap = average_overlap(ranking_A,
                                        ranking_B)

    print('\nRank-biased overlap estimate: {:.4f}'.format(rbo_estimate))
    print('Average overlap = {:.4f}'.format(reference_overlap))

    return True


def main(verbose=True):
    top_follows = sort_by_followers()

    top_wishlists = load_manual_wishlist_snapshot()

    if verbose:
        print('Top follows: {}'.format(top_follows))
        print('Top wishlists: {}'.format(top_wishlists))

    top_follows, top_wishlists = trim_rankings(top_follows,
                                               top_wishlists)

    compute_several_rank_correlations(top_follows,
                                      top_wishlists)

    return True


if __name__ == '__main__':
    main()
