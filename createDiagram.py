
def createVenn(size1, size2, overlap, name1, name2):
	return '''<script>document.getElementsByTagName("venn")[0].innerHTML="";var sets = [{label: "'''+name1+'''", size: ''' + unicode(size1) + '''
}, {label: "'''+name2+'''", size: ''' + unicode(size2) + '''}],
    overlaps = [{sets: [0,1], size: ''' + unicode(overlap) +'''}];

// get positions for each set
sets = venn.venn(sets, overlaps);

// draw the diagram in the 'venn' div
venn.drawD3Diagram(d3.select("venn"), sets, 300, 300);
</script>
''';