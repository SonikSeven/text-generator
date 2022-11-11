import random


def main():
    with open(input(), encoding="utf-8") as corpus_file:
        corpus = corpus_file.read().split()
    first_words = [word for word in set(corpus) if word[0].isupper() and word[-1] not in ".?!"]
    trails = {}
    for i in range(len(corpus) - 1):
        trails.setdefault(corpus[i], {})
        trails[corpus[i]].setdefault(corpus[i + 1], 0)
        trails[corpus[i]][corpus[i + 1]] += 1
    for _ in range(10):
        chain = [random.choice(first_words)]
        while len(chain) < 5 or chain[-1][-1] not in ".?!":
            chain += random.choices(tuple(trails[chain[-1]].keys()), tuple(trails[chain[-1]].values()))
        print(" ".join(chain))


if __name__ == "__main__":
    main()
