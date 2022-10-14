def solution(participant, completion):
    answer = ''
    particpant_dict={}
    for player in participant:
        particpant_dict[player]=particpant_dict.get(player, 0)+1
    for complete in completion:
        particpant_dict[complete] -= 1
    for player, complete in particpant_dict.items():
        if complete:
            answer+=player
    return answer