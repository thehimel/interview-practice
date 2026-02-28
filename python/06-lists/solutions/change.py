"""
Change list items: index assignment, slice replace, insert.

colors = ["red", "blue", "green", "yellow", "black", "white", "gray"]

Exercise:
- Replace index 2 with "purple".
- Replace indices 1-3 with ["pink","cyan"].
- Replace index 1 with ["mint","navy"].
- Insert "olive" at index 2.
- Return a new list.
"""


def change_items(colors: list) -> list:
    """Apply single index, slice replace, and insert. Return a new list.

    Shallow copy is enough: we only replace or insert elements; we do not mutate
    existing element objects.
    """
    result = colors.copy()
    result[2] = "purple"            # ["red", "blue", "purple", "yellow", "black", "white", "gray"]
    result[1:4] = ["pink", "cyan"]  # ["red", "pink", "cyan", "black", "white", "gray"] — fewer
    result[1:2] = ["mint", "navy"]  # ["red", "mint", "navy", "cyan", "black", "white", "gray"] — more
    result.insert(2, "olive")       # ["red", "mint", "olive", "navy", "cyan", "black", "white", "gray"]
    return result


def main() -> None:
    colors = ["red", "blue", "green", "yellow", "black", "white", "gray"]
    print("colors =", colors)
    print("change_items(colors) =", change_items(colors))
    print("colors unchanged =", colors)


if __name__ == "__main__":
    main()
