function togglelayout() {
	oBody = document.getElementById('body');
	if (oBody) {
		if (oBody.className == 'liquid') {
			oBody.className = 'fixed';
		} else {
			oBody.className = 'liquid';
		}
	}
}
