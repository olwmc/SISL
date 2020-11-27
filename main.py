from sisl import Statement
from typing import List

def main():
    results: dict = Statement.make_statements("s.txt")
    
    for key in results.keys():
        print(key + ": ")

        for statement in results[key]:
            print("\t" + str(statement) + "\n")
main()
