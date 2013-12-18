$(document).ready(function(){

    // Enquiry form
  $('#contact-pyladies').validate({
        rules: {
            'cm-name': {
                required: true
            },
            'cm-jhkihd-jhkihd': {
                required: true,
                email: true
            }
        },
        messages: {
            'cm-name': 'Please provide your name',
            'cm-jhkihd-jhkihd': 'Please provide your email address'
        },
        errorPlacement: function(error, element){
            error.insertAfter(element).addClass('val-error');
        },
        submitHandler: function(form) {
            form.submit();
        }
    });

    $('#fieldflyut').keyup(function() {
        count = this.value.length;
        remaining = 250 - count;
        $('#char-count').text(remaining);

        if (remaining == 1){
            $('#plural').hide()
        } else {
            $('#plural').show()
        }
    });
});