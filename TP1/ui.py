import typing
from  PyQt5.QtWidgets  import *
from PyQt5 import QtCore, uic
import sys

from PyQt5.QtWidgets import QWidget

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn_list=[]
        uic.loadUi('postfix.ui',self)
        self.input_screen=self.findChild(QLineEdit,'input_screen')
        self.Postfix_screen=self.findChild(QLineEdit,'Postfix_screen')
   
        x_1=self.findChild(QPushButton,f"pushButton_1")
        x_1.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_1.text()))
        
   
        x_2=self.findChild(QPushButton,f"pushButton_2")
        x_2.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_2.text()))
        
   
        x_3=self.findChild(QPushButton,f"pushButton_3")
        x_3.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_3.text()))
        
   
        x_4=self.findChild(QPushButton,f"pushButton_4")
        x_4.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_4.text()))
        
   
        x_5=self.findChild(QPushButton,f"pushButton_5")
        x_5.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_5.text()))
        
   
        x_6=self.findChild(QPushButton,f"pushButton_6")
        x_6.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_6.text()))
        
   
        x_7=self.findChild(QPushButton,f"pushButton_7")
        x_7.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_7.text()))
        
   
        x_8=self.findChild(QPushButton,f"pushButton_8")
        x_8.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_8.text()))
        
   
        x_9=self.findChild(QPushButton,f"pushButton_9")
        x_9.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_9.text()))
        
   
        x_10=self.findChild(QPushButton,f"pushButton_10")
        x_10.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_10.text()))
        
   
        x_11=self.findChild(QPushButton,f"pushButton_11")
        x_11.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_11.text()))
        
   
        x_12=self.findChild(QPushButton,f"pushButton_12")
        x_12.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_12.text()))
        
   
        x_13=self.findChild(QPushButton,f"pushButton_13")
        x_13.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_13.text()))
        
   
        x_14=self.findChild(QPushButton,f"pushButton_14")
        x_14.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_14.text()))
        
   
        x_15=self.findChild(QPushButton,f"pushButton_15")
        x_15.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_15.text()))
        
   
        x_16=self.findChild(QPushButton,f"pushButton_16")
        x_16.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_16.text()))
        
   
        x_17=self.findChild(QPushButton,f"pushButton_17")
        x_17.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_17.text()))
        
   
        x_18=self.findChild(QPushButton,f"pushButton_18")
        x_18.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_18.text()))
        
   
        x_19=self.findChild(QPushButton,f"pushButton_19")
        x_19.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_19.text()))
        
   
        x_20=self.findChild(QPushButton,f"pushButton_20")
        x_20.clicked.connect(lambda:self.input_screen.setText(self.input_screen.text()+ x_20.text()))
        
        compile=self.findChild(QPushButton,f"compile")
        compile.clicked.connect(lambda:self.Postfix_screen.setText(infix_to_postfix(self.input_screen.text())))
        dellet=self.findChild(QPushButton,f"dell")
        dellet.clicked.connect(lambda:self.input_screen.setText(str(self.input_screen.text())[:-1] ))
        clear=self.findChild(QPushButton,f"clear")
        clear.clicked.connect(lambda:self.cl())
        

        dellet=self.findChild(QPushButton,f"validat")
        dellet.clicked.connect(lambda:print(generate_truth_table(str(self.Postfix_screen.text()))))
        self.show()
    def cl(self):
        self.input_screen.setText("" )
        self.Postfix_screen.setText("" )
        
# ######################################################################################
# ######################################################################################
# ######################################################################################
# ######################################################################################


def posfix(expression:str):
    oparetor = {'→': 1, '↔': 1, '∩': 2, '∪': 2, '¬': 3}
    oparetor_stack = []
    result = ''
   


    for char in expression:
        if char.isalpha():
            result += char
        
        elif char == '(':
            oparetor_stack.append(char)
        elif char == ')':
            while oparetor_stack and oparetor_stack[-1] != '(':
                result += oparetor_stack.pop()
            oparetor_stack.pop()  
 
            
        else:
            
            while len(oparetor_stack) and oparetor_stack[-1] != '(' and oparetor[char] <= oparetor.get(oparetor_stack[-1]):
                result += oparetor_stack.pop()
            oparetor_stack.append(char)

    while oparetor_stack:
        result += oparetor_stack.pop()

    return result


# ######################################################################################
# ######################################################################################
# ######################################################################################
# ######################################################################################
def infix_to_postfix(expression):
    stack = []
    postfix = []
    oparetor = {'→': 1, '↔': 1, '∩': 2, '∪': 2, '¬': 3}

    for char in expression:
        if char.isalpha():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '(' from stack
        else:
            while stack and stack[-1] != '(' and oparetor[char] <= oparetor.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)  

# ######################################################################################
# ######################################################################################
# ######################################################################################
# ######################################################################################

def generate_truth_table(postfix_expression:str):
    variables = set()
    table = []
    oparetor = {'→': 1, '↔': 1, '∩': 2, '∪': 2, '¬': 3}
    # Get unique variables from the postfix expression
    for char in postfix_expression:
        if char.isalpha():
            variables.add(char)

    # Generate all possible combinations of variable values
    variable_values = get_variable_combinations(variables)

    # Evaluate the expression for each combination of variable values
    for values in variable_values:
        stack = []
        for char in postfix_expression:
            if char.isalpha():
                stack.append(values.get(char))
            elif char in oparetor:
                if len(stack) < 2:
                    return None
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = evaluate_logic_operator(char, operand1, operand2)
                stack.append(result)
            else:
                return None

        if len(stack) == 1:
            table.append([values, stack[0]])

    return table


def get_variable_combinations(variables):
    values = {}
    variable_list = sorted(list(variables))
    num_variables = len(variable_list)

    for i in range(2 ** num_variables):
        binary = bin(i)[2:].zfill(num_variables)
        values = {variable_list[j]: int(binary[j]) for j in range(num_variables)}

    return values


def evaluate_logic_operator(operator, operand1, operand2):
    # Perform logic operator evaluation based on the provided operator precedence dictionary
    # Modify this function according to your logic operator evaluation rules
    if operator == '→':
        return operand1 <= operand2
    elif operator == '↔':
        return operand1 == operand2
    elif operator == '∩':
        return operand1 and operand2
    elif operator == '∪':
        return operand1 or operand2
    elif operator == '¬':
        return not operand1
    else:
        return False
# ######################################################################################
# ######################################################################################
# ######################################################################################
# ######################################################################################
app=QApplication(sys.argv)
jj=UI()
app.exec_()

