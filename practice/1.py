def get_distance(key_pad, hand_coord):
    key_pad_y, key_pad_x = divmod(key_pad-1, 3)
    hand_coord_y, hand_coord_x = divmod(hand_coord-1, 3)
    
    distance = abs(key_pad_y - hand_coord_y) + abs(key_pad_x - hand_coord_x)
    
    return distance

def solution(numbers, hand):
    answer = ''
    lh = 10
    rh = 12
    #거리관련 알고리즘이라....
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            lh = i
        elif  i in [3,6,9]:
            answer += 'R'
            rh = i 
        else:
            key_to_right = get_distance(i,rh)
            key_to_left = get_distance(i,lh)
            
            if key_to_right < key_to_left:
                answer += 'R'
                rh = i 
            elif key_to_right > key_to_left:
                answer += 'L'
                lh = i
            else: 
                if hand == 'left':
                    answer += 'L'
                    lh = i 
                else:
                    answer += 'R'
                    rh = i 
    print (answer)
    return answer

number = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"
k=solution(number,hand)