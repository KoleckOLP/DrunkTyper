$(document).ready(function () {
    $.ajax({
        url: "/settings_status",
        type: "POST",
        data: "gib status",
        contentType: "plain/text",
        success: function (response) {
            console.log(response);
            if (response == "nothing") {
                $('input[value=nothing]').prop('checked', true)
            }
            else if (response == "letter") {
                $('input[value=letter]').prop('checked', true)
            }
            else if (response == "word") {
                $('input[value=word]').prop('checked', true)
            }
        },
        error: function (error) {
            console.error(error);
        }
    })

    $('#settings').submit(function (event) {
        $.ajax({
            url: "/settings_input",
            type: "POST",
            data: JSON.stringify({ stopat: $('input[name="stopat"]:checked').val(), wcount: $('input[name="wcount"]').val() }),
            contentType: "application/json",
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.error(error);
            }
        })
        event.preventDefault();
    })
})
