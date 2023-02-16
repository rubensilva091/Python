import ply.yacc as yacc
import sys
from tp_lexer import tokens


def p_program(p):
    "program : '{' MAIN body '}' "
    p[0] = p[3]
# criação do programa {main ... }


def p_body(p):
    "body : declarations commands"
    p[0] = p[1] + 'START\n' + p[2] + 'STOP'
# corpo do programa contém declarações e comandos a realizar

# region DECLARATIONS FUNCTIONS


def p_empty_declarations(p):
    "declarations : "
    p[0] = ""
# sem declarações


def p_declarations(p):
    "declarations : declaration declarations"
    p[0] = p[1] + p[2]
# especificação de declarações.... uma ou mais declarações


def p_int_declaration(p):
    "declaration : INT ID"
    if p[2] in parser.variables:
        parser.success = False
        print("Multiple variable declaration " + p[2])
        sys.exit(0)
    else:
        parser.variables[p[2]] = parser.count
        p[0] = 'PUSHI 0\n'
        parser.count += 1
# declaração de um inteiro sem valor || int ID


def p_int_num_declaration(p):
    "declaration : INT ID '=' NUM"
    if p[2] in parser.variables:
        parser.success = False
        print("Multiple variable declaration " + p[2])
        sys.exit(0)
    else:
        parser.variables[p[2]] = parser.count
        p[0] = "PUSHI "+str(p[4])+"\n"
        parser.count += 1
# declaração de int id com um certo valor || ex: int num1 = 4

# endregion

# region ALL COMMANDS FUNCTIONS


def p_empty_commands(p):
    "commands : "
    p[0] = ""
# sem comandos


def p_commands(p):
    "commands : command commands"
    p[0] = p[1]+p[2]
# especificação dos comandos 1 ou mais a realizar

# region PRINT COMMAND FUNCTIONS


def p_print_command(p):
    "command : cmd_prints"
    p[0] = p[1]
# especificação do cmd_print (será desenvolvido as várias alternativas de print)


def p_cmd_prints_all(p):
    "cmd_prints : PRINT '(' cmd_print prints ')' "
    p[0] = str(p[3])+str(p[4])
# cmd_print função geral


def p_cmd_prints(p):
    "prints : '+' cmd_print prints "
    p[0] = p[2] + p[3]
# desenvolvimento de cmd_print


def p_empty_cmd_prints(p):
    "prints :"
    p[0] = ""
# cmd_print vazio


def p_print_id_command(p):
    "cmd_print : Id"
    p[0] = p[1][1]+"WRITEI\n"
# comando para dar print a um Id


def p_print_str_command(p):
    "cmd_print : STR"
    p[0] = "PUSHS " + p[1] + "\n" + "WRITES\n"
# comando para dar print a uma STR

# endregion

# region READ COMMAND FUNCTIONS


def p_read_command(p):
    "command : cmd_read"
    p[0] = p[1]


def p_read_id_command(p):
    "cmd_read : READ Id"
    p[0] = "READ\nATOI\n" + p[2][0]


# endregion

# region IF COMMAND // IF ELSE COMMAND FUNCTIONS


def p_if_command(p):
    "command : cmd_if"
    p[0] = p[1]


def p_cmd_if(p):
    "cmd_if : IF condition '{' commands '}'"
    p[0] = str(p[2])+"JZ IF" + str(parser.label) + "\n" + \
        str(p[4])+"IF"+str(parser.label)+":\n"

    parser.label += 1


def p_if_else_command(p):
    "command : cmd_if_else"
    p[0] = p[1]


def p_cmd_if_else(p):
    "cmd_if_else : IF condition '{' commands '}' ELSE '{' commands '}'"
    p[0] = p[2] + "JZ IF" + str(parser.label)+"\n"+p[4]+"JUMP IFEND" + str(
        parser.label) + "\nIF" + str(parser.label) + ":\n"+p[8]+"IFEND"+str(parser.label)+":\n"
    parser.label += 1


# endregion

def p_atribution_command(p):
    "command : attribution"
    p[0] = p[1]


def p_cmd_atb(p):
    "attribution : Id '=' exp"
    p[0] = p[3] + p[1][0]
# igualdade de um Id para uma expressão || resultado = num1 + num2 || resultado = num1 - 2 etc..

# region WHILE DO FUNCTIONS


def p_do_while_command(p):
    "command : cmd_while"
    p[0] = p[1]


def p_cmd_while(p):
    "cmd_while : WHILE condition DO '{' commands '}'"
    p[0] = "WHILE" + str(parser.loop)+":\n" + p[2] + "JZ ENDWHILE"+str(parser.loop) + \
        "\n"+p[5] + "JUMP WHILE"+str(parser.loop) + \
        "\n"+"ENDWHILE"+str(parser.loop)+":\n"
    parser.loop += 1

# endregion

# endregion


# region CONDITIONS FUNCTIONS

def p_condition(p):
    "condition : '(' context ')'"
    p[0] = p[2]


def p_condition_Neg(p):
    "condition : NOT '(' context ')'"
    p[0] = str(p[3])+"NOT\n"


def p_condition_AND(p):
    "condition : condition AND condition"
    p[0] = str(p[1])+str(p[3]) + "MUL\n"


def p_condition_OR(p):
    "condition : condition OR condition"
    p[0] = str(p[1])+str(p[3]) + "ADD\n"


def p_condition_EQUALS(p):
    "context : exp EQUALS exp"
    p[0] = str(p[1])+str(p[3])+"EQUAL\n"


def p_condition_GREATER(p):
    "context : exp '>' exp"
    p[0] = str(p[1])+str(p[3])+"SUP\n"


def p_condition_LESSER(p):
    "context : exp '<' exp"
    p[0] = str(p[1])+str(p[3])+"INF\n"


def p_condition_GREATERQ(p):
    "context : exp GREATERQ exp"
    p[0] = str(p[1])+str(p[3])+"SUPEQ\n"


def p_condition_LESSERQ(p):
    "context : exp LESSERQ exp"
    p[0] = str(p[1])+str(p[3])+"INFEQ\n"


def p_context(p):
    "context : condition"
    p[0] = p[1]

# endregion

# region EXPRESSION FUNCTIONS


def p_plus_expression(p):
    "exp : exp '+' term"
    p[0] = p[1] + p[3] + "ADD\n"


def p_minus_expression(p):
    "exp : exp '-' term"
    p[0] = p[1] + p[3] + "SUB\n"


def p_expression(p):
    "exp : term"
    p[0] = p[1]

# endregion

# region TERM FUNCTIONS


def p_division_term(p):
    "term : term '/' factor"
    p[0] = p[1] + p[3] + "DIV\n"


def p_multiplication_term(p):
    "term : term '*' factor"
    p[0] = p[1] + p[3] + "MUL\n"


def p_mod_term(p):
    "term : term '%' factor"
    p[0] = p[1] + p[3] + "MOD\n"


def p_term(p):
    "term : factor"
    p[0] = p[1]
# endregion

# region FACTORS FUNCTIONS


def p_num_factor(p):
    "factor : NUM"
    p[0] = "PUSHI "+p[1]+"\n"


def p_id_factor(p):
    "factor : Id"
    p[0] = p[1][1]

# endregion


def p_Id(p):
    "Id : ID"
    if p[1] not in parser.variables:
        parser.success = False
        print("Variable not declared: " + p[1])
        sys.exit(0)
    else:
        p[0] = ("STOREG " + str(parser.variables[p[1]])+"\n", "PUSHG " +
                str(parser.variables[p[1]])+"\n", p[1])
# definição Id = ID


def p_error(p):
    print("Syntax error!")
    parser.success = False
    sys.exit(0)
# definição de erro de sintaxe

# region ALL FUNCTIONS RELATED TO SIMPLE ARRAYS


def p_def_array_values(p):
    "values : NUM ',' values"
    p[0] = "PUSHI "+p[1]+"\n"+p[3]
    parser.arraycount += 1


def p_def_array_num(p):
    "values : NUM"
    p[0] = "PUSHI "+p[1]+"\n"
    parser.arraycount += 1


def p_def_empty_array(p):
    "values :"
    p[0] = ""


def p_array_declaration(p):
    "declaration : INT ID '[' NUM ']'"
    if p[2] in parser.variables:
        parser.success = False
        print("Multiple variable declaration " + p[2])
        sys.exit(0)
    else:

        parser.variables[p[2]] = parser.count
        p[0] = "PUSHN " + p[4] + "\n"
        parser.count += int(p[4])


def p_array_num_declaration(p):
    "declaration : INT ID '[' NUM ']' '=' values"
    if p[2] in parser.variables:
        parser.success = False
        print("Multiple variable declaration " + p[2])
        sys.exit(0)

    elif (parser.arraycount) != int(p[4]):
        parser.success = False
        print("Index out of range -> variable: " + p[2])
        sys.exit(0)
    else:
        parser.variables[p[2]] = parser.count
        p[0] = p[7]
        parser.count += int(p[4])
        parser.arraycount = 0


def p_print_command_id_Array(p):
    "cmd_print : ID_Array"
    p[0] = p[1][0]+p[1][1] + "LOADN\n"+"WRITEI\n"


def p_read_id_array_command(p):
    "cmd_read : READ ID_Array"
    p[0] = p[1][0]+p[1][1] + "READ\nATOI\nSTOREN\n"


def p_id_array_factor(p):
    "factor : ID_Array"
    p[0] = (p[1][0]+p[1][1]+"LOADN\n", p[1][2])


def p_condition_exp(p):
    "context : exp"
    p[0] = str(p[1])


def p_array_exp_command(p):
    "command : ID_Array '=' exp"
    p[0] = p[1][0]+p[1][1]+p[3]+"STOREN\n"


def p_id_array(p):
    "ID_Array : ID '[' factor ']'"
    if (p[1] not in parser.variables):
        parser.success = False
        print("Multiple variable declaration " + p[1])
        sys.exit(0)
    else:
        p[0] = ("PUSHGP\nPUSHI " + str(parser.variables[p[1]])+"\nPADD\n", p[3])

        # endregion


# region ALL FUNCTIONS RELATED TO DOUBLE ARRAYS

def p_double_values(p):
    "d_values : '[' values ']' d_values"
    p[0] = p[2] + p[4]
    parser.darraycount += 1


def p_empty_double_values(p):
    "d_values :"
    p[0] = ""


def d_values_values(p):
    "d_values : '[' values ']'"
    p[0] = p[2]
    parser.darraycount += 1


def p_double_array_declaration(p):
    "declaration : INT ID '[' NUM ']' '[' NUM ']'"
    if p[2] in parser.variables:
        parser.success = False
        print("Multiple variable declaration " + p[2])
        sys.exit(0)
    else:
        parser.variables[p[2]] = parser.count
        p[0] = "PUSHN " + str(int(p[4])*int(p[7])) + "\n"
        parser.count += (int(p[4]) * int(p[7]))

def p_double_array_num_declaration(p):
    "declaration : INT ID '[' NUM ']' '[' NUM ']' '=' d_values "
    if p[2] in parser.variables:
        parser.success = False
        print("Multiple variable declaration " + p[2])
        sys.exit(0)
    elif (parser.arraycount != int(p[4])*int(p[7])) or (parser.darraycount != int(p[4])):
        parser.success = False
        print("Index out of range -> variable: " + p[2])
        sys.exit(0)
    else:
        parser.variables[p[2]] = parser.count
        p[0] = p[10]
        parser.count += (int(p[4]) * int(p[7]))
        parser.size[p[2]] = int(p[7])
        parser.arraycount = 0
        parser.darraycount = 0


def p_double_array_exp_command(p):
    "command : ID_Double_Array '=' exp"
    p[0] = p[1][0]+p[1][1]+p[3]+"STOREN\n"


def p_print_command_double_array(p):
    "cmd_print : ID_Double_Array"
    p[0] = p[1][0]+p[1][1] + "LOADN\n"+"WRITEI\n"


def p_read_command_double_array(p):
    "cmd_read : ID_Double_Array"
    p[0] = p[1][0]+p[1][1] + "READ\nATOI\nSTOREN\n"


def p_id_double_array_factor(p):
    "factor : ID_Double_Array"
    p[0] = (p[1][0]+p[1][1]+"LOADN\n")


def p_id_double_array(p):
    "ID_Double_Array : ID '[' factor ']' '[' factor ']'"
    if (p[1] not in parser.variables):
        parser.success = False
        print("Multiple variable declaration " + p[1])
        sys.exit(0)
    else:
        p[0] = ("PUSHGP\nPUSHI " + str(parser.variables[p[1]]) +
                "\nPADD\n", p[3] + "PUSHI " + str(parser.size[p[1]]) + "\nMUL\n" + p[6] + "ADD\n")


# endregion

parser = yacc.yacc()
parser.variables = {}
parser.success = True

parser.count = 0
parser.label = 0
parser.loop = 0
parser.size = {}
parser.arraycount = 0
parser.darraycount = 0

fIn = input('FileInput: ')
fOut = input('FileOutput: ')

with open(fIn, 'r') as file:
    code = file.read()
out = parser.parse(code)
with open(fOut, 'w') as output:
    output.write(str(out))

print(parser.variables)
