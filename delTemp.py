import os
import PySimpleGUI as sg

#################### VAR #############################
verificacao = True

######################### FUNC #######################
def delTemp():
    os.system(r'del /q %temp%\* && for /d %x in (%temp%\*) do @rd /s /q "%x""')

def delWinTemp():
    os.system(r'del /q C:\Windows\Temp\* && for /d %x in (C:\Windows\Temp\*) do @rd /s /q "%x"')

def delPrefetch():
    os.system(r'del /q C:\Windows\Prefetch\* && for /d %x in (C:\Windows\Prefetch\*) do @rd /s /q "%x"')


############################# GUI #####################
layout = [[sg.Text('ANTES DE MAIS NADA, SALVE TUDO O QUE ESTÁ ABERTO!')],
          [sg.Check('%TEMP%', size = (10, 1), key = '%temp%')],
          [sg.Check('temp', size = (10, 1), key = 'temp')],
          [sg.Check('prefetch', size = (10, 1), key = 'prefetch')],
          [sg.Button('Limpar tudo'), sg.Button('Limpar selecionados'), sg.Button('Sair')]]

window = sg.Window('Deletar arquivos temporários', layout)
 

while True:
    event, values = window.read()

#################### LIMPAR SELECIONADOS ##############
    if event == 'Limpar selecionados':
        if verificacao == True:
            sg.popup('Certifique-se de ter salvo todo seu trabalho aberto e selecione novamente a opção desejada', title = 'Cuidado!')
            verificacao = False
        else:
            if values['%temp%'] == True:
                delTemp()
            if values['temp'] == True:
                delWinTemp()
            if values['prefetch'] == True:
                delPrefetch()

#################### LIMPAR TUDO ######################
    if event == 'Limpar tudo':
        if verificacao == True:
            sg.popup('Certifique-se de ter salvo todo seu trabalho aberto e selecione novamente a opção desejada', title = 'Cuidado!')
            verificacao = False
        else:
            delTemp()
            delWinTemp()
            delPrefetch()

#################### FECHAR JANELA ####################
    if event == sg.WIN_CLOSED or event == 'Sair':
        break