function reloadWebpage()
{

	xmlhttp=new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
		
			var responseData = jQuery.parseJSON(xmlhttp.responseText);
			window.sessionData = responseData;
			
			//adjustment for existing elements
			$("#heading").css("margin-top", "80px");
			$("#bottom-bar").css("position", "relative");
			
			// Draw Tabs
			$("#intro").after(FormatTabs());
			
			// Draw  comparison
			$("#tabs").after(FormatComparison());
			
			// Draw Topics
			topicPercentage = calculateTopicPercentage(responseData.categorylist, responseData.numberOfTweets, responseData.numberOfTweets);
			document.getElementById("topics").innerHTML = FormatTopics(responseData.categorylist, topicPercentage);
			
			// Draw People
			document.getElementById("people").innerHTML = FormatPeople(responseData.commonfollowercount, responseData.user1displayname, responseData.user2displayname);
			
			// Draw Media
			
 			// Draw User Profiles
			var u1html = FormatUserProfile(responseData.user1image,responseData.user1displayname,responseData.user1name, responseData.user1description, responseData.user1location, responseData.user1tweetcount, responseData.user1friendcount, responseData.user1followercount, responseData.user1background, "1");
			var u2html = FormatUserProfile(responseData.user2image,responseData.user2displayname,responseData.user2name, responseData.user2description, responseData.user2location, responseData.user2tweetcount, responseData.user2friendcount, responseData.user2followercount, responseData.user2background, "2");
			$("#intro").after("<div id=\"profile\" class=\"row\">" + u1html + u2html + "</div>");
					
			// Draw Word Clouds
			drawWordCloud(responseData.wordcloud);
			//drawHashTagCloud(responseData.hashtagcloud);
			
			// Venn Diagram
			vennlabel1 = responseData.user1name +"\n" + responseData.user1friendcount + " Friends";
			vennlabel2 = responseData.user2name +"\n" + responseData.user2friendcount + " Friends";
			drawVenn("", "", responseData.user1friendcount, responseData.user2friendcount, responseData.commonfollowercount);
			$("svg")[1].setAttribute("height", "250px");
			
			//$("#userIcon-1")[0].nextSibling.innerHTML = "<p class=\"venn-user\">"+responseData.user1displayname + ": " + responseData.user1friendcount + " Friends" +"</p>";
			//$("#userIcon-2")[0].nextSibling.innerHTML = "<p class=\"venn-user\">"+responseData.user2displayname + ": " + responseData.user2friendcount + " Friends" +"</p>";
			
			// Draw Common Followers
			var cfarray = responseData.commonfollowers;
			var followerlist = [];
			var commonfollowinghtml = ""
			for (var i = 0; i < cfarray.length; i++) {
			
				var temparray = [];
				for (var j = 0; j < cfarray[i].length; j++) {
					temparray.push(cfarray[i][j]);
				}
				var image = cfarray[i][0];
				var screenname = cfarray[i][1];
				var description = cfarray[i][2];
				var location = cfarray[i][3];
				var friends = cfarray[i][4];
				var followers = cfarray[i][5];
				var username = cfarray[i][6];
				var numtweets = cfarray[i][7];
				var bgimage = cfarray[i][8];

				var curfollowerdiv = FormatUser(image,username,screenname, description, location, numtweets, friends, followers,bgimage)
				commonfollowinghtml = commonfollowinghtml + curfollowerdiv;
			
				followerlist.push(temparray);
			}
			document.getElementById("common-following").innerHTML = commonfollowinghtml;

			// Draw Common Mentions
			var cmarray = responseData.commonmentions;
			var mentionlist = [];
			var commonmentionhtml = ""
			for (var i = 0; i < cmarray.length; i++) {
			
				var temparray = [];
				for (var j = 0; j < cmarray[i].length; j++) {
					temparray.push(cmarray[i][j]);
				}
				var image = cmarray[i][0];
				var screenname = cmarray[i][1];
				var description = cmarray[i][2];
				var location = cmarray[i][3];
				var friends = cmarray[i][4];
				var followers = cmarray[i][5];
				var username = cmarray[i][6];
				var numtweets = cmarray[i][7];
				var bgimage = cmarray[i][8];
				
				var curfollowerdiv = FormatUser(image,username,screenname, description, location, numtweets, friends, followers,bgimage);
				commonmentionhtml = commonmentionhtml + curfollowerdiv;
			
				mentionlist.push(temparray);
			}
			if (mentionlist.length == 0) {
				commonmentionhtml = "<p class=\"comparison-intro\">No Common Mentions</p>";
			}
			document.getElementById("mentionslist").innerHTML = commonmentionhtml;
			
			// Draw Tweets
			
			window.responseData = responseData;
			
			// Draw Gallery
			mediahtml = FormatImageGallery(new Array(responseData.media1, responseData.media2), new Array(responseData.user1displayname, responseData.user2displayname));
 			document.getElementById("media").innerHTML = mediahtml;
			
			$("#compare-btm").button('reset');
		}
	}
	
	xmlhttp.open("POST","/userinput",true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	
	var name1 = document.getElementById('user1input').value;
	var name2 = document.getElementById('user2input').value;
	
	var datatosend = "user1input=" + name1 + "&user2input=" + name2;
	xmlhttp.send(datatosend);
	
	$("#compare-btm").button('loading');
}

function calculateTopicPercentage(categorylist, user1TotalTweet, user2TotalTweet) {
	var percentages = [];
	
	for (var i = 0; i < categorylist.length; i++) {
		cat = categorylist[i];
		user1frequency = 0;
		user2frequency = 0;
		for(var j = 0; j < cat.entities.length; j++) {
			user1frequency = user1frequency + parseFloat(cat.entities[j].user1frequency);
			user2frequency = user2frequency + parseFloat(cat.entities[j].user2frequency);
		}
		for(var j = 0; j < cat.keywords.length; j++) {
			user1frequency = user1frequency + parseFloat(cat.keywords[j].user1frequency);
			user2frequency = user2frequency + parseFloat(cat.keywords[j].user2frequency);
		}
		var percentage = {"user1percentage": user1frequency / user1TotalTweet, "user2percentage": user2frequency / user2TotalTweet};
		percentages.push(percentage);
	}
	
	return percentages;
}