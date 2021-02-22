SCRIPT_NAME = "RPGRoll";
SCRIPT_VER = "3";
SCRIPT_DESC = "Rolagem de dados";

print("RPGRoll executando.");

function rolaDados(dados,lados,mod,personagem){
	var textresult = "Você rolou " + dados + "d" + lados + " com modificador " + ((mod==undefined)?"0":mod) + " para "+personagem+" = ";
	var resultado = 0;
	var valor = 0;

	for(var count = 1;count <= dados;count++){
		valor = Math.floor(Math.random() * lados) + 1;
		resultado += Number(valor); 
		if(valor <= 33)
			textresult+= "1,4 "+ valor + "  + ";	
		else if(valor >= 34 && valor <= 66)
			textresult+= "1,8 "+ valor + "  + ";	
		else if(valor >= 67)
			textresult+= "1,9 "+ valor + "  + ";	
	}
	resultado += ((mod==undefined)?0:Number(mod));
	textresult +=  ((mod==undefined)?"0":mod) + " = " + resultado;
	command('say '+ textresult);
}

function rola(word,word_eol){
	var dados = word[1];
	var lados = word[2];
	var mod = word[3];
	var personagem = word[4];
	if(!possuiErro("rola",dados,lados,mod,personagem)){
		rolaDados(dados,lados,mod,personagem);
	}
}

function possuiErro(origem,dados,lados,mod,personagem){
	var temErro = false;
	if(dados === undefined){
		print("4t[ERRO] "+origem+": Por favor, insira os dados.")
		temErro = true;
	}
	if(lados === undefined){
		print("4t[ERRO] "+origem+": Por favor, insira quantos lados o dado tem de ter.")
		temErro = true;	
	}
	if(mod === undefined){
		print("4t[ERRO] "+origem+": Por favor, insira o valor do modificador.")
		temErro = true;	
	}
	if(personagem === undefined){
		print("4t[ERRO] "+origem+": Por favor, insira o nome do personagem.")
		temErro = true;	
	}
	return temErro;
}

function rolap(word,word_eol){
	var dados = word[1];
	var lados = word[2];
	var personagem = word[3];
	if(!possuiErro("rolap",dados,lados,0,personagem)){
		rolaDados(dados,lados,0,personagem);	
		rolaDados(dados,lados,-10,personagem);
		rolaDados(dados,lados,-20,personagem);
	}
}

hook_command ('rola', rola, "USAGE: rola qtd lados mod");
hook_command ('rolap', rolap, "USAGE: rolap qtd lados");