


import keyword
from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('DefaultNoMoreNagging')

layout = [
    [sg.Text('Usuário:'), sg.Input(key='Usuario',size=(20,1))],
    [sg.Text('Senha:'), sg.Input(key='Senha nova', size=(15,1), password_char='*')],   
    [sg.Button('Entrar')],
]

layoutWelcome = [
    [sg.Text('Seja Bem-Vindo!')],
    [sg.Button('OK')]
]

layoutEsqueceu = [
    [sg.Text('Senha'), sg.Input(key='Senha nova', size=(25,1))],
    [sg.Text('Confirme a Senha'), sg.Input(key='Confirme a Senha',size=(25,1))],
    [sg.Button('Atualizar')]
    
]

layoutConfirme = [
    [sg.Text(' Senhas Diferentes ')],
    [sg.Button('OK')]
]

layoutAtualizar = [
    [sg.Text('Senha Atualizada')],
    [sg.Button('OK')]
]

layoutErro = [
    [sg.Text('Senha Incorreta')],
    [sg.Button('OK')]

]

layoutMensalista = [
    [sg.Text('Tabela de Mensalista Estapar', size=(30,2))],
    [sg.Text('Usuário:'), sg.Input(key='Usuario',size=(20,1))]

]
# janela
janela = sg.Window('Tela de Login', layout)
janelaWelcome = sg.Window('Acesso Liberado', layoutWelcome)
janelaEsqueceu = sg.Window('Esqueceu a senha', layoutEsqueceu)
janelaConfirme = sg.Window('Senhas Diferentes', layoutConfirme)
janelaAtualizar = sg.Window('Senha Atualizada', layoutAtualizar)
janelaErro = sg.Window('Senha incorreta', layoutErro)
janelaMensalista = sg.Window('Mensalista Estapar', layoutMensalista)
# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Esqueceu a senha?':
        janelaEsqueceu()
    if eventos == 'Esqueceu a senha?':
          #if (valores['Senha nova'] != ['Confirme a Senha']):
            #janelaConfirme()
            #janelaConfirme.Close()
            
      
        if(valores['Senha nova'] == ['Confirme a Senha']):
            janelaAtualizar()
            janelaAtualizar.Close()      
    if eventos == 'Entrar':
        if (valores['Usuario'] == 'Admin' or valores['Usuario'] == 'CGC' or valores ['Usuario'] == 'Caixa') and valores['Senha nova'] == '1234' or valores['Senha nova'] == 'Admin':
            janela.Close()
            janelaWelcome()
            janelaWelcome.Close()
            janelaMensalista()
        if (valores['Usuario'] != 'Admin' or valores['Usuario'] != 'CGC' or valores ['Usuario'] != 'Caixa') and valores['Senha nova'] != '1234':
            janelaErro()
            janelaErro.Close()
            
        

            
           
            
