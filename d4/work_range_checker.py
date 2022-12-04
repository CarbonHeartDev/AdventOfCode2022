def parse_range_string(rng):
    i1,i2 = (rng[:-1]).split(",")
    return (list(map(lambda n: int(n),i1.split("-"))), list(map(lambda n: int(n),i2.split("-"))))

def range_contains_the_other(rng):
    ((i1l,i1h),(i2l,i2h)) = parse_range_string(rng)
    return ((i1l >= i2l and i1h <= i2h) or (i2l >= i1l and i2h <= i1h))

def ranges_overlap(rng):
    ((i1l,i1h),(i2l,i2h)) = parse_range_string(rng)
    return not(i1h < i2l or i1l > i2h)

def count_ranges_containing_the_other(input_file):
    return len(list(filter(range_contains_the_other, open(input_file))))
    
def count_overlapping_ranges(input_file):
    return len(list(filter(ranges_overlap, open(input_file))))
