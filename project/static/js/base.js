$(".dots_for_box").on("click", function (event) {
    event.stopPropagation();
    $(".base_box_top").slideToggle("fast");
});

document.addEventListener('mouseup', function(e) {
    var container = document.getElementById('base_box_top');
    if (!container.contains(e.target)) {
        container.style.display = 'none';
    }
});