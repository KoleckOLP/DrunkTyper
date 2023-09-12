var value
var oldvalue

var text = ""

var length = 0
var max = 0

var last_correct_length = 0

var timer1
var took1

var started = false
var cheating = false

$(document).ready(function () { // runs one time once the page loads
    var input = $("#user-input")
    var text1 = $("#text1")
    var took1 = $("#took1")

    text = text1.text()
    max = text.length

    input.val("") // clears the textbox on firefox

    input.keyup(function () { // runs on each keypress in textarea
        value = input.val();
        length = value.length

        // start timer
        if (oldvalue === undefined & value !== undefined) {
            start_additive_timer()
            started = true
        }

        if (value != oldvalue) { // prevents stuff being run twice if text didn't change

            // colors
            if (text.slice(0, length) == value) {
                correct = true
                text1.html(`<span id=\"correct\">${text.slice(0, length)}</span>${text.slice(length)}`)
                last_correct_length = length
            }
            else {
                correct = false
                wrong_text = text.slice(last_correct_length, length).replaceAll(' ', '·')
                wrong_text = wrong_text.replace('\n', "↵\n")
                text1.html(`<span id=\"correct\">${text.slice(0, last_correct_length)}</span><span id=\"wrong\">${wrong_text}</span>${text.slice(length)}`)
            }
        }

        // anti-cheat
        if(oldvalue !== undefined) {
            if (length-oldvalue.length >= max/4) {
                cheating = true
            }
        }

        // stop timer
        if ((length == max && correct && started) || cheating) {
            stop_additive_timer()
            started = false
            input.prop('readonly', true)
            if (cheating) {
                took1.text("cheating: Wrote more the 1/8th of the text in one text area refresh.")
            }
            else {
                wpm = ((text.split(" ")).length / tooktime) * 60
                wpm5 = ((max / 5) / tooktime) * 60
                took1.text(took1.text() + `${wpm.toFixed(2)} rWPM ${wpm5.toFixed(2)} aWPM`)
            }
        }

        oldvalue = value

        function start_additive_timer() {
            var startTime = Date.now();
            timer1 = setInterval(function () {
                var elapsedTime = Date.now() - startTime;
                tooktime = (elapsedTime / 1000).toFixed(2)
                took1.text(tooktime + "s ")
            }, 10);
        }

        function stop_additive_timer() {
            clearInterval(timer1)
        }
    })
})
