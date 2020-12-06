/* jQuery compliant JS for base.html */

$(document).ready(function () {
  //This call triggers when a specific feeds news is clicked.

  $(".navbar-item").click(function () {
    // $target defines the attribute being clicked by the user
    let $target = $(this).attr("href");

    // Hides all news-boxes, this is to make sure the page does not become cluttered and you can review one feed at a time.
    $(".news-box").css("display", "none");
    $("" + $target).fadeIn(1500);
  });
});
