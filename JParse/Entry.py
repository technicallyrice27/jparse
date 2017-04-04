# -*- coding: utf-8 -*-
import re

class Entry:
    """"
    Entry describes an entry from the dictionary.
    Requires word (in Japanese) to be passed during creation.
    Populates following variables with information:
        word = original word (REQUIRED)
        reading = full reading including ending (ex: 食べる and たべる) 
        furigana = furigana for the kanji only (or None when word is full kana)
        kanji_stem = only the kanji, no extra kana (ex: 食べる is just 食)
    """
    # Look up entry in dictionary and populate class variables with information
    def __init__(self, word, reading=None):
        self.word = word
        self.furigana = self._furi(reading)
        self.kanji_stem = self._kanji(word)

    # Method to lookup a word in the dictionary
    def lookup(self, word):
        # Connect to DB
        # Get entry
        # Parse into variables
        # Check if furigana exists, or look it up if needed. Either way, compare
        if not self.furigana:
            pass

    # Outputs string as: Word (Furigana) {Properties} [Definitions]
    def __str__(self):
        # set properties variable as , separated string here
        #properties =
        return "{word} ({furigana}) {{properties}} [{definitions}]"

    def _furi(self, reading):
        if reading:
            same = ''.join(set(self.word) & set(reading))
            furi = re.sub(same, '', reading)
            return furi
        else:
            return None

    def _kanji(self, word):
        pass
