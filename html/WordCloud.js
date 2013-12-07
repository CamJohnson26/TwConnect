function drawWordCloud(input) {

	inputCounts = [];
	inputWords = [];
	for (var i = 0; i < input.length; i++) {
		inputWords.push(input[i][0]);
		inputCounts.push(input[i][1]);
	}
	
	var fill = d3.scale.category20();
	 var counts= inputCounts;
	var largest = 0;
	for(var i = 0; i < counts.length; i++) {
		if (parseFloat(counts[i]) > largest) {
			largest = parseFloat(counts[i]);
		}
	}
	
	if (largest == 0) {
		largest = 1;
	}
	d3.layout.cloud().size([400, 400])
	  .words(inputWords.map(function(d, i) {
		return {text: d, size: (28 * (parseFloat(counts[i]) / largest) + 12)};
	  }))
	  .padding(5)
	  .rotate(function() { return 0; })
	  .font("Impact")
	  .fontSize(function(d) { return d.size; })
	  .on("end", draw)
	  .start();
	
	function draw(words) {
	document.getElementsByTagName("wordcloud")[0].innerHTML="";
	d3.select("wordcloud").append("svg")
		.attr("width", 400)
		.attr("height", 400)
	  .append("g")
		.attr("transform", "translate(200,200)")
	  .selectAll("text")
		.data(words)
	  .enter().append("text")
		.style("font-size", function(d) { return d.size + "px"; })
		.style("font-family", "Impact")
		.style("fill", function(d, i) { return fill(i); })
		.attr("text-anchor", "middle")
		.attr("transform", function(d) {
		  return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
		})
		.text(function(d) { return d.text; });
	}
}

function drawHashTagCloud(input) {

	inputCounts = [];
	inputWords = [];
	for (var i = 0; i < input.length; i++) {
		inputWords.push(input[i][0]);
		inputCounts.push(input[i][1]);
	}
	
	var fill = d3.scale.category20();
	 var counts= inputCounts;
	 
	var largest = 0;
	for(var i = 0; i < counts.length; i++) {
		if (parseFloat(counts[i]) > largest) {
			largest = parseFloat(counts[i]);
		}
	}
	
	if (largest == 0) {
		largest = 1;
	}
	d3.layout.cloud().size([400, 400])
	  .words(inputWords.map(function(d, i) {
		return {text: d, size: (28 * (parseFloat(counts[i]) / largest) + 12)};
	  }))
	  .padding(5)
	  .rotate(function() { return 0; })
	  .font("Impact")
	  .fontSize(function(d) { return d.size; })
	  .on("end", draw)
	  .start();
	
	function draw(words) {
	document.getElementsByTagName("hashtagcloud")[0].innerHTML="";
	d3.select("hashtagcloud").append("svg")
		.attr("width", 400)
		.attr("height", 400)
	  .append("g")
		.attr("transform", "translate(200,200)")
	  .selectAll("text")
		.data(words)
	  .enter().append("text")
		.style("font-size", function(d) {return d.size + "px"; })
		.style("font-family", "Impact")
		.style("fill", function(d, i) { return fill(i); })
		.attr("text-anchor", "middle")
		.attr("transform", function(d) {
		  return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
		})
		.text(function(d) { return d.text; });
	}
}