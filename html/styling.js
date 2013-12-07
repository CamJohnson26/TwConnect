window.onload = function() {
	$("body").css("padding-top", $(".navbar").css("height"));
	$("#2users").affix({
		offset: {
			top: function () {
				return (this.top = $("#heading").offset().top + $("#heading").height())
			}
		}
	})
}