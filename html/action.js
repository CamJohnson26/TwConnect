/* $("#subtopic-refer").click( function() {
	$("#tweet-box").css("display", "inline-block");
	$("#backgroundDarkener").css("display", "inline-block");
    left = $(document).width() / 2 - $("#tweet-box").width() / 2;
	$("#tweet-box").css("left", left.toString() + "px")
}) */

$('#myModal').on('show.bs.modal', function () {
	$(".navbar").css("z-index", "1");
	$(".affix").css("z-index", "2");
	$(".affix-top").css("z-index", "2");
})

$('#myModal').on('hidden.bs.modal', function () {
	$(".navbar").css("z-index", "1030");
	$(".affix").css("z-index", "1031");
	$(".affix-top").css("z-index", "1031");
})