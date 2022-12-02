def calculate_tournament_score_method1(input_file):
    total_score = 0
    for line in open(input_file, "r", encoding="utf8"):
        their = ord(line[0]) - ord("A")
        your = ord(line[2]) - ord("X")

        total_score += your+1
        if(your == their):
            total_score += 3
        if((their + 1) % 3 == your):
            total_score += 6

    return total_score

def calculate_tournament_score_method2(input_file):
    total_score = 0
    for line in open(input_file, "r", encoding="utf8"):
        their = ord(line[0]) - ord("A")
        match_outcome = ord(line[2]) - ord("X")
        your = (their + (match_outcome - 1)) % 3

        total_score += (match_outcome * 3) + (your+1)

    return total_score