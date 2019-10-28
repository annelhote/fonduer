from fonduer.parser.lingual_parser import SimpleParser


def test_simple_parser_support():
    lingual_parser = SimpleParser()
    assert lingual_parser.has_tokenizer_support()
    assert not lingual_parser.has_NLP_support()


def test_simple_split_sentences():
    tokenize_and_split_sentences = SimpleParser().split_sentences
    text = "This is a text.<NB>This is another text."

    iterator = tokenize_and_split_sentences(text)
    assert len(list(iterator)) == 2
