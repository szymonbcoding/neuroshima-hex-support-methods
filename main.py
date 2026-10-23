def probability_counter(how_many_tokens_meet_reqs: int, how_many_tokens_in_pot: int = 34, how_many_tokens_to_draw: int = 3) -> float:

    how_many_tokens_not_meet_reqs = how_many_tokens_in_pot - how_many_tokens_meet_reqs

    probability_not_to_meet_reqs = 1

    for draw_no in range(how_many_tokens_to_draw):
        probability_not_to_meet_reqs *= how_many_tokens_not_meet_reqs/(how_many_tokens_in_pot - draw_no)
    
    probability_not_to_meet_reqs = round(probability_not_to_meet_reqs * 100, 1)
    propability_to_meet_reqs = round(100 - probability_not_to_meet_reqs, 1)
    
    print(f"{probability_not_to_meet_reqs=}")
    print(f"{propability_to_meet_reqs=}")

probability_counter(4, 34, 3)

    
