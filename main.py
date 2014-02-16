from unshred.factory.simple import create_simple_unshredder


def main():
    unshredder = create_simple_unshredder(
        'assets/shredded_images/TokyoPanoramaShredded.png', 32)
    answer = unshredder.solve()
    answer.save('output/answer.png')

if __name__ == "__main__":
    main()