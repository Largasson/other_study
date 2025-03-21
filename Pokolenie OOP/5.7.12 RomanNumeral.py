from functools import total_ordering


@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.roman_num = number

    def __repr__(self):
        return self.roman_num

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.roman_num == other.roman_num
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral.roman_to_arabic(self.roman_num) < RomanNumeral.roman_to_arabic(other.roman_num)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
           sum_arabic = RomanNumeral.arabic_to_roman(RomanNumeral.roman_to_arabic(self.roman_num) + RomanNumeral.roman_to_arabic(other.roman_num))
           return RomanNumeral(sum_arabic)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
           sub_arabic = RomanNumeral.arabic_to_roman(RomanNumeral.roman_to_arabic(self.roman_num) - RomanNumeral.roman_to_arabic(other.roman_num))
           return RomanNumeral(sub_arabic)
        return NotImplemented

    def __int__(self):
        return RomanNumeral.roman_to_arabic(self.roman_num)


    @staticmethod
    def roman_to_arabic(roman_num):
        rule_add = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        rule_div = {
            ('I', 'V'): 3,
            ('I', 'X'): 8,
            ('X', 'L'): 30,
            ('X', 'C'): 80,
            ('C', 'D'): 300,
            ('C', 'M'): 800,
        }
        arabic_num = 0
        prev_literal = None
        for literal in roman_num:
            if prev_literal and rule_add[prev_literal] < rule_add[literal]:
                arabic_num += rule_div[(prev_literal, literal)]
            else:
                arabic_num += rule_add[literal]
            prev_literal = literal
        return arabic_num

    @staticmethod
    def arabic_to_roman(arabic_num):
        roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                         'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                         'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        roman_num = ''
        for letter, value in roman_numbers.items():
            while arabic_num >= value:
                roman_num += letter
                arabic_num -= value
        return roman_num



