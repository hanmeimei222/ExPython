from nose.tools import *
from src.ex48 import lexicon
from src.parser import *


def test_parse_sentence_1():
    word_list = lexicon.scan("run north")
    result = parse_sentence(word_list)
    sub = result.subject
    verb = result.verb
    obj = result.object
    assert_equal(sub, 'player')
    assert_equal(verb, 'run')
    assert_equal(obj, 'north')


def test_parse_sentence_2():
    result = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    sub = result.subject
    verb = result.verb
    obj = result.object
    assert_equal(sub, 'bear')
    assert_equal(verb, 'eat')
    assert_equal(obj, 'honey')


def test_parser_error():
    assert_raises(ParserError, parse_verb, [('noun', 'honey'), ('stop', 'the'), ('verb', 'eat')])
    assert_raises(ParserError, parse_object, [('stop', 'at'), ('verb', 'eat')])
    assert_raises(ParserError, parse_subject, [('stop', 'the'), ('direction', 'south')])
    assert_raises(ParserError, parse_sentence, [('noun', 'bear'), ('noun', 'honey'), ('stop', 'the'), ('noun', 'honey')])
