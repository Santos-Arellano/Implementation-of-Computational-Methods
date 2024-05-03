class TM:
    def __init__(self, states, start_state, accept_states, alphabet, _num):
        self.states = states
        self.start_state = start_state
        self.accept_states = accept_states
        self.alphabet = alphabet
        self.tape = _num
        self.head = 1
        self.transitions = {
            ('q0', '1'): ('q1', '1', 'R'),
            ('q0', '#'): ('qf', '#', 'R'),
            ('q1', '1'): ('q2', '1', 'R'),
            ('q1', '#'): ('q11', '#', 'L'),
            ('q2', '1'): ('q3', '$', 'R'),
            ('q2', '#'): ('q11', '#', 'L'),
            ('q3', '1'): ('q4', '$', 'L'),
            ('q3', '#'): ('q7', '#', 'L'),
            ('q3', '$'): ('q3', '$', 'R'),
            ('q4', '#'): ('q5', '#', 'R'),
            ('q4', '$'): ('q4', '$', 'L'),
            ('q4', '0'): ('q4', '0', 'L'),
            ('q4', '1'): ('q4', '1', 'L'),
            ('q5', '1'): ('q5', '0', 'R'),
            ('q5', '0'): ('q6', '1', 'R'),
            ('q5', '$'): ('q6', '1', 'R'),
            ('q6', '1'): ('q6', '1', 'R'),
            ('q6', '0'): ('q6', '0', 'R'),
            ('q6', '$'): ('q3', '$', 'R'),
            ('q7', '#'): ('q8', '#', 'R'),
            ('q7', '$'): ('q7', '#', 'L'),
            ('q7', '0'): ('q7', '0', 'L'),
            ('q7', '1'): ('q7', '1', 'L'),
            ('q8', '1'): ('q9', '1', 'R'),
            ('q8', '0'): ('q8', '1', 'R'),
            ('q9', '0'): ('q9', '1', 'R'),
            ('q9', '1'): ('q10', '1', 'R'),
            ('q9', '#'): ('q11', '#', 'L'),
            ('q10', '1'): ('q10', '1', 'R'),
            ('q10', '0'): ('q10', '1', 'R'),
            ('q10', '#'): ('qf', '#', 'L'),
            ('q11', '1'): ('qf', '#', 'R')
        }
        
    def perform_log2n(self):
        current_state = self.start_state
        while current_state not in self.accept_states:
            if(self.head >= len(self.tape) or self.head <= 0):
                self.tape.append('#')
            if(self.tape[self.head] not in self.alphabet):
                print('Simbolos invalidos')
                break
            if (current_state, self.tape[self.head]) in self.transitions:
                current_state, write, move = self.transitions[current_state,(self.tape[self.head])]
                """print(current_state, write, move)""" #Descomentar esta linea para ver las transiciones que se realizan. 
                self.tape[self.head] = write
                if move == 'R':
                    self.head+=1
                else:
                    self.head-=1
            else:
                print ('Error')
                break
        return self.tape;


# Definición de la maquina de turing
states = {'q0', 'q1','q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'qf'}
start_state = 'q0'
accept_states = {'qf'}
alphabet = {'1', '0', '$', '#'}

print("⌈Log2(n)⌉")
print("Ingresa el valor de n en unario ejemplo: (3 = 111)")
num = input()
_num = ['#']
for i in range(len(num)):
    _num.append(num[i])

TM = TM(states, start_state, accept_states, alphabet, _num)
result = TM.perform_log2n()
output = 0
for i in range(len(result)):
    if result[i] == '1':
        output += 1
print('⌈Log2(n)⌉ = ',output)