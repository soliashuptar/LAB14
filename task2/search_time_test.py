import random
import time
import sys

# sys.path.append("..")

from linkedbst import LinkedBST

def main():
    f = open("words.txt")
    data = f.readlines()
    WORDS = random.sample(data, 10000)
    return WORDS


def search_list():
    f = open('words.txt')
    data = f.readlines()
    start = time.time()
    for i in main():
        index = data.index(i)
    return time.time() - start

def search_tree():
    f = open("words.txt")
    data = f.readlines()
    random.shuffle(data)
    tree = LinkedBST()
    start = time.time()
    for word in data:
        tree.add(word)
    for i in main():
        ind = tree.find(i)
    simple_tree = time.time() - start

    tree.rebalance()
    start = time.time()
    for i in main():
        ind = tree.find(i)
    rebalanced_tree = time.time() - start

    return simple_tree, rebalanced_tree

if __name__ == "__main__":
    print("Time of searching with list methods is {}, in tree - {}, in rebalanced tree - {} ".format(
        search_list(), search_tree()[0], search_tree()[1]
    ))