$(document).ready(function() {
    $('.carousel').on('slid.bs.carousel', function () {
        var index = $('.carousel-item.active').index();
        $('.list-group-item').removeClass('active');
        $('.list-group-item').eq(index).addClass('active');
    });
});

function changeSlide(imageId) {
    $('.carousel-item').removeClass('active');
    $('#' + imageId).closest('.carousel-item').addClass('active');
}