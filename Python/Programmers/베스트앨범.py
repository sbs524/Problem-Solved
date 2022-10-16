def solution(genres, plays):
    answer = []
    gen_dict={}
    
    for i in range(len(genres)):
        gen_dict[genres[i]]=gen_dict.get(genres[i], 0)+plays[i]
    
    
    for i in range(len(gen_dict)):
        max=0
        genre_val=''
        for genre, play in gen_dict.items():
            if max<play:
                max=play
                genre_val=genre
        gen_dict[genre_val]=0
        
        
        for j in range(2):
            max=0
            genre_index=0
            for k in range(len(genres)):
                if genre_val==genres[k] and max<plays[k]:
                    max=plays[k]
                    genre_index=k
            if max:
                answer.append(genre_index)
                plays[genre_index]=0
            
        
                    
    
    return answer