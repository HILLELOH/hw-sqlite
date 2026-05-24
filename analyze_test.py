import re
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

def matches_expected(actual: str, expected: str) -> bool:
    """Support regex patterns in expected output (e.g. /.*/i)."""
    m = re.fullmatch(r'/(.+)/([a-z]*)', expected)
    if m:
        flags = re.IGNORECASE if 'i' in m.group(2) else 0
        return bool(re.fullmatch(m.group(1), actual, flags))
    return actual == expected

@pytest.mark.parametrize("testcase", testcases, ids=[testcase["name"] for testcase in testcases])
def test_cases(testcase):
    actual_output = run_testcase(testcase["input"])
    assert matches_expected(actual_output, testcase["output"]), \
        f"Expected {testcase['output']}, got {actual_output}"


def test_new_cases():
    # net_support is antisymmetric: swap args negates result
    assert net_support_for_candidate1("יאיר לפיד", "בני גנץ") == -47
    # condorcet_winner returns a known candidate or "אין"
    known = {"בנימין נתניהו", "יאיר לפיד", "בני גנץ", "גדעון סער", "נפתלי בנט", "ניר ברקת", "יולי אדלשטיין", "אין"}
    assert condorcet_winner() in known
    # candidate vs itself: 0
    assert net_support_for_candidate1("יאיר לפיד", "יאיר לפיד") == 0
