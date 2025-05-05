from abc import ABC, abstractmethod
import textwrap


class Paragraph(ABC):
    def __init__(self, length):
        self._length = length
        self._words = []

    def add(self, text):
        self._words.extend(text.split())

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def end(self):
        text = ' '.join(self._words)
        wrapped_text = textwrap.wrap(text, width=self._length)
        for line in wrapped_text:
            print(line)
        self._words.clear()


class RightParagraph(Paragraph):
    def end(self):
        text = ' '.join(self._words)
        wrapped_text = textwrap.wrap(text, width=self._length)
        for line in wrapped_text:
            print(line.rjust(self._length))
        self._words.clear()


leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()

rightparagraph = RightParagraph(10)

rightparagraph.add('death')
rightparagraph.add('can have me')
rightparagraph.add('when it earns me')
rightparagraph.end()
