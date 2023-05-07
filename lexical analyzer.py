import ply.lex as lex
import ply.yacc as yacc

# Define the token types
tokens = (
    'NAME', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN'
)

# Define the token regular expressions
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER  = r'\d+'

# Define the token handling functions
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Define the parsing rules
def p_statement_assign(p):
    'statement : NAME EQUALS expression'
    p[0] = ('assign', p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_name(p):
    'expression : NAME'
    p[0] = ('name', p[1])

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Run the compiler on the input program
while True:
    try:
        s = input('>>> ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s, lexer=lexer)
    print(result)
