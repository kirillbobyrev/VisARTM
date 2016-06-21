$(function() {
    $('.btn-assess').click(function() {
        child = $(this).find('span');

        var value_to_btn_class = new Map();
        value_to_btn_class.set(-1, 'glyphicon-minus');
        value_to_btn_class.set(0, 'glyphicon-unchecked');
        value_to_btn_class.set(1, 'glyphicon-plus');

        var current_value = parseInt($(this).attr('score'));

        child.toggleClass(value_to_btn_class.get(current_value));

        var next_value = current_value + 1;
        if (next_value > 1) {
            next_value = -1;
        }

        child.addClass(value_to_btn_class.get(next_value));
        $(this).attr('score', next_value);

        $.ajax({
            url: '/assess',
            data: {
                class_name: $(this).attr('class_name'),
                arg_list: $(this).attr('arg_list'),
                score: $(this).attr('score')
            },
            type: 'POST',
            success: function(response) {},
            error: function(error) {}
        });
    });
});
