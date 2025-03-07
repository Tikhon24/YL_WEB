import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str)


def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            rows = file.readlines()
            return len(rows)
    except Exception:
        return 0


def main():
    args = parser.parse_args()
    filename = args.file
    count_rows = count_lines(filename)
    print(count_rows)


if __name__ == '__main__':
    main()
