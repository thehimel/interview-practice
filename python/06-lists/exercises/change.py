"""
Change list items: index assignment, slice replace, insert.

colors = ["red", "blue", "green", "yellow", "black", "white", "gray"]

Exercise: Replace index 2 with "purple"; replace indices 1–3 with ["pink","cyan"];
replace index 1 with ["mint","navy"]; insert "olive" at index 2. Return a new list.
"""


def change_items(colors: list) -> list:
    """Apply single index, slice replace, and insert. Return a new list."""
    pass


def main() -> None:
    colors = ["red", "blue", "green", "yellow", "black", "white", "gray"]
    print("colors =", colors)
    print("change_items(colors) =", change_items(colors))
    print("colors unchanged =", colors)


if __name__ == "__main__":
    main()
