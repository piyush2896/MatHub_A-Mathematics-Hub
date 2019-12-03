/*
Author: Piyush Malhotra
Date modified: 11/14/2019
*/

$(document).ready(function () {
    $('#password, #confirm-password').on('keyup', function () {
        if ($('#password').val() == $('#confirm-password').val()) {
            $('#message').html('Matching').css('color', 'green');
        } else
            $('#message').html('Not Matching').css('color', 'red');
    });
});
