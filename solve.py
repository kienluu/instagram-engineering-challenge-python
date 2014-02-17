import logging
import sys
from unshred.factory.simple import create_simple_unshredder

ch = logging.StreamHandler(stream=sys.stdout)
logger = logging.getLogger('unshredder')
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)


def main():
    unshredder = create_simple_unshredder(
        'assets/shredded_images/city_night_10.png', 10)
    answer = unshredder.solve()
    answer.save('output/city_night_simple_answer.png')

if __name__ == "__main__":
    main()