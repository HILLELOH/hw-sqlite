import pytest
from analyze import condorcet_winner, net_support_for_candidate1
from testcases import parse_testcases

testcases = parse_testcases("testcases.txt")

def run_testcase(party:str):
    if party == "condorcet_winner":
        return f"{condorcet_winner()}"
    else:
        candidate1,candidate2 = party.split(",")
        return f"{net_support_for_candidate1(candidate1,candidate2)}"


@pytest.mark.parametrize("testcase", testcases, ids=[testcase["name"] for testcase in testcases])
def test_cases(testcase):
    actual_output = run_testcase(testcase["input"])
    assert actual_output == testcase["output"], f"Expected {testcase['output']}, got {actual_output}"


def test_new_cases():
    # your new tests here
    pass
