from sisl import Statement
from typing import List
import os

def main():
    results: dict = Statement.make_statements("testing.txt")
    
    class Test:
        kind: str
        attr: List[str]
        tests: List[str]
        body: str
        sep: str

        def __init__(self, kind, attr, tests, sep):
            self.kind = kind
            self.attr = attr
            self.tests = tests
            self.sep = sep

        def print_out(self) -> str:
            # String to be returned and the original body
            outStr = ""
            tempstr = self.body 

            # For each test
            for t in self.tests:
                # Split them by the separator
                split = t.split(sep)

                # For each attribute
                for i in range(len(self.attr)):
                    # Replace every instance of the placeholder attribute with the 
                    # Corresponding test variable
                    tempstr = tempstr.replace( "$" + self.attr[i] + "$" , split[i])

                # Add to outstring with some whitespace
                outStr += tempstr + "\n\n"

                # Reset tempstr
                tempstr = self.body 
            
            # Return outstr
            return(outStr)
        
    # Get the only test, and the separator
    t = results["TEST"][0]
    sep = results["SEP"][0].title

    # Get the only template
    template = results["TEMPLATE"][0]

    # Form the first test
    test = Test(t.title, template.attr, t.body, sep)

    # Set template to test body
    test.body = "\n".join(template.body)

    # Get the header
    head = "\n".join(results["HEADER"][0].body) + "\n"

    # Open file with corresponding outfile name
    f = open(results["OUTFILE"][0].title, "w")

    # Write and close file
    f.write(head + test.print_out())
    f.close()

    # Run file with corresponding command
    os.system("".join(results["CMD"][0].body).strip())

main()