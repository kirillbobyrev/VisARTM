$(function() {
    $('.btn-assess').click(function() {
        debugger;
        var term_name = $($(this).parent().parent().find('td')[2]).text().trim();
        $.ajax({
            url: '/assess',
            data: {
                term_name: term_name
            },
            type: 'POST',
            success: function(response) {
                alert('ABCD');
            },
            error: function(error) {
            }
        });
    });
});
