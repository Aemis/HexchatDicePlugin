local nome = "Rolador4.0 - Lua Version"
local versao = 4
local desc = "Rolador de dados Multiplos"
math.randomseed(os.time())

local personagem_arquivo = hexchat.get_info("configdir") .. "/nome_personagem.txt"

local function salvar_personagem(nome)
    local f = io.open(personagem_arquivo, "w")
    if f then
        f:write(nome)
        f:close()
    end
end

local function carregar_personagem()
    local f = io.open(personagem_arquivo, "r")
    if f then
        local nome = f:read("*l")
        f:close()
        return nome
    end
    return nil
end


local function rolar_dado(qtd, lados)
    local total = 0
    local texto = ""

    for i = 1, qtd do
        if i > 1 then
            texto = texto .. " ; "
        end

        local resultado = math.random(1, lados)
        total = total + resultado

        if resultado < (lados / 3) then
            texto = texto .. "0,4 " .. resultado .. " "
        elseif resultado < ((lados / 3) * 2) then
            texto = texto .. "0,7 " .. resultado .. " "
        else
            texto = texto .. "0,3 " .. resultado .. " "
        end
    end

    return texto, total
end

local function rolador(expr, nome)
    local resultado_final = 0
    local texto = "Rolei " .. expr .. " para " .. nome .. " e os resultados foram ["

    for sinal, qtd, lados in string.gmatch(expr, "([+-]?)(%d+)[dD]?(%d*)") do
        local mult = (sinal == "-") and -1 or 1
        local quantidade = tonumber(qtd)
        local texto_parte = ""
        local valor = 0

        if lados ~= "" then
            lados = tonumber(lados)
            texto_parte, valor = rolar_dado(quantidade, lados)
        else
            valor = quantidade
            texto_parte = tostring(mult * quantidade)
        end

        resultado_final = resultado_final + (mult * valor)
        texto = texto .. sinal .. " (" .. texto_parte .. ") "
    end

    texto = texto .. "] = " .. tostring(resultado_final) .. ""
    return texto
end

local function comando_rolar(word, word_eol, userdata)
    comando = word[2]
    nome = word[3]

    if not comando then
        hexchat.print("Uso: /rolam EXPRESSAO [NOME_PERSONAGEM]")
        return hexchat.EAT_ALL
    end

    if not nome then
        nome = carregar_personagem()
        if not nome then
            hexchat.print("Você ainda não atribuiu um personagem. Ex: /rolam 1d6+1d4 Juju")
            return hexchat.EAT_ALL
        end
    else
        salvar_personagem(nome)
    end

    hexchat.print("O nome é "..nome)

    local frase = rolador(comando, nome)
    local canal = hexchat.get_info("channel")
    hexchat.command("msg " .. canal .. " " .. frase)

    return hexchat.EAT_ALL
end

hexchat.register(nome,versao,desc)
hexchat.hook_command("ROLAM",comando_rolar,desc)