def n_dice_prob(n):
    """
    Returns the probability of rolling at most a 5 on n fair six sided dice.
    """
    return (5 / 6) ** n - (4 / 6) ** n


for n in range(1, 100):
    print(f"n = {n}, P(roll at most 5) = {n_dice_prob(n)}")
