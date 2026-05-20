"""
Functions for parsing and running testcases from the testcases.txt file.

Written by Claude Code.
"""

def parse_testcases(filename:str):
    cases = []
    current = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("case="):
                current = {"name": line[5:]}
            elif line.startswith("input="):
                current["input"] = line[6:]
            elif line.startswith("output="):
                current["output"] = line[7:]
                cases.append(current)
    print("Cases: \n", cases)
    return cases
