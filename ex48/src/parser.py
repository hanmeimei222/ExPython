class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, obj):
        # we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


class Util(object):
    #  peek at a list of words and return what type of word it is
    @staticmethod
    def peek(word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None

    # confirms the expected word is the right type
    # takes it off the list and returns the word
    @staticmethod
    def match(word_list, expecting):
        if word_list:
            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None


    # skip words that aren't useful to the Sentence
    @staticmethod
    def skip(word_list, word_type):
        while Util.peek(word_list) == word_type:
            Util.match(word_list, word_type)

class Parse(object):
    def parse_verb(self, word_list):
        Util.skip(word_list, 'stop')

        if Util.peek(word_list) == 'verb':
            return Util.match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next.")


    def parse_object(self, word_list):
        Util.skip(word_list, 'stop')
        next_word = Util.peek(word_list)

        if next_word == 'noun':
            return Util.match(word_list, 'noun')
        elif next_word == 'direction':
            return Util.match(word_list, 'direction')
        elif next_word == 'number':
            return Util.match(word_list, 'number')
        else:
            raise ParserError("Expected a noun or direction next.")


    def parse_subject(self, word_list):
        Util.skip(word_list, 'stop')
        next_word = Util.peek(word_list)

        if next_word == 'noun':
            return Util.match(word_list, 'noun')
        elif next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected a verb next.")


    def parse_sentence(self, word_list):
        subj = self.parse_subject(word_list)
        verb = self.parse_verb(word_list)
        obj = self.parse_object(word_list)

        return Sentence(subj, verb, obj)
