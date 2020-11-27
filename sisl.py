from typing import List

class Statement(object):
        kind: str
        title: str
        attr: List[str]
        body: List[str]

        # Initializer function
        def __init__(self, kind:str, title:str, 
					 attr:List[str] = None, body:List[str] = None):
            self.kind  = kind 
            self.title = title
            self.attr  = attr 
			
            if (body == []):
                self.body = None
            else:
                self.body = body 

        # Str function
        def __str__(self) -> str:
            # Build string
            return self.kind + "\n\t" + self.title + "\n\t" + str(self.attr) + "\n\t" +str(self.body)
		
        # Make statements from file
        def make_statements(filename):
            # Statement reference
            reference: dict = {}

            # File contents
            lines = open(filename).readlines()

            i = 0
            # Loop through lines
            while(i < len(lines)):
                if lines[i][0] == "#" or lines[i] == "\n":
                    i += 1

                else:
                    # Split the parts of new section
                    parts = lines[i].strip('\n').split(" ")

                    # Body (if available)
                    body = []

                    # Check any attributes
                    if len(parts) > 2:
                        attr = parts[2:len(parts)]
                    else:
                        attr = None

                    # Go to next line
                    i += 1

                    # Go to next char containing line
                    while(i < len(lines) and (lines[i] == "\n" or lines[i][0] == '#')):
                        i += 1

                    # If encounter a body
                    if i < len(lines) and lines[i].strip("\n") == ":START":
                        # Next line
                        i += 1

                        # While not the end of the body
                        while(lines[i].strip("\n") != ":END"):
                            # Append line to body
                            body.append(lines[i])
                            
                            # Next line
                            i+= 1

                        # Begin new statement
                        i+= 1

                    # Make new statement
                    s = Statement(parts[0], parts[1], attr, body)

                    # Set new statement
                    if s.kind in reference:
                        reference[s.kind].append(s)
                    else:
                        reference[s.kind] = [s]

            return reference