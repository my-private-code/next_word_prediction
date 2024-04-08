var data = []
var token = ""

jQuery(document).ready(function () {
    var slider = $('#max_words')
    slider.on('change mousemove', function (evt) {
        $('#label_max_words').text('Top k words: ' + slider.val())
    })

    var slider_mask = $('#max_words_mask')
    slider_mask.on('change mousemove', function (evt) {
        $('#label_max_words').text('Top k words: ' + slider_mask.val())
    })

    $('#input_text').on('keyup', function (e) {
        if (e.key == ' ') {
            $.ajax({
                url: '/get_end_predictions',
                type: "post",
                contentType: "application/json",
                dataType: "json",
                data: JSON.stringify({
                    "input_text": $('#input_text').val(),
                    "top_k": slider.val(),
                }),
                beforeSend: function () {
                    $('.overlay').show()
                },
                complete: function () {
                    $('.overlay').hide()
                }
            }).done(function (jsondata, textStatus, jqXHR) {
                console.log(jsondata)
                $('#text_bert').val(jsondata['bert'])
                $('#text_bert_cn').val(jsondata['bert_cn'])
                // $('#text_bart').val(jsondata['bart'])
                $('#text_electra').val(jsondata['electra'])
            }).fail(function (jsondata, textStatus, jqXHR) {
                console.log(jsondata)
            });
        }
    })

    $('#btn-process').on('click', function () {
        $.ajax({
            url: '/get_mask_predictions',
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                "input_text": $('#mask_input_text').val(),
                "top_k": slider_mask.val(),
            }),
            beforeSend: function () {
                $('.overlay').show()
            },
            complete: function () {
                $('.overlay').hide()
            }
        }).done(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            $('#mask_text_bert').val(jsondata['bert'])
            // $('#mask_text_bart').val(jsondata['bart'])
            $('#mask_text_electra').val(jsondata['electra'])
        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
        });
    })
})