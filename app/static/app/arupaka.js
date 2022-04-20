$(function(){
	loadend();
});


document.getElementById("1").addEventListener("click",function(){home()},true);
document.getElementById("2").addEventListener("click",function(){illust()},true);
document.getElementById("3").addEventListener("click",function(){about()},true);

function home(){
	document.getElementById("amain").style.display = "";
	document.getElementById("bmain").style.display = "none";
	document.getElementById("cmain").style.display = "none";
}
function illust(){
	document.getElementById("amain").style.display = "none";
	document.getElementById("bmain").style.display = "";
	document.getElementById("cmain").style.display = "none";
}
function about(){
	document.getElementById("amain").style.display = "none";
	document.getElementById("bmain").style.display = "none";
	document.getElementById("cmain").style.display = "";
}

function loadend(){
	document.getElementById("bmain").style.display = "none";
	document.getElementById("cmain").style.display = "none";
	document.getElementById("end").style.display = "none";
}