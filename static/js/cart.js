$('.update-link').click(function (e) {
    var form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function (e) {
    console.log("this is working")
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var size = $(this).data('product_size');
    var url = `/cart/remove/${itemId}/`;
    var data = {
        'csrfmiddlewaretoken': csrfToken,
        'product_size': size
    };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
})