var value
var length = 0
var status
var last_correct_length = 0
var wrong_text = ""
var started = false
var max = 0
var ended = false
var running
var finished = false

var time1
var time2

var tooktime
var oldvalue = ""

var cheating

var dick = 0

$(document).ready(function(){
    var input = $("#user-input")
    var text1 = $("#text1")
    var debug = $("#debug")
    var took1 = $("#took1")

    var text = text1.text()

    debug.text(`${started} ${ended} ${length} ${max} ${dick}`)

    input.keyup(function() {
        value = input.val();
    
        length = value.length
        max = text.length

        // started
        if (length > 0 && started == false && finished == false) {
            started = true
            finished = false
            ended = false
            time1 = $.now()
        }

        // ended
        if (length == max && status && started) {
            ended = true
            started = false
            time2 = $.now()
            //console.log(time2 - time1) // this thing finally prove that the timer works
        }

        // colors
        if (text.slice(0, length) == value ) {
            if (value.length-oldvalue.length > max/2) {
                cheating = true
                started = false
                ended = true
            }
            status = true
            text1.html(`<span id=\"correct\">${text.slice(0, length)}</span>${text.slice(length)}`)
            last_correct_length = length
            oldvalue = value
        }
        else {
            status = false
            wrong_text = text.slice(last_correct_length, length).replaceAll(' ', '·')
            wrong_text = wrong_text.replace('\n', "↵\n")
            text1.html(`<span id=\"correct\">${text.slice(0, last_correct_length)}</span><span id=\"wrong\">${wrong_text}</span>${text.slice(length)}`)
        }

        // timer
        if (started && !running) {
            dick = dick + 1
            var startTime = Date.now();
        
            setInterval(function() {
                running = true
                if (started) {
                    var elapsedTime = Date.now() - startTime;
                    tooktime = (elapsedTime / 1000).toFixed(2)
                    took1.text(tooktime+"s ")
                }
            }, 10);
        }
        else {
            running = false
            if (ended && finished == false && !cheating) {
                finished = true
                wpm = ((text.split(" ")).length / tooktime) * 60
                wpm5 = ((max / 5) / tooktime ) * 60
                took1.text(took1.text()+`${wpm.toFixed(2)} rWPM ${wpm5.toFixed(2)} aWPM`)
            }
            else if (cheating) {
                took1.text("You are cheating")
            }
        }

        debug.text(`${started} ${ended} ${length} ${max} ${dick}`)
    })
})


