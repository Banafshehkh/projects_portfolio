import random

def monty_hall_problem(switch_doors: bool) -> bool:
    """Simulation of the monty hall problem

    Args:
        switch_doors (bool): If true, the contestant will switch their choice.

    Returns:
        bool: True if the contenstant wins the car, False otherwise.
    """

    doors = ["car", "goat", "goat"]
    random.shuffle(doors)

    # select a door randomly
    initial_choice = random.choice(range(3))

    # Monty reveals a door with a goat
    revealed_doors = [i for i in range(3) if i != initial_choice and doors[i] == 'goat']
    revealed_door = random.choice(revealed_doors)


    # If contestant decides to switch, their final choice is the remaining door
    if switch_doors:
        final_choice = [i for i in range(3) if i != initial_choice and i != revealed_door][0]
    else:
        # Keep the initial choice
        final_choice = initial_choice

    # Return if contestant won the car
    return doors[final_choice] == 'car'


def simulate_games(num_games: int = 1000) -> None:
    """Simulate a number of monty hall game and prints the number of wins

    Args:
        num_games (int, optional): the number of simulations. Defaults to 1000.

    Returns:
        : None
    """

    # Simulate games where contestant keeps and switches doors
    num_wins_without_switching = sum(monty_hall_problem(switch_doors=False) for _ in range(num_games))
    num_wins_with_switching = sum(monty_hall_problem(switch_doors=True) for _ in range(num_games))

    return num_wins_without_switching, num_wins_with_switching


if __name__ == "__main__":
    num_games = 1000
    num_wins_without_switching, num_wins_with_switching = simulate_games(num_games)
    print(f"Winning percentage without switching doors: {(num_wins_without_switching/num_games):.2%}")
    print(f"Winning percentage with    switching doors: {(num_wins_with_switching/num_games):.2%}")