
// отправка числа на сервер и получение ответа
$(document).ready(function(){
    var form = $('#prime-factors');
    // сам аякс-запрос
    var get_prime_factors = function() {
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: form.serialize(),
            success: function (data) {
                $('#result').html(data)
            }
        });
    };

    // вешаем запрос на любое из действий над инпутом: ввод с клавиатуры, вставка, клик
    $('#number').on('keyup paste', function(){
        get_prime_factors();
    });

    // вешаем запрос на подтверждение формы (если нажать enter)
    form.on('submit', function(e){
        e.preventDefault();
        get_prime_factors();
    })
});