# Data Mining & Social Network Analysis Assignment 1

To run the program, see the [Usage](#Usage) section at the end of the document.

## Introduction

In this assignment, I use **Apriori Algorithm** to find frequent itemsets and association rules from the given dataset. The dataset contains **88162** transactions and **16470** items. The program reads the dataset from the file and finds the frequent itemsets and association rules. The program also prints the time taken to find the frequent itemsets and association rules.

## Apriori Algorithm

Given transactions: `T = {tid1, tid2, ..., tidn}`, `tid = {item1, item2, ..., itemm}`; and minimum support: `min_supp`.

The Apriori algorithm finds the frequent itemsets by using the following steps:

- **Step 1**: Find the frequent 1-itemsets.
- **Step 2**: Generate candidate k-itemsets from frequent (k-1)-itemsets.
- **Step 3**: Prune the candidate k-itemsets that are not frequent.
- **Step 4**: Repeat steps 2 and 3 until no frequent k-itemsets can be generated.

After finding the frequent itemsets, the algorithm return a table(python dictionary) of frequent itemsets and their support count.

## Strong Association Rules

Given frequent itemsets(python dictionary) and minimum confidence: `min_conf`.

The algorithm finds the strong association rules by using the following steps:

- **Step 1**: Generate all possible association rules from the frequent itemsets.
- **Step 2**: Calculate the confidence of each association rule.
- **Step 3**: Prune the association rules that do not satisfy the minimum confidence.

After finding the strong association rules, the algorithm return a list of association rules.

## Final Output Format

Given the association rules, the program writes the output to the `output.txt` file.

In the `output.txt` file, each line contains an strong association rule:

`{item1, item2, ...} -> {item3, item4, ...} (confidence)`

## Time Execution Comparison

| Minimum Support | Minimum Confidence | Time Taken | # of Frequent Itemsets | # of Association Rules |
| --------------- | ------------------ | ---------- | ---------------------- | ---------------------- |
| 1500            | 0.5                | 2.30s      | 68                     | 60                     |
| 1000            | 0.6                | 10.61s     | 135                    | 64                     |

## Usage

clone the repository and run the following command in the terminal:

```bash
git clone https://github.com/LittleFish-Coder/association-rules-mining.git
```

```bash
cd association-rules-mining
```

```bash
python nm6121030.py
```

add arguments to the command line to change the default values of the program.

- `--input` to change the input file
- `--min_supp` to change the minimum support (default: 1500)
- `--min_conf` to change the minimum confidence (default: 0.5)

### Example

```bash
python nm6121030.py --input input.txt --min_supp 1000 --min_conf 0.6
```
