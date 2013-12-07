function createTable(n) {

	rv = "<table>";
	rv = rv + "<tr>";

	for (var i=0;i<n.length;i++) {
		rv = rv + "<td>" + n[i] + "</td>";
	}
	
	rv = rv + "</tr>";
	rv = rv + "</table>";
	
	return rv;
}

function createTableFrom2dArray(n) {
	rv = "<table>";

	for (var i = 0; i < n.length; i++) {
		rv = rv + "<tr>";
	
		for (var j = 0; j < n[i].length; j++) {
			rv = rv + "<td>" + n[i][j] + "</td>";
		}

		rv = rv + "</tr>";
	}
	
	rv = rv + "</table>";
	
	return rv;
}

function create2DTable(n, m, o) {

	rv = "<table>";
	rv = rv + "<tr>";
	for (var i=0;i<n.length;i++) {
		rv = rv + "<td>" + n[i] + "</td>";
	}
	rv = rv + "</tr>";
	
	rv = rv + "<tr>";
	for (var j=0; j< m.length;j++) {
		rv = rv + "<td>" + m[j] + "</td>";
	}
	rv = rv + "</tr>";
	
	rv = rv + "<tr>";
	for (var j=0; j< o.length;j++) {
		rv = rv + "<td>" + o[j] + "</td>";
	}
	rv = rv + "</tr>";
	
	rv = rv + "</table>";
	
	return rv;
}