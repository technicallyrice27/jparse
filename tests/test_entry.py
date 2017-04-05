from JParse.Entry import Entry

class TestEntry:
    def test_furi_full_kanji(self):
        e = Entry('言葉','ことば')
        assert(e.furigana == "言葉(ことば)")

    def test_furi_kanji_and_hira(self):
        e = Entry('言葉遣い','ことばづかい')
        assert(e.furigana == "言葉遣(ことばづか)い")

    def test_furi_mixed_hira(self):
        e = Entry('取り戻す','とりもどす')
        assert(e.furigana == "取(と)り戻(もど)す")

    def test_all_hira(self):
        e = Entry('なぜなら','なぜなら')
        assert(e.furigana == None)

    def test_all_hira_no_reading(self):
        e = Entry('なぜなら')
        assert(e.furigana == None)