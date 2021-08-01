$(function () {
  if (location.pathname !== '/') {
    $('nav a').removeClass('active');
    $('nav a[href^="/' + location.pathname.split("/")[1] + '"]').addClass('active');
  }
});

