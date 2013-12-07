function drawVenn(label1, label2, size1, size2, overlap) {
	document.getElementsByTagName("venn")[0].innerHTML="";
	var sets = [{label: label1, size:size1}, 
			{label: label2, size:size2}],
			 overlaps = [{sets: [0,1], size:overlap}];
	
	// get positions for each set
	sets = venn.venn(sets, overlaps);
	
	// draw the diagram in the 'venn' div
	venn.drawD3Diagram(d3.select("venn"), sets, 300, 300);
}