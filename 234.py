from typing import Iterator


def phone_number(phone: str) -> bool:
    groups = phone.split('-')
    if phone.startswith('7') and len(groups) == 5 and len(groups[1]) == 3 and len(groups[2]) == 3 and len(
            groups[3]) == 2 and len(groups[4]) == 2:
        chars = ''.join(groups)
        return all(c.isdigit() for c in chars)
    elif phone.startswith('8') and len(groups) == 4 and len(groups[1]) == 3 and len(groups[2]) == 4 and len(
            groups[3]) == 4:
        chars = ''.join(groups)
        return all(c.isdigit() for c in chars)
    return False


def get_all_numbers(text: str) -> Iterator:
    for c in range(len(text)):
        chunk = text[c:(c + 15)]
        if phone_number(chunk):
            yield chunk


if __name__ == '__main__':
    string = input()
    print(*get_all_numbers(string), sep='\n')
