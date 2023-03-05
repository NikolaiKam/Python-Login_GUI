import PySimpleGUI as sg
from Logers import *
from Logins_Random_Codes import *

sg.theme('Python')

layout=[
    [
        sg.Text('Enter your email: '),
        sg.InputText(key='Email', size=(50,3))
    ],
    [
        sg.Text('Enter password: '),
        sg.InputText(key='Password',size=(50,3),password_char='*')
    ],
    [
        sg.Submit('Log In'),
        sg.Text('',key='correct')
    ],
    [
        sg.Submit('Forgot your password'),
        sg.Text('',key='random')
    ]
]

window=sg.Window('Registration',layout)

while True:
    event,value = window.read()
    
    if event==sg.WIN_CLOSED:
        break

    if event=='Log In':
        if correct_email(str(value['Email']))=='Correct':
            window['correct'].update(correct_logs(str(value['Email']),str(value['Password'])))             
        else:
            window['correct'].update('Invalid email')
    
    
    if event=='Forgot your password':
        code1=Generate_Code()
        window['random'].update(code1)

window.close()
