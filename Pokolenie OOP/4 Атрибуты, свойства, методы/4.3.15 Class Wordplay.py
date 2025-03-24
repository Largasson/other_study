import copy


class Wordplay:
    def __init__(self, words=None):
        if words is None:
            words = []
        self.words = words.copy()

    def add_word(self, word):
        if not {word}.issubset(set(self.words)):
            self.words.append(word)

    def words_with_length(self, n):
        return [word for word in self.words if len(word) == n]

    def only(self, *args):
        return [word for word in self.words if
                set(args).issubset(set(word)) and set(word).issubset(set(args)) or word in args]
#   return [w for w in self.words if set(w) <= set(args)] # лучшее
    def avoid(self, *args):
        return [word for word in self.words if set(args).isdisjoint(set(word))]



print('TEST_1')
wordplay = Wordplay()

print(wordplay.words_with_length(1))
print(wordplay.only('a', 'b', 'c'))
print(wordplay.avoid('a', 'b', 'c'))

print('TEST_2')
wordplay = Wordplay()

print(wordplay.words)
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)

print('TEST_3')
wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])

wordplay.add_word('python')
print(wordplay.words_with_length(4))


print('TEST_4')

wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))


print('TEST_5')
wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.avoid('a', 'b', 'c'))

print('TEST_6')
wordplay = Wordplay()
print(wordplay.words)

print('TEST_7')
wordplay = Wordplay(['Тьюринг', 'Торвальдс', 'Россум', 'Гейтс', 'Гамильтон', 'Бэкус', 'Кнут'])

print(wordplay.words_with_length(6))
print(wordplay.avoid('ь'))

print('TEST_8')
words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)

print('TEST_9')
wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.words)
wordplay.add_word('stepik')
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)

