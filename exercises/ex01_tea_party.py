"""Planning a cozy tea party using functions!"""


__author__: str = "730824450"


def main_planner(guests: int) -> None:
    """comprehensive function for planning a tea party based on the number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))))


def tea_bags(people: int) -> int:
    """how many tea bags are needed based on the number of guests"""
    return people * 2


def treats(people:int) -> int:
    """how many treats are needed based on the number of guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """the cost of the tea bags and the treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))