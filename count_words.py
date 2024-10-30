# count_words.py

class CountWords:
    def count(self, s: str) -> int:
        words = 0
        last = ' '

        for char in s:
            if not char.isalpha() and (last.lower() == 's' or last.lower() == 'r'):
                words += 1
            last = char

        if last.lower() == 'r' or last.lower() == 's':
            words += 1

        return words