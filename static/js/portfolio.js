$(document).ready(getMaxHeight);

function getMaxHeight() {            
    var maxHeight = -1;
    $('.panel').each(function() {
        maxHeight = maxHeight > $(this).height() ? maxHeight : $(this).height();
    });
    setHeight(maxHeight);
}

function setHeight(maxHeight) {
    $('.panel').each(function() {
        if ($(this).height() == maxHeight) {
            $(this).addClass("tall-panel");
        } else {
            $(this).addClass("short-panel");
        }
    });

    $('.short-panel').css('height',$('.tall-panel').height());
}

$(window).resize(function () {
    $('.short-panel').css('height',$('.tall-panel').height());
});

