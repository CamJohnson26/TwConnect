$(document).on("click", "#topic-panel", function (event) {
	if (!event.target) {
		return;
	}
	if (event.target.id.split(" ").indexOf("subtopic-refer") != -1) {
		showSubTopicRelatedTweets(event.target.innerHTML, event.target.getAttribute("topic"), event.target.parentNode);
	}
})

function showSubTopicRelatedTweets(subtopic, topic, element) {
	categoryList = window.sessionData.categorylist;
	user1 = window.sessionData.user1name.toUpperCase();
	user2 = window.sessionData.user2name.toUpperCase();
	
	for (var i = 0; i < categoryList.length; i++) {
		if (categoryList[i].category == topic) {
			keywds = categoryList[i].keywords;
			entities = categoryList[i].entities;
			break;
		}
	}

	var tweet1html = "<ul class=\"list-group related-tweets\">";
	var tweet2html = "<ul class=\"list-group related-tweets\">";
	frequency = 0;
	user1count = 0;
	user2count = 0;
	tweets = [];
	
	for (var i = 0; i < keywds.length; i++) {
		if (keywds[i].keyword == subtopic) {
			frequency += keywds[i].frequency;
			user1count += keywds[i].user1count;
			user2count += keywds[i].user2count;
			tweets = tweets.concat(keywds[i].tweets);
			break;
		}
	}
	
	for (var i = 0; i < entities.length; i++) {
		if (entities[i].text == subtopic) {
			frequency += entities[i].frequency;
			user1count += entities[i].user1count;
			user2count += entities[i].user2count;
			tweets = tweets.concat(entities[i].tweets);
			break;
		}
	}
		
		
	for (var i = 0; i < tweets.length; i++) {
		if ("@" + tweets[i].screen_name.toUpperCase() == user1) {
			tweet1html = tweet1html + "<li class=\"list-group-item\">" + FormatTweet(tweets[i].text, tweets[i].user_name, "@" + tweets[i].screen_name, tweets[i].tweetid, tweets[i].date) + "</li>";
		}
		else {
			tweet2html = tweet2html + "<li class=\"list-group-item\">" + FormatTweet(tweets[i].text, tweets[i].user_name, "@" + tweets[i].screen_name, tweets[i].tweetid, tweets[i].date) + "</li>";
		}
	}
	
	tweet1html = tweet1html + "</ul>";
	tweet2html = tweet2html + "</ul>";
	
	document.getElementById("tweet-box").innerHTML = tweet1html + tweet2html;
	document.getElementById("myModalLabel").innerHTML = "\"" + subtopic + "\"-related tweets";
	
	// Draw Tweets
	twttr.widgets.load();
}