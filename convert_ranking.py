import numpy as np


def list_app_ids(ranking_A, ranking_B, verbose=False):
    app_ids = sorted(set(ranking_A).union(ranking_B))
    if verbose:
        print(f'#appIDs = {len(app_ids)}')
    return app_ids


def convert_ranking_for_scipy(ranking, app_ids, reverse_order=False):
    out_of_bound_rank = len(ranking) + 1

    v = np.zeros(len(app_ids)).astype(np.int32)
    for i, app_id in enumerate(app_ids):
        try:
            # NB: ranks are between 1 and len(ranking)
            rank = ranking.index(app_id) + 1
        except ValueError:
            # NB: the out-of-bound rank is len(ranking)+1
            rank = out_of_bound_rank
        v[i] = rank

    if reverse_order:
        # For weighted tau, we have to ensure that **scores** (based on reversed ranks) are non-negative.
        # NB: scores are between 1 and len(ranking), and the out-of-bound score is 0.
        v = out_of_bound_rank - v

    return v


def convert_ranking_to_vector_of_ranks(ranking, app_ids):
    return convert_ranking_for_scipy(ranking, app_ids, reverse_order=False)


def convert_ranking_to_vector_of_scores(ranking, app_ids):
    return convert_ranking_for_scipy(ranking, app_ids, reverse_order=True)


def run_example():
    ranking = ["a", "c", "b", "d"]
    references = 'abcd'

    ranks = convert_ranking_to_vector_of_ranks(ranking, references)
    print({k: v for (k, v) in zip(references, ranks)})

    scores = convert_ranking_to_vector_of_scores(ranking, references)
    print({k: v for (k, v) in zip(references, scores)})

    return True


def main():
    run_example()

    return True


if __name__ == '__main__':
    main()
