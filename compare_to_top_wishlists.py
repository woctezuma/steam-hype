from utils import sort_by_followers, load_manual_wishlist_snapshot


def main(verbose=True):
    top_follows = sort_by_followers()

    top_wishlists = load_manual_wishlist_snapshot()

    if verbose:
        print('Top follows: {}'.format(top_follows))
        print('Top wishlists: {}'.format(top_wishlists))

    return True


if __name__ == '__main__':
    main()
