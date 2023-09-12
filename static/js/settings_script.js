$(document).ready(function () {
    $.ajax({
        url: "/settings_status",
        type: "POST",
        data: "gib status",
        contentType: "json",
        success: function (response) {
            stopat = response.stopat
            wcount = response.wcount
            if (stopat == "nothing") {
                $('input[value=nothing]').prop('checked', true)
            }
            else if (stopat == "letter") {
                $('input[value=letter]').prop('checked', true)
            }
            else if (stopat == "word") {
                $('input[value=word]').prop('checked', true)
            }

            $('input[name=wcount]').val(wcount)
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
                alert("Settings were saved.")
            },
            error: function (error) {
                console.error(error);
            }
        })
        event.preventDefault();
    })
})
