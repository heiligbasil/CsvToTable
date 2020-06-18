import sys


def calculate_column_count(items):
    """Calculate the number of columns based on the length of the longest item in the list"""
    global column_total
    longest_length = len(max(items, key=len))
    if longest_length < 15:
        column_total = 5
    elif longest_length < 25:
        column_total = 4
    else:
        column_total = 3


def table_print(items):
    """Print the items to screen into the format of a pseudo table"""
    print()
    column = 1
    for item in items:
        print(item.strip(), end='\t')
        column += 1
        if column > column_total:
            print()
            column = 1


def table_html(items):
    """Output the items to screen into a format useful in a HTML table"""
    print()
    print("<tr>")
    column = 1
    for item in items:
        print("<td style=\"text-align:center\">", end='')
        print(item.strip(), end='')
        print("</td>")
        column += 1
        if column > column_total:
            print("</tr>")
            print("<tr>")
            column = 1
    print("</tr>")


# Read in the contents of the .CSV file and split it into a list
with open(sys.path[0] + '\\contents.csv') as f:
    split_items = f.read().split(sep=',')

column_total = 1

calculate_column_count(split_items)
table_print(split_items)
table_html(split_items)
