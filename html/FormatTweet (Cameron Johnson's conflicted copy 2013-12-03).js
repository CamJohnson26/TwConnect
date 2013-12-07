function FormatTweet(tweetText, userName, userHandle, tweetid, tweetdate) {
	rv = "<blockquote class=\"twitter-tweet\" lang=\"en\"><p>" + tweetText;
	rv = rv + "</p>&mdash; " + userName;
	rv = rv + " (" + userHandle + ") <a href=\"https://twitter.com/" + userHandle.substring(1) +"/statuses/";
	rv = rv + tweetid + "\">November 23, 2013</a></blockquote></div>";
	//rv = rv + "<script async src=\"//platform.twitter.com/widgets.js\" charset=\"utf-8\"></script></div>";
	
	return rv;
}

function FormatUser(imgsrc,username,screenname, description, location, numtweets, numfollowing, numfollower, bgimage) {

	rv = "<div class=\"following-profile thumbnail\"><div class=\"following-profile-upper\"><div class=\"following-info\" style=\"background-image:url('" + bgimage + "')\"";
	rv = rv + "><img class=\"following-head-picture\" src=\"" + imgsrc;
	rv = rv + "\"></img><p class=\"following-name\">" + username;
	rv = rv + "</p><p class=\"following-handle\">" + "@" + screenname;
	rv = rv + "</p><p class=\"following-intro\">" + description;
	rv = rv + "</p><p class=\"following-location\">" + location;
	rv = rv + "</p></div><div class=\"following-info-num\"><div class=\"following-tweet-num\"><p class=\"following-num-num\">" + numtweets;
	rv = rv + "</p><p class=\"following-num-text\"> Tweets";
	rv = rv + "</p></div><div class=\"following-following-num\"><p class=\"following-num-num\">" + numfollowing;
	rv = rv + "</p><p class=\"following-num-text\">Followings";
	rv = rv + "</p></div><div class=\"following-follower-num\"><p class=\"following-num-num\">" + numfollower;
	rv = rv + "</p><p class=\"following-num-text\"> Followers";
	rv = rv + "</p></div></div></div></div>";
	
	return rv;
}

function FormatUserProfile(imgsrc,username,screenname, description, location, numtweets, numfollowing, numfollower, background, somenumber) {
	rv = "<div id=\"user"+ somenumber  +"-profile\" class=\"thumbnail\">"
	rv = rv + "<div class=\"user-info\" style=\"background-image: url('" + background + "');background-size: 100% 100%;background-repeat: no-repeat;\"><img class=\"head-picture\" src=\"" + imgsrc;
	rv = rv + "\"><p class=\"user-name\">" + username;
	rv = rv + "</p><p class=\"user-handle\">" +screenname;
	rv = rv + "</p><p class=\"user-intro\">" + description;
	rv = rv + "</p><p class=\"user-location\">" + location;
	rv = rv + "</p></div><div id=\"user-info-num-" + somenumber + "\"><div class=\"tweet-num\"><p class=\"user-num-num\">" + numtweets;
	rv = rv + "</p><p class=\"user-num-info\"> Tweets";
	rv = rv + "</p></div><div class=\"following-num\"><p class=\"user-num-num\">" + numfollowing;
	rv = rv + "</p><p class=\"user-num-info\">Followings";
	rv = rv + "</p></div><div class=\"follower-num\"><p class=\"user-num-num\">" + numfollower;
	rv = rv + "</p><p class=\"user-num-info\"> Followers";
	rv = rv + "</p></div></div></div>";
	
	return rv;
}

function FormatImageGallery(n, username) {
	var rv = "";
	for (var j = 0; j < n.length; j++) {
	if (n.length == 0) return "";
	rv = rv + "\
<div><h6 class=\"comparison-subtitle\">Images posted by "+ username[j] +"...</h6></div>\
<div id=\"carousel-example-generic-"+j+"\" class=\"carousel slide\" data-ride=\"carousel\">\
  <ol class=\"carousel-indicators\">\
	<li data-target=\"#carousel-example-generic-"+j+"\" data-slide-to=\"0\" class=\"active\"></li>";
	for (var i = 1; i < n[j].length; i++) {
		rv = rv + "\
	<li data-target=\"#carousel-example-generic-"+j+"\" data-slide-to=\"" + i + "\"></li>"
	}
	rv = rv + "\
  </ol>\
  <div class=\"carousel-inner\">";
	rv = rv + "\
    <div class=\"item active\">\
      <img class=\"gallery-img\" src=\"" + n[j][0] + "\">\
    </div>";
	for (var i = 1; i < n[j].length; i++) {
		rv = rv + "\
    <div class=\"item\">\
      <img class=\"gallery-img\" src=\"" + n[j][i] + "\">\
    </div>"
	}
	rv = rv + "\
  </div>\
  <a class=\"left carousel-control\" href=\"#carousel-example-generic-"+j+"\" data-slide=\"prev\">\
    <span class=\"glyphicon glyphicon-chevron-left\"></span>\
  </a>\
  <a class=\"right carousel-control\" href=\"#carousel-example-generic-"+j+"\" data-slide=\"next\">\
    <span class=\"glyphicon glyphicon-chevron-right\"></span>\
  </a>\
</div>"
}

	return rv;
}

function FormatTabs() {
	var rv = "\
		<div id=\"tabs\">\
			<ul class=\"nav nav-tabs nav-justified\">\
				<li class=\"active\"><a class=\"tab-square\" href=\"#topics\" data-toggle=\"tab\">TOPICS</a></li>\
				<li><a class=\"tab-square\" href=\"#people\" data-toggle=\"tab\">PEOPLE</a></li>\
				<li><a class=\"tab-square\" href=\"#media\" data-toggle=\"tab\">MEDIA</a></li>\
			</ul>\
		</div>"
		
	return rv;
}

function FormatComparison() {
	var rv = "<div id=\"comparison\" class=\"tabbable\">";
	rv = rv + "<div class=\"tab-content\">";
	rv = rv + "<div id=\"topics\" class=\"tab-pane fade in active\">";
	rv = rv + "</div>";
	rv = rv + "<div id=\"people\" class=\"tab-pane fade\">"
	rv = rv + "</div>"
	rv = rv + "<div id=\"media\" class=\"tab-pane fade\">"
	rv = rv + "</div>"
	rv = rv + "</div>"
	rv = rv + "</div>"
	
	return rv;
}
				
function FormatTopics(categorylist, topicPercentage) {
	var rv = "\
		<div><h6 class=\"comparison-subtitle\" style=\"margin-bottom: 0px\">They are talking about...</h6></div>\
		<div class=\"word-cloud\">\
			<wordcloud></wordcloud>\
		</div>\
		<div><h6 class=\"comparison-subtitle\">What kinds of things do they talk about...</h6></div>\
		<div class=\"panel-group\" id=\"topic-panel\">\
			";
	
	for (var i = 0; i < categorylist.length; i++) {
		var subtopics = [];
		var subtopic_percentage = [];
		var entities = categorylist[i].entities;
		var keywords = categorylist[i].keywords;
		for (var j = 0; j < entities.length; j++) {
			subtopics.push(entities[j].text);
			subtopic_percentage.push([j, entities[j].user1frequency, entities[j].user2frequency, parseInt(entities[j].user1frequency) + parseInt(entities[j].user2frequency)]);
		}
		for (var k = 0; k < keywords.length; k++) {
			subtopics.push(keywords[k].keyword);
			subtopic_percentage.push([j + k, keywords[k].user1frequency, keywords[k].user2frequency, parseInt(keywords[k].user1frequency) + parseInt(keywords[k].user2frequency)]);
		}
		rv = rv + FormatTopicPanel(categorylist[i].category, topicPercentage[i], subtopics, subtopic_percentage, "" +(i+1));
	}
	
	return rv;
}

function FormatTopicPanel(panelname, percentage, subtopics, subtopic_percentage, index) {
	var rv = "<div class=\"panel panel-default\">\
				<div class=\"panel-heading topic-panel-heading\" data-toggle=\"collapse\" data-parent=\"#topic-panel\" href=\"#topic"+index+"\">\
					<div class=\"mbar-left-blank\" style=\"width: " + (30 - percentage["user1percentage"] * 100 * .30).toString() + "%\"></div>\
					<div class=\"mbar-left\" style=\"width: " + (5 + percentage["user1percentage"] * 100 * .30).toString() + "%\">\
						<div class=\"topic-percentage\">" + Math.floor(percentage["user1percentage"] * 100) + "%&nbsp;&nbsp;</div>\
					</div>\
					<div class=\"panel-title topic-bar\">" + panelname + "</div>\
					<div class=\"mbar-right\" style=\"width: " + (5 + percentage["user2percentage"] * 100 * .30).toString() + "%\">\
						<div class=\"topic-percentage\">&nbsp;&nbsp;" + Math.floor(percentage["user2percentage"] * 100) + "%</div>\
					</div>\
					<div class=\"mbar-right-blank\" style=\"width: " + (30 - percentage["user2percentage"] * 100 * .30).toString() + "%\"></div>\
				</div>\
				<div id=\"topic"+index+"\" class=\"panel-collapse collapse\">\
				<div class=\"panel-body\">";
	
	subtopic_percentage.sort(function(a, b) {return b[3] - a[3];});
	largest = 0;
	for (var i = 0; i < subtopic_percentage.length; i++) {
		if (subtopic_percentage[i][1] > largest) {
			largest = subtopic_percentage[i][1];
		}
		if (subtopic_percentage[i][2] > largest) {
			largest = subtopic_percentage[i][2];
		}
	}

	for (var i = 0; i < subtopic_percentage.length; i++) {
		var leftwidth = parseFloat(subtopic_percentage[i][1] / largest) * 100;
		var rightwidth = parseFloat(subtopic_percentage[i][2] / largest) * 100;
		rv = rv + FormatTopicKeyword(subtopics[subtopic_percentage[i][0]], leftwidth, rightwidth, panelname);
	}
	rv = rv +"</div></div></div>";	
	
	return rv;
}

function FormatTopicKeyword(keyword, widthleft, widthright, panelname) {
	var rv = "<div class=\"subtopic\">\
					<div class=\"bar-left-outer\"><div class=\"bar-left\" style=\"width: " + (widthleft * 0.4) + "%\"></div></div>\
					<div class=\"subtopic-bar\"   data-toggle=\"modal\" data-target=\"#myModal\" id=\"subtopic-refer\" topic=\"" + panelname + "\">" + keyword + "</div>\
					<div class=\"bar-right-outer\"><div class=\"bar-right\" style=\"width: " + (widthright * 0.4) + "%\"></div></div>\
				</div>";
	return rv;
}
					
function FormatPeople(commonfollowers, user1, user2) {
	var rv = "\
		<h6 class=\"comparison-subtitle\">Common Followings</h6>\
		<div id=\"venn-inner\">\
			<venn id=\"venn\"></venn>\
			<div id=\"venn-explanation\">\
				<div id=\"venn-user1-explanation\">\
					<span id=\"userIcon-1\" class=\"glyphicon glyphicon-user inline-icon\"></span>\
					<p class=\"venn-user\">" + user1 + "</p>\
				</div>\
				<div id=\"venn-user2-explanation\">\
					<span id=\"userIcon-2\" class=\"glyphicon glyphicon-user inline-icon\"></span>\
					<p class=\"venn-user\">" + user2 + "</p>\
				</div>\
			</div>\
		</div>\
		<p class=\"comparison-intro\">There are "+ commonfollowers +" People they both follow</p>\
		<h6 class=\"comparison-subtitle\">They both mention...</h6>\
		<div id=\"mentionslist\"></div>\
		<h6 class=\"comparison-subtitle\">Common followings</h6>\
		<div id=\"common-following\"></div>\
		\
		\
		<div id=\"mentionslist\"></div>\
		<div id=\"tweetstest\"></div>\
		<div id=\"userprofiles\"></div>\
		<div id=\"followerlist\"></div>\
	"
	
	return rv;
}
				