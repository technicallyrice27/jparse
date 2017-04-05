# -*- coding: utf-8 -*-
import re

class Entry:
    """"
    Entry describes an entry from the dictionary.
    Requires word (in Japanese) to be passed during creation.
    Populates following variables with information:
        word = original word (REQUIRED)
        reading = full reading including ending (ex: 食べる and たべる)
            - When reading == None it is a kana word
        furigana = word with furigana in form: kanji (furigana) other kana
        kanji_stem = only the kanji, no extra kana (ex: 食べる is just 食)
    """
    part_of_speech = None
    definitions = None
    first_hira = 12353
    last_kata = 12534

    # Look up entry in dictionary and populate class variables with information
    def __init__(self, word, reading=None):
        self.word = word
        self.reading = reading
        self.furigana = self._furi(reading)
        self.kanji_stem = self._kanji(word)

    # Outputs string as: Word(Furigana){Properties}[Definitions]
    def __str__(self):
        # set properties variable as , separated string here
        #properties =
        if self.furigana:
            return f"{furigana}{{properties}}[{definitions}]"
        else:
            return f"{word} {{properties}} [{definitions}]"

    def _furi(self, reading):
        if reading:
            if reading == self.word:
                return None  # it's a kana word
            if not (set(self.word) & set(reading)):
                return f"{self.word}({reading})"
            furi = []
            counter = 0
            i = 0
            while i < len(reading):
                if self.word[i-counter] != reading[i]:
                    j = i
                    while not self.first_hira <= ord(self.word[j-counter]) <= self.last_kata:
                        furi.append(self.word[j-counter])
                        j = j + 1
                    furi.append('(')
                    furi.append(reading[i])
                    i = i + 1
                    while self.word[i-counter] != reading[i]:
                        furi.append(reading[i])
                        counter = counter + 1
                        if counter >= j:
                            counter = counter - (j-1)
                        i = i + 1
                    furi.append(')')
                    furi.append(reading[i])
                else:
                    furi.append(reading[i])
                i = i + 1
            return ''.join(furi)
        else:
            return None

    def _kanji(self, word):
        kanji = ''
        kana = ''
        for c in word:
            if self.first_hira <= ord(c) <= self.last_kata:
                kana = kana + c
            else:
                kanji = kanji + c
        if len(kanji) > 1:
            return word.split(kanji[0],1)[-1].split(kanji[-1])[0]
        else:
            return kanji
