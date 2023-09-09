def climbingLeaderboard(ranked, player):
    # Step 1: Create a unique ranked leaderboard
    unique_ranked = [ranked[0]]
    for score in ranked:
        if score != unique_ranked[-1]:
            unique_ranked.append(score)

    # Step 2: Initialize a list to store player ranks
    player_ranks = []

    # Step 3: Iterate through the player's scores
    for player_score in player:
        while unique_ranked and player_score >= unique_ranked[-1]:
            unique_ranked.pop()
        player_ranks.append(len(unique_ranked) + 1)

    return player_ranks
