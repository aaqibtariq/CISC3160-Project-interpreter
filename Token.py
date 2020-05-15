# token is used to indicate that
# there is no more input left for lexical analysis
(INTEGER, PLUS, MINUS, MUL, LPAREN, RPAREN, ID, ASSIGN,
SEMI, EOF) = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL','(', ')', 'ID', 'ASSIGN',
    'SEMI', 'EOF'
)

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):

        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


