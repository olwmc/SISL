from sisl import Statement

def add_entry(filename):
    # Get entry name
    entry_name = ""
    while(entry_name == ""):
        entry_name = input("Entry name (Cannot be blank): ")
    
    # Get category
    category = ""
    while(category == ""):
        category = input("Category (Cannot be blank): ")
    
    # Get tags
    tags = input("Separate tags by commas: ")

    # Get description
    description = input("Enter a description: ")

    # If empty, make an empty list
    if tags == "":
        tags = []
    else:
        tags = tags.split(",")

    # Scrub spaces for underscores
    entry_name = entry_name.replace(" ", "_")
    category = category.replace(" ", "_")

    for i in range(len(tags)):
        tags[i] = tags[i].replace(" ", "_")

    # Open file
    f = open(filename, "a")

    # Write first line
    f.write(category + " " + entry_name + " " + " ".join(tags) + "\n")
    
    # Write description
    f.write(":START\n")
    f.write(description + "\n")
    f.write(":END\n")

    # Close
    f.close()

def read_entries(filename):
    statements = Statement.make_statements(filename)
    for k in statements.keys():
        print(k)
        for entry in statements[k]:
            print(entry)