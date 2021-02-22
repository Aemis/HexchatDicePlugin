local nome = "Rolador3.0 - Lua Version"
local versao = 3
local desc = "Rolador de dados"
math.randomseed(os.time())

local function rolador(word,eol)
	qtd = word[2]--QTD
	lados = word[3]--LADOS
	mod = word[4]--MOD
	nome = word[5]--PERSONAGEM

	erro = false
	erro = (tonumber(qtd) < 1)
	erro = ((tonumber(lados) < 1) or erro)
	erro = ((not nome) or erro)

	if erro then
		hexchat.print("Por favor utilize /rola QTD LADOS MOD NOME_PERSONAGEM sendo que o QTD, LADOS e NOME_PERSONAGEM não podem ser vazios!!!")
	else

		dado = 0
		dados = 0
		frase = "Rolei "..tostring(qtd).."d"..tostring(lados).." com mod("..tostring(mod)..") para "..nome.." e os resultados foram ["
		for n = 1,qtd do
			if (n > 1) then
				frase = frase.." - "
			end
			dado = math.random(1,lados) 
			dados = dados + dado
			if dado < (lados/3) then
				frase = frase.." 0,4 "..tostring(dado).." "
			end
			if dado >= (lados/3) and dado < ((lados/3)*2) then
				frase = frase.." 0,7 "..tostring(dado).." "
			end
			if dado >= ((lados/3)*2) then
				frase = frase.." 0,3 "..tostring(dado).." "
			end
		end
		frase = frase.." + "..tostring(mod).."]"
		dados = dados + mod
		frase = frase.." = "..tostring(dados)..""

		canal = hexchat.get_info("channel")
		comando = "msg "..canal.." "..frase
		hexchat.command(comando)
	end 

	return hexchat.EAT_ALL
end

hexchat.register(nome,versao,desc)
hexchat.hook_command("ROLA",rolador,desc)