import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--count', action='store_true')
parser.add_argument('--num', action='store_true')
parser.add_argument('--sort', action='store_true')
parser.add_argument('filename', type=str)


def main():
    try:
        args = parser.parse_args()
        filename = args.filename
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines = list(map(lambda row: row.strip(), lines))
            index = 0
            if args.num:
                index += 2
                for i, line in enumerate(lines):
                    lines[i] = f'{i} {line}'
            if args.sort:
                lines.sort(key=lambda line: line[index:])
        print('\n'.join(lines))
        if args.count:
            print(f'rows count: {len(lines)}')
    except Exception:
        print('ERROR')


if __name__ == '__main__':
    main()
