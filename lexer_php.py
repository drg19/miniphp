import ply.lex as lex
import sys

# list of tokens
tokens = (
    # Reserverd words 
    'abstract', 
    'and', 
    'array',
 	'as', 
 	'break', 
 	'case',
 	'STRING',
  	'const',  
  	'do', 
  	'echo', 
  	'else', 
  	'elseif', 
  	'empty', 
  	'for',  
  	'function', 
  	'global', 
    'if', 
   'include',
    'list',
 	'namespace',
  	'new', 
  	'or', 
    'print', 
    'return', 
    'try',
    'use', 
    'while',
    'strpos',

    #--------------
    'start_php',
    'end_php', 
    #------------

    # Symbols
    'PLUS',
    #'PLUSEQUAL',
    'MINUS',
    #'MINUSEQUAL',
    'Backslash',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
 	'DECLARATE',

   
    # Others   
    'ID', 
    'NUMBER',
)

# Regular expressions rules for a simple tokens 
#t_PLUS   = r'\+'
#t_MINUS  = r'-'
t_Backslash  = r'\\'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_DECLARATE = r'\$'





def t_AND(t):
    r'and'
    return t

def t_strpos(t):
    r'strpos'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_array(t):
    r'array'
    return t

def t_CASE(t):
    r'case'
    return t

def t_const(t):
    r'const'
    return t

def t_do(t):
    r'do'
    return t

def t_while(t):
    r'while'
    return t

def t_use(t):
    r'use'
    return t

def t_var(t):
    r'var'
    return t


def t_as(t):
    r'as'
    return t


def t_echo(t):
    r'echo'
    return t

def t_else(t):
    r'else'
    return t

def t_elseif(t):
    r'elseif'
    return t

def t_empty(t):
    r'empty'
    return t

def t_for(t):
    r'for'
    return t

def t_if(t):
    r'if'
    return t

def t_function(t):
    r'function'
    return t

def t_global(t):
    r'global'
    return t

def t_include(t):
    r'imclude'
    return t

def t_list(t):
	r'list'
	return t

def t_newspace(t):
    r'newspace'
    return t

def t_new(t):
    r'new'
    return t

def t_or(t):
	r'or'
	return t

def t_print(t):
    r'print'
    return t

def t_private(t):
	r'private'
	return t
	
def t_return(t):
	r'return'
	return t

def t_try(t):
    r'try'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_STRING(t):
	r'(\" | \')(.|\n)*?(\' | \")'
	r'\'(.|\n)*?\''
	##t.value= Char(t.value)
	##t.lexer.lineno += 1
	return t

def t_start_php(t):
	r'\<\?php'
	return t

def t_end_php(t):
	r'\?\>'
	return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
    
def t_MINUS(t):
	r'-'
	return t

def t_PLUS(t):
	r'\+'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_comments_C9(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1


def t_end(t):
    r'\?\>'

       

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'test.txt'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()

