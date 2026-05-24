import sqlite3

DB = "poll.db"

def _get_col(candidate: str) -> str:
    """Return the Q6_N column name for a candidate name."""
    with sqlite3.connect(DB) as conn:
        cur = conn.execute(
            "SELECT Variable FROM codes_for_questions WHERE Label = ?", (candidate,)
        )
        row = cur.fetchone()
    if row is None:
        raise ValueError(f"Unknown candidate: {candidate}")
    return row[0]


def net_support_for_candidate1(candidate1: str, candidate2: str) -> int:
    """
    Return #voters preferring candidate1 over candidate2 minus #voters preferring candidate2 over candidate1.

    >>> net_support_for_candidate1("בני גנץ", "יאיר לפיד")
    47
    >>> net_support_for_candidate1("בנימין נתניהו", "יולי אדלשטיין")
    11
    >>> net_support_for_candidate1("ניר ברקת", "נפתלי בנט")
    -45
    """
    col1, col2 = _get_col(candidate1), _get_col(candidate2)
    with sqlite3.connect(DB) as conn:
        cur = conn.execute(
            f"SELECT SUM(CASE WHEN {col1} < {col2} THEN 1 WHEN {col1} > {col2} THEN -1 ELSE 0 END)"
            " FROM list_of_answers"
        )
        return int(cur.fetchone()[0])


def condorcet_winner() -> str:
    """
    Return the name of the Condorcet winner (beats every other candidate pairwise), or "אין" if none exists.

    >>> condorcet_winner() in ["בנימין נתניהו", "יאיר לפיד", "בני גנץ", "גדעון סער", "נפתלי בנט", "ניר ברקת", "יולי אדלשטיין", "אין"]
    True
    """
    with sqlite3.connect(DB) as conn:
        candidates = [
            row[0]
            for row in conn.execute(
                "SELECT Label FROM codes_for_questions WHERE Variable LIKE 'Q6_%' AND Label NOT LIKE '%אחר%'"
            ).fetchall()
        ]
        for c1 in candidates:
            if all(net_support_for_candidate1(c1, c2) > 0 for c2 in candidates if c2 != c1):
                return c1
    return "אין"


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
