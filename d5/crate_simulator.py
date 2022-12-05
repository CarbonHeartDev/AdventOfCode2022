def parse_crate_layout(file):
    lines = []
    lines.append(FILE.readline())
    while(lines[len(lines) - 1] != " 1   2   3   4   5   6   7   8   9 \n"):
        lines.append(FILE.readline())
    lines.pop()
    lines.reverse()

    crate_layout = [[] for i in range(9)]
    for line in lines:
        for i in range(9):
            char = line[i * 4 + 1]
            if char != ' ':
                crate_layout[i].append(char)

    return crate_layout

def simulate_crate_mover_9000(crate_layout, file):
    for line in FILE:
        n,form_crate,to_crate = line.rstrip().replace("move ","").replace(" from ",",").replace(" to ",",").split(',')
        for i in range(int(n)):
            crate_layout[int(to_crate) - 1].append(crate_layout[int(form_crate) - 1].pop())

def simulate_crate_mover_9001(crate_layout, file):
    for line in FILE:
        n,form_crate,to_crate = line.rstrip().replace("move ","").replace(" from ",",").replace(" to ",",").split(',')
        crate_layout[int(to_crate) - 1] = crate_layout[int(to_crate) - 1] + crate_layout[int(form_crate) - 1][-int(n):]
        crate_layout[int(form_crate) - 1] = crate_layout[int(form_crate) - 1][:-int(n)]
FILE = open("downloadedInput.txt")

#crate_rows = parse_crate_layout(FILE)
#FILE.readline()
#simulate_crate_mover_9001(crate_rows, FILE)
