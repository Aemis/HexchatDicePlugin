__module_name__ = "Dice Roller"
__module_version__ = "1.0"
__module_description__ = "Rolador de Dados em Python"

import hexchat 
from random import seed
from random import randint

def rolarDado(nome, qtd, lados, mod):
	seed()
	texto = "Rolei "+str(qtd)+"d"+str(lados)+" com mod("+str(mod)+") para "+str(nome)+" e os resultados foram ["
	dadoAtual = 1
	resultado = 0
	resultadoFinal = 0
	while dadoAtual <= qtd:
		if dadoAtual > 1:
			texto = texto+" - "
		
		resultado = randint(1,lados)
		resultadoFinal = resultadoFinal + resultado		
		if resultado < (lados/3):
			texto = texto+" 0,4 "+str(resultado)+" "

		if resultado >= (lados/3) and resultado < ((lados/3)*2):
			texto = texto+" 0,7 "+str(resultado)+" "

		if resultado >= ((lados/3)*2):
			texto = texto+" 0,3 "+str(resultado)+" "

		dadoAtual = dadoAtual + 1
	texto = texto+" + "+str(mod)+"]"
	resultadoFinal = resultadoFinal + mod
	texto = texto+" = "+str(resultadoFinal)+""
	return texto


def comandoRolador(word, word_eol, userdata):
	if len(word) < 5:
		print("Por favor utilize /rola QTD LADOS MOD NOME_PERSONAGEM sendo que o QTD, LADOS e NOME_PERSONAGEM não podem ser vazios!!!")
	else:		
		qtd = int(word[1]) #QTD
		lados = int(word[2]) #LADOS
		mod = int(word[3]) #MOD
		nome = word[4] #PERSONAGEM
		frase = rolarDado(nome,qtd,lados,mod)
		canal = hexchat.get_info("channel")
		comando = "msg "+canal+" "+frase
		hexchat.command(comando)
	return hexchat.EAT_ALL


hexchat.hook_command("rola",comandoRolador,"Por favor utilize /rola QTD LADOS MOD NOME_PERSONAGEM sendo que o QTD, LADOS e NOME_PERSONAGEM não podem ser vazios!!!")
