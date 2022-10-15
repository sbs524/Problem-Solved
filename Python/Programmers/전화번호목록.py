def solution(phone_book):
    answer = True
    
    numbers = {}
    
    for number in phone_book:
        numbers[number] = 1
    
    for number in phone_book:
        temp=''
        for n in number:
            temp+=n
            if temp in numbers and temp!=number:
                return False
    
    return answer