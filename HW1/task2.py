text = """
Вчера Анна и Артем гуляли в парке. Анна заметила слово level на
старом плакате. Рядом кто-то написал radar, а чуть дальше было
нарисовано слово kayak. На скамейке сидел человек с книгой civic,
а возле фонтана дети мелом написали refer. Остальные слова в тексте
палиндромами не являются.
"""

text = text.lower()
words = text.split()
punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~"
palindromes = []

for i in range(len(words)):
    word = words[i].strip(punct)
    if word == word[::-1] and len(word) >= 2 and palindromes.count(word) == 0:  # palindromes.count(word) == 0 - чтобы убрать повторы слов
        palindromes.append(word)


print(palindromes)
