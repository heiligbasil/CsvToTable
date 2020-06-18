import sys


def table_print(items):
    print()
    column = 1
    for item in items:
        print(item.strip(), end='\t')
        column += 1
        if column > column_total:
            print()
            column = 0


def table_html(items):
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
            column = 0
    print("</tr>")


with open(sys.path[0] + '\\contents.csv') as f:
    split_items = f.read().split(sep=',')

column_total = 4
table_print(split_items)
table_html(split_items)
