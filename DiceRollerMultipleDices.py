__module_name__ = "Dice Roller Multiple"
__module_version__ = "0.1"
__module_description__ = "Rolador de Dados Multiplos em Python"

import hexchat
import re
from random import seed, randint

def rolador(comando, nome):
    regex = r"([+-]?)(\d+)(?:d(\d+))?"
    texto = "Rolei " + comando + " para " + str(nome) + " e os resultados foram ["

    padrao = re.findall(regex, comando)
    resultadoFinal = 0

    for sinal, quantidade, lados in padrao:
        quantidade = int(quantidade)
        sinalChar = sinal
        sinal = -1 if sinal == '-' else 1

        if lados:
            lados = int(lados)
            textoParte, valorParcial = rolar_dado(quantidade, lados)
            resultadoFinal += sinal * valorParcial
        else:
            valorParcial = quantidade
            textoParte = str(sinal * quantidade)
            resultadoFinal += sinal * quantidade

        texto += sinalChar+" (" + textoParte + ") "

    texto += "] = " + str(resultadoFinal) + ""
    return texto

def rolar_dado(qtd, lados):
    seed()
    resultadoFinal = 0
    texto = ""

    for i in range(1, qtd + 1):
        if i > 1:
            texto += " ; "

        resultado = randint(1, lados)
        resultadoFinal += resultado

        if resultado < (lados / 3):
            texto += "0,4 " + str(resultado) + " "
        elif resultado < ((lados / 3) * 2):
            texto += "0,7 " + str(resultado) + " "
        else:
            texto += "0,3 " + str(resultado) + " "

    return texto, resultadoFinal

def comandoRolador(word, word_eol, userdata):
    isOk = 0

    if len(word) == 2:
        nomePersonagem = hexchat.get_pluginpref("name_character")

        if nomePersonagem:
            nome = nomePersonagem
            comando = word[1]
            isOk = 1
        else:
            print("Você ainda não atribuiu um personagem. Por favor utilize /rolam OPERAÇÃO NOME_PERSONAGEM antes de prosseguir. Exemplo: /rolam 1d4+1d6 Juju")
    elif len(word) == 3:
        comando = word[1]
        nome = word[2]
        hexchat.set_pluginpref("name_character", nome)
        isOk = 1

    if isOk == 1:
        frase = rolador(comando, nome)
        canal = hexchat.get_info("channel")
        hexchat.command("msg " + canal + " " + frase)
    else: 
        print("Erro ao executar. Verifique!")

    return hexchat.EAT_ALL

hexchat.hook_command("rolam", comandoRolador, "Uso: /rolam OPERAÇÃO NOME_PERSONAGEM na primeira rolagem, após isso /rolam OPERAÇÃO.")
