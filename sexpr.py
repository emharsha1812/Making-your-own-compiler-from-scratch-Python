#First step is to parse the source code into tree structures
#Parsing is the boring part
#But S-expressions can be parsed with minimal efforts

#A sexpr is either a nested list or an indivisible element called 'atom'

#To parse an sexpr the first step is to determine whether its an atom or a list, this is done  by looking at the first non-whitespace character

def parse_expr(s:str, idx:int):
    idx=skip_space(s,idx)
    if s[idx]='(':
        # its a list
    
    elif s[idx]==')':
        raise Exception('bad brackets')
    else:
        #an atom
    