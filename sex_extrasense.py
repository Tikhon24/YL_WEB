import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', default=50,
                    type=int, help='отношение к куклам')
parser.add_argument('--cars', default=50,
                    type=int, help='отношение к машинам')
parser.add_argument('--movie', choices=['melodrama', 'football', 'other'], default='other',
                    type=str, help='выбор категории фильмов')

movies = {
    'melodrama': 0,
    'football': 100,
    'other': 50
}


def main():
    args = parser.parse_args()

    movie = movies[args.movie]

    barbie = args.barbie
    barbie = barbie if 0 <= barbie <= 100 else 50

    cars = args.cars
    cars = cars if 0 <= cars <= 100 else 50

    boy = int((100 - barbie + cars + movie) / 3)
    girl = int(100 - boy)

    print(f'boy: {boy}')
    print(f'girl: {girl}')


if __name__ == '__main__':
    main()
