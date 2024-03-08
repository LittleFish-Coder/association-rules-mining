# Data Mining & Social Network Analysis Assignment 1

To run the program, see the [Usage](#Usage) section at the end of the document.

## Introduction

In this assignment, I use **Apriori Algorithm** to find frequent itemsets and association rules from the given dataset. The dataset contains 88162 transactions and 16470 items. The program reads the dataset from the file and finds the frequent itemsets and association rules. The program also prints the time taken to find the frequent itemsets and association rules.

## Apriori Algorithm

## Final Output

format: each line contains an strong association rule
`{item1, item2, ...} -> {item3, item4, ...} (confidence)`

## Usage

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
