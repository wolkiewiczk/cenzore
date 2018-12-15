from dictionaries_loader import DictionaryLoader


class StringUtils(DictionaryLoader):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # list with a common letters replacements
        self.special_characters = {
            '1': 'i',
            '3': 'e',
            '4': 'a',
            'q': 'k',
            '0': 'o',
            'f': 'w',
            '8': 'b',
            '@': 'a',
            '$': 's'
        }

    def refactor(self, word):

        """Modify word parameter to trim whitespace, replace all characters in spacial_characters list and remove
        whitespaces and non-letters. Returns modified word.
        """

        if type(word) not in [str]:
            raise ValueError("The 'word' parameter needs to be str type")
        if len(word) == 0:
            raise ValueError("Given str must not be empty")

        word = word.replace(" ", "").lower()
        wordlist = list(word)
        index = 0
        last_letter = wordlist[0]

        for lt in word:
            if lt in self.special_characters:
                wordlist[index] = self.special_characters.get(lt)

            if (last_letter == wordlist[index] and index != 0) \
                    or ord(wordlist[index]) < 65 or ord(wordlist[index]) > 122 \
                    or 97 > ord(wordlist[index]) > 90:
                del wordlist[index]
                continue

            last_letter = wordlist[index]
            index += 1
        word = "".join(wordlist)
        return word

    @staticmethod
    def compare(word1, word2):
        """Calculates distance between 2 strings given. See Levenshtein algorithm"""

        if type(word1) not in [str] or type(word2) not in [str]:
            raise ValueError("The 'word1' and 'word2' parameters need to be str type")
        if len(word1) == 0 or len(word2) == 0:
            raise ValueError("Given str must not be empty")

        len1 = len(word1)
        len2 = len(word2)
        table = [[0] * (len1 + 1) for i in range(len2+1)]

        for i in range(len2+1):
            table[i][0] = i

        for i in range(len1+1):
            table[0][i] = i

        for i in range(1, len2+1):
            for j in range(1, len1+1):
                if word1[j-1] != word2[i-1]:
                    cost = 1
                else:
                    cost = 0
                table[i][j] = min(table[i][j-1]+1, table[i-1][j]+1, table[i-1][j-1]+cost)

        return table[len2][len1]

    def binary_search_by_distance(self, word, dictionary, max_distance=1):
        """Searches if given word exists in a list called dictionary.
         Maximum differ of words is set by max_distance parameter.
         """

        if type(word) not in [str]:
            raise ValueError("Word parameter must be str")
        if len(word) == 0:
            raise ValueError("Given str must not be empty")
        if type(dictionary) not in [list, dict]:
            raise ValueError("Dictionary parameter must be a list")
        if len(dictionary) == 0:
            raise ValueError("Given list must not be empty")
        if type(max_distance) not in [int] or max_distance < 0:
            raise ValueError("Max_distance must be a non-negative int")

        if type(dictionary) in [dict]:
            keys = [*dictionary]
        else:
            keys = dictionary

        first_index = 0
        last_index = len(keys) - 1
        current_index = (last_index - first_index) // 2 + first_index

        while self.compare(word, keys[current_index]) > max_distance and first_index != last_index - 1:

            if word < keys[current_index]:
                last_index = current_index
                current_index = (last_index - first_index) // 2 + first_index
            elif word > keys[current_index]:
                first_index = current_index
                current_index = (last_index - first_index) // 2 + first_index

        if first_index == last_index - 1:
            if self.compare(word, keys[first_index]) <= max_distance \
                    or self.compare(word, keys[last_index]) <= max_distance:
                return keys[current_index]
            return False
        return keys[current_index]
