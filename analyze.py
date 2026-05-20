import sqlite3

def net_support_for_candidate1(candidate1:str, candidate2:str)->int:
    # Your code here
    pass

def condorcet_winner()->str:
    # Your code here
    pass


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

    # Use this code for testing via console input-output:
    # party = input()
    # if party == "condorcet_winner":
    #     print(condorcet_winner())
    # else:
    #     candidate1,candidate2 = party.split(",")
    #     print(net_support_for_candidate1(candidate1,candidate2))
