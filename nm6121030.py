import argparse
import itertools
import time


def generate_transactions(input_file):
    transactions = []  # list of itemset
    with open(input_file, "r") as f:
        for line in f:
            itemset = line.strip().split()  # list of items
            itemset = [int(item) for item in itemset]
            transactions.append(set(itemset))  # store the itemset as a set
    return transactions


def apriori(transactions, min_supp):
    # generate first candidate itemset
    frequent_itemsets = {}  # key: itemset, value: count

    # create candiate table 1: C1
    C1 = {}  # key: item, value: count
    for tid, transaction in enumerate(transactions):
        for item in transaction:
            item = frozenset([item])  # convert to frozenset: immutable
            if item in C1:
                C1[item] += 1
            else:
                C1[item] = 1
    total_itemsets = len(C1)  # total itemsets number of the raw transactions
    # print(f"Total number of itemsets in C1: {total_itemsets}")
    # fileter out the itemset that does not satisfy the min_supp: L1
    L1 = {}
    for item in list(C1.keys()):
        if C1[item] >= min_supp:
            L1[item] = C1[item]

    # update the frequent itemsets with L1
    frequent_itemsets.update(L1)

    # generate the next candidate itemset
    itemsets = list(L1.keys())
    k = 2
    while itemsets:
        # print(f"k = {k}")
        ck = generate_candidates(itemsets, k)
        lk = prune_candidates(ck, transactions, min_supp)

        if lk:
            frequent_itemsets.update(lk)
            itemsets = list(lk.keys())
            k += 1
        else:
            break

    return frequent_itemsets


def generate_candidates(L, k):
    C = set()
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if len(L[i].union(L[j])) == k:
                C.add(L[i].union(L[j]))
    # print(f"C: {C}")
    return C


def prune_candidates(C, transactions, min_supp):
    L = {}
    for candidate in C:  # { frozenset({item, item}), frozenset({item, item}), ... }
        count = 0
        for transaction in transactions:
            if candidate.issubset(transaction):
                count += 1
        if count >= min_supp:
            # print(f"candidate: {candidate}, count: {count}")
            L[candidate] = count
    return L


def strong_association_rules(frequent_itemsets, min_conf):
    rules = []
    for itemset in frequent_itemsets:
        if len(itemset) > 1:
            for antecedent_size in range(1, len(itemset)):
                for antecedent in itertools.combinations(itemset, antecedent_size):
                    antecedent = frozenset(antecedent)
                    consequent = itemset - antecedent
                    confidence = frequent_itemsets[itemset] / frequent_itemsets[antecedent]
                    if confidence >= min_conf:
                        rules.append((antecedent, consequent, confidence))
    return rules


def format_output_rules(rules):
    output = []
    for rule in rules:
        antecedent = set(list(rule[0]))
        consequent = set(list(rule[1]))
        confidence = rule[2]
        output.append(f"{antecedent} -> {consequent} ({confidence:.2f})")
    return output


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Apriori Algorithm")
    parser.add_argument("--input", type=str, default="input.txt", help="input file name")
    parser.add_argument("--min_supp", type=int, default=1500, help="input min_supp")
    parser.add_argument("--min_conf", type=float, default=0.5, help="input min_conf")
    args = parser.parse_args()

    # get the input file, min_supp and min_conf
    input_file = args.input
    min_supp = args.min_supp
    min_conf = args.min_conf
    print(f"input file: {input_file}")
    print(f"min_supp: {min_supp}")
    print(f"min_conf: {min_conf}")

    # read the input file
    transactions = generate_transactions(input_file)

    ##### start time #####
    start = time.time()

    # apply the apriori algorithm: return the itemsets that satisfy the min_supp
    frequent_itemsets = apriori(transactions, min_supp)
    # apply the strong association rules: return the rules that satisfy the min_conf
    rules = strong_association_rules(frequent_itemsets, min_conf)

    end = time.time()
    ##### end time #####

    # information
    print(f"Number of transactions: {len(transactions)}")
    print(f"Number of frequent itemsets with min_supp = {min_supp}: {len(frequent_itemsets)}")
    print(f"Number of strong association rules with min_conf = {min_conf}: {len(rules)}")
    print(f"Execution time: {end - start:.2f} seconds")

    # format the output and write to the output file
    output_path = "output.txt"
    output = format_output_rules(rules)

    with open(output_path, "w") as f:
        print(f"output file: {output_path}")
        f.write(f"min_supp: {min_supp}, min_conf: {min_conf}\n")
        for line in output:
            f.write(line + "\n")
            print(line)
