# Text Generator

This Python script employs a simple Markov chain-like model to generate text chains from a given corpus. By analyzing the input text, it constructs sentences that, while random, bear a semblance of grammatical structure and coherence based on the original text's patterns.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/text-generator.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Usage

Once the script is running, input the path to to the text file you wish to use as the corpus for generating sentences. The script will then generate and print ten sentences based on the input text.

## How It Works

The script reads the entire text of the provided corpus and performs the following actions:

1. Identifies words that start with an uppercase letter and do not end with a punctuation mark (`.` `?` `!`) as potential sentence starters.
2. Builds a dictionary (`trails`) mapping each word to its subsequent word along with the occurrence frequency.
3. Generates ten sentences by:
   - Starting with a randomly selected first word,
   - Randomly choosing subsequent words based on their occurrence frequency following the previous word in the chain,
   - Continuing a word ending with a punctuation mark is reached to conclude the sentence.

## License

This project is licensed under the [MIT License](LICENSE.txt).
