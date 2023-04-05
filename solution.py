
## A list of tuple, (1)


"""
Problem type: 
    Converting problem

The gist of the problem:
    Convert positive integer to roman string
    E.g.
        3 -> "III"
        58 -> "LVIII" as L = 50, V = 5, III = 3

Input range:
    1 <= integer <= 3999

Concerned target:   
     Individual positive integer number
    E.g.
        If 10201, then we will focus on 1, 0, 2, 0, 1 consecutively

Goal:
    Correctly covert every number to corresponding roman character

What we have known:
    1. For any symbol and their value, their differences are just how many 0 follow behind
       E.g.
            V = 5, L = 50
            C = 100, M = 1000
    2. So we need to know for each number, how many their zeros are followed behind
       E.g.
            111 -> 1 is followed by 2 zero(100) + 1 is followed by 1 zero(10) + 1 is followed by 0 zero(1)
    3. Regardless the zeros, when a number is less than 4, and it's roman is just it's "1" symbol and repeating times
       E.g.
            3 -> I * 3 = III
            200 -> C * 2 = CC
    4. Regardless the zeros, when a number is 4, then it's roman is it's "1" symbol +  "5" symbol
       E.g.
            4 -> I + V = IV
            400 -> C + D = CD
    5. Regardless the zeros, when a number is 9, then it's roman is it's "1" symbol +  "10" symbol    
       E.g.
            9 -> I + X = IX
            90 -> X + C = XC    
    6. Regardless the zeros, when a number is 5, it's just it's corresponding roman

    7. Regardless the zeros, when a number is 5 < n < 9, it's just it's "5" symbol + "1" symbol * repeats

Conclusion:
    We can create a dictionary with number as the key and roman as the corresponding value
    When we determine the number's cases(n < 4,5 < n < 9, n = 0, n = 4 or 9, )
    Just plug in their keys and get the values


Must do in order to achieve the goal:
    1. We can create a dictionary with number as the key and roman as the corresponding value

    2. The dictionary has to include the "0" as key and the corresponding value is empty string

    3. Need to know for every number, how many zeros are followed
        E.g.
            If it's 123, then you must know it's 1 * 10^2 + 2 * 10^1 + 3 * 10^0

    4. When ignoring the zeros, there are 2 cases:
            a. The number is 0, 1, 2, 3, or 5, 6, 7, 8 -> "1" symbol * repeat or "5" symbol + "1" symbol * repeat
                when the case is "0" or "5", the repeat times is 0, which means no zero repeats
            b. The number is 4 or 9, meaning the number mod 5 is 4 or 9

"""

"""
-------------Definitions--------------

ROMAN_DICT: Dict           // The dictionary
number: Int                // The raw input number
number_string: String      // The stringified raw input number
roman: String              // The final roman string we want to get

n: Int                     // The individual number of the input raw number 
digits: Int                // How many digits the individual number has 
repeat: Int                // What the remainder of the number 
symbol: Char               // The converted individual number to roman


convert(n, digits, repeat):
    IF 
        remainder_is_four(n) -> // Means the number is 4 or 9
            IF
                 is_greater_than_four(n) -> n := 10
                ¬is_greater_than_four(n) -> n := 5
            FI;
            symbol := ROMAN_DICT[digits] + ROMAN_DICT[n * digits] // The "1" + "5" (or "10") symbol
        
       ¬remainder_is_four(n) -> // Means the number is 0, 1, 2, 3 or 5, 6, 7, 8   
            IF
                 is_greater_than_four(n) -> n := 5 
                ¬is_greater_than_four(n) -> n := 0
            FI;
            symbol := ROMAN_DICT[n * digits] + ROMAN_DICT[digits] * repeat  
                                                                 // "5" symbol(or none) + repeated "1" symbol(or none)           
    FI  
---------------Steps-------------------

number_string := toString(number)
roman := ""
power := length(number_string) - 1
l := length(number_string)
i := 0

Loop condition                  Loop invariant 
{ i ≠ l   ∧   roman = ( sΣn | 0 ≤ n < i: symbol )} 

   
for c in number_string:
    n := int(c);
    digits := 10 ^ power;
    repeat := n mod 5;
    convert(n, digits, repeat);
    i := i + 1
    power := power - 1

{  i = l ∧  roman = ( sΣn | 0 ≤ n < i: symbol ) }

--------------------------------------

Complexity: Θ(n)

"""


ROMAN_DICT = {
                 1: "I", 5: "V",
                10: "X", 50: "L",
               100: "C", 500: "D",
              1000: "M", 0: ""
                       }


def solution(n):
    return n_to_roman(n)


def n_to_roman(n):
    n_str = str(n)
    pow = len(n_str) - 1  # Determine how many zeros
    roman = ""

    for digit in n_str:
        d = int(digit)
        digits = 10 ** pow
        remainder = d % 5
        is_gtr_five = (d - 5) >= 0
        if remainder == 4:
            # d = 4 or 9 -> break it to 1 + 5 or 1 + 10
            # Must start with 1
            roman += ROMAN_DICT[digits] + ROMAN_DICT[(10 if is_gtr_five else 5) * digits]
        else:
            # d = 0, 1, 2, 3 or 5, 6, 7, 8
            # n = 5, 6, 7, 8 -> break it to 5 + 1 * repeat
            roman += ROMAN_DICT[(5 if is_gtr_five else 0) * digits] + ROMAN_DICT[digits] * remainder

        pow -= 1

    return roman



# print(solution(3))
# print(solution(58))
print(solution(1994))
print(solution(101))
print(solution(10))

