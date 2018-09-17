$(function () {
	var windowJanela;
	// configurando o annyAng
	if( annyang ) {
		// Definicao do primeiro comando. Primeiro texto de chamada e depois a funcao ou texto a escrever
		var commands = {
			'limpar': function() {
				$("#texto").html("");
				$("body").css({"background-color" : "white"});
			},
			'escreva *term': function(term) {
			  $("#texto").html($("#texto").html()+" <br/>"+ term);
			},
			'acessar *term': function(term) {
				windowJanela = window.open('http://'+term, 'teste');
			},
			'facebook': function() {
				facebook = window.open('http://www.facebook.com');
			},
			'fechar guia': function(term) {
				 windowJanela.close();
				 if(facebook){
					 facebook.close();
				 }
			},
			'fundo *term': function(term) {
				if(term == "vermelho"){
					$("body").css({"background-color" : "darkred"});
				}
				if(term == "verde"){
					$("body").css({"background-color" : "green"});
				}
				if(term == "azul"){
					$("body").css({"background-color" : "blue"});
				}
				if(term == "amarelo"){
					$("body").css({"background-color" : "yellow"});
				}
				if(term == "preto"){
					$("body").css({"background-color" : "black"});
				}
			}
		};

	  //Idioma...
	  annyang.setLanguage("pt-BR");

	  // Adicionar comandos para a API (annyang)
	  annyang.addCommands(commands);

	  // Iniciar escuta. Podera ser chamado aqui ou carregado por um evento ou botao, etc
	  annyang.start();
	}
});
