import calories_calculator

def test_top():
    """GIVEN a full input file
    when the calculation of the elf carrying more calories is requested
    THEN return the correct elf"""
    expected_output = (35, 71780)

    assert calories_calculator.top("testInputs/downloadedInput.csv") == expected_output

def test_top3():
    """GIVEN a full input file
    when the calculation of the three elves carrying more calories is requested
    THEN return the list of the three elves which carries more calories"""
    expected_output = [(35, 71780), (225, 71481), (76, 69228)]

    assert calories_calculator.top3("testInputs/downloadedInput.csv") == expected_output

def test_top_empty_input():
    """GIVEN an empty input file
    when the calculation of the elf carrying more calories is requested
    THEN return None"""
    assert not calories_calculator.top("testInputs/empty.csv")

def test_top3_empty_input():
    """GIVEN a full input file
    when the calculation of the three elves carrying more calories is requested
    THEN return an empty list"""
    assert not calories_calculator.top3("testInputs/empty.csv")

def test_top_single_elf_input():
    """GIVEN an input file with just one elf
    when the calculation of the elf carrying more calories is requested
    THEN return the first elf and the calories he carries"""
    expected_output = (1, 1700)

    assert calories_calculator.top("testInputs/singleElf.csv") == expected_output

def test_top3_signle_elf_input():
    """GIVEN an input file with just one elf
    when the calculation of the three elves carrying more calories is requested
    THEN return a single item list"""
    expected_output = [(1, 1700)]

    assert calories_calculator.top3("testInputs/singleElf.csv") == expected_output
