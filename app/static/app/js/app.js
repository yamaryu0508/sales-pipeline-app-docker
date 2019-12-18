$(function () {

    // Bootstrap Datepicker
    $('.dateinput').datepicker({
        todayBtn: 'linked',
        format: 'yyyy-mm-dd',
        language: 'ja',
        autoclose: true,
        todayHighlight: true,
    });
    $('.dateinput').attr('placeholder','YYYY-MM-DD');

    $('.datetimeinput').attr('placeholder','YYYY-MM-DD HH:MM:SS');

    $('#input-form').on('sumbit', function (e) {
        e.preventDefault();
    })

    $('.save').on('click', function (e) {
        $('.save').addClass('disabled');
        $('#input-form').submit();
    })

    $('.delete').on('click', function (e) {
        $('.delete').addClass('disabled');
    })

    var conditions = $('#filter').serializeArray();
    $.each(conditions, function () {

        if ($('[name=' + this.name + ']').hasClass('nullbooleanselect') && this.value == 1) {
            return;
        }

        if (this.value) {
            $('.filtered').css('visibility', 'visible');
        }
    })

    $(".pagination").rPage();
});