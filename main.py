from sisl import Statement
from typing import List

def main():
    results: dict = Statement.make_statements("testing.txt")
    
    class Test:
        kind: str
        attr: List[str]
        tests: List[str]

        def __init__(self, kind, attr, tests):
            self.kind = kind
            self.attr = attr
            self.tests = tests

        def __str__(self):
            return (self.kind + " " + str(self.attr) + " " + str(self.tests))

    tests = []
    for t in results["TEST"]:
        tests.append(Test(t.title, results["TEMPLATE"][0].attr, t.body))

    print(tests[0])

    
main()