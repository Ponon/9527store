function loadPage(url, elementId) {
	var selectedElements = document.querySelectorAll('.selected');
	selectedElements.forEach(function(element) {
		element.classList.remove('selected');
	});
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById(elementId).innerHTML = this.responseText;

			
			}
		}
	};
	xhttp.open("GET", url, true);
	xhttp.send();
}



// 默认加载go.html
window.onload = function() {
	loadPage('go.html', 'content');
};