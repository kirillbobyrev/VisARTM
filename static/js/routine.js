$(function() {
    $('.btn-assess').click(function() {
        $.ajax({
        url: '/assess',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            alert('abcd');
        },
        error: function(error) {
        }
        });
    });
});
