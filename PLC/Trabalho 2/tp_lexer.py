import ply.lex as lex

literals = ['%', '*', '+', '/', '-', '=',
            '(', ')', '.', '<', '>', ',', '{', '}', '[', ']']

tokens = ['INT', 'ID', 'STR', 'NUM',
          'MAIN', 'PRINT', 'READ',
          'IF', 'ELSE',
          'EQUALS', 'GREATERQ', 'LESSERQ',
          'WHILE', 'DO',
          'AND', 'OR', 'NOT']

def t_INT(t):
    r'int'
    return t

def t_STR(t):
    r'"[^"]+"'
    return t

def t_NUM(t):
    r'-?\d+'
    return t

def t_MAIN(t):
    r'Main'
    return t

def t_PRINT(t):
    r'Print'
    return t

def t_READ(t):
    r'Read'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_EQUALS(t):
    r'=='
    return t

def t_GREATERQ(t):
    r'>='
    return t

def t_LESSERQ(t):
    r'<='
    return t

def t_WHILE(t):
    r'While'
    return t

def t_DO(t):
    r'Do'
    return t

def t_AND(t):
    r'AND'
    return t

def t_OR(t):
    r'OR'
    return t

def t_NOT(t):
    r'!'
    return t

def t_ID(t):
    r'\w+'
    return t

t_ignore = " \t\n"

def t_error(t):
    print('Illegal character: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

