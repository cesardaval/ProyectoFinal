$(document).ready(main);
var contador = 1;

function main(){
	$('.menu_bar').click(function(){
		/*si la variable cuenta 1 esta
		activado el menu, si no esta
		desactivado*/
		if (contador==1){
			/*elmenu esta oculto*/
			$('nav').animate({
				left:'0'
			});
			contador = 0;
		}else{
			contador = 1;
			$('nav').animate({
				left:'-100%'
			});
		}
	});
}
/*https://www.youtube.com/watch?v=EB4BG3QZn3o*/