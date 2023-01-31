

$(document).ready(function () {
    $('#usernamevalidation').hide();
    $('#passwordvalidation').hide();
    $('#confirmpasswordvalidation').hide();

    var username_error = true;
    var email_error = true;
    var passowrd_error = true;
    var confirm_password_error = true;

    $('#username').keyup(function () {
        username_validation();
    });

    function username_validation() {
        var username_val = $('#username').val();
        if (username_val.length == '') {
            $('#usernamevalidation').show();
            $('#usernamevalidation').html('Nombre de usuario no puede estra vacio');
            $('#usernamevalidation').css('color', 'red');
            username_error = false;
            return false;
        }
        else {
            $('#usernamevalidation').hide();
        }

        if (username_val.length <= 4) {
            $('#usernamevalidation').show();
            $('#usernamevalidation').html('El nombre de usuario debe contener más de 4 caracteres');
            $('#usernamevalidation').css('color', 'red');
            username_error = false;
            return false;
        }
        else {
            $('#usernamevalidation').hide();
        }
    }

    $('#email').keyup(function () {
        email_validation();
    });

    function email_validation() {
        var email = /^([\-\.0-9a-zA-Z]+)@([\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
        var email_val = $('#email').val();
        if (email_val.length == '') {
            $('#emailvalidation').show();
            $('#emailvalidation').html('El correo electrónico no puede estar vacío');
            $('#emailvalidation').css('color', 'red');
            email_error = false;
            return false;
        }
        else {
            $('#emailvalidation').hide();
        }

        if (!email.test(email_val)) {
            $('#emailvalidation').show();
            $('#emailvalidation').html('Por favor, escriba el correo electrónico en el formato correcto. Ej.: xqz@dominio.com');
            $('#emailvalidation').css('color', 'red');
            email_error = false;
            return false;
        }
        else {
            $('#emailvalidation').hide();
        }
    }

    $('#password').keyup(function () {
        password_validation();
    });

    function password_validation() {
        var password1 = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
        var password_val = $('#password').val();
        if (password_val.length == '') {
            $('#passwordvalidation').show();
            $('#passwordvalidation').html('La contraseña no puede estar vacía');
            $('#passwordvalidation').css('color', 'red');
            passowrd_error = false;
            return false;
        }
        else {
            $('#passwordvalidation').hide();
        }

        if (password_val.length <= 7) {
            $('#passwordvalidation').show();
            $('#passwordvalidation').html('La contraseña debe contener al menos 8 caracteres');
            $('#passwordvalidation').css('color', 'red');
            passowrd_error = false;
            return false;
        }
        else {
            $('#passwordvalidation').hide();
        }

        if (!password1.test(password_val)) {
            $('#passwordvalidation').show();
            $('#passwordvalidation').html(`La contraseña debe contener:
            1. Letras minúsculas y mayúsculas
            2. Al menos un carácter especial
            3. Al menos un número`);
            $('#passwordvalidation').css('color', 'red');
            passowrd_error = false;
            return false;
        }
        else {
            $('#passwordvalidation').hide();
        }


    }


    $('#confirmpassword').keyup(function () {
        confirm_password();
    });

    function confirm_password() {
        var confirm_password_val = $('#confirmpassword').val();
        var password_val = $('#password').val();

        if (password_val != confirm_password_val) {
            $('#confirmpasswordvalidation').show();
            $('#confirmpasswordvalidation').html('Las contraseñas no coinciden');
            $('#confirmpasswordvalidation').css('color', 'red');
            $('#green-tick').css('background-color', '').css('color', '')
            confirm_passowrd_error = false;
            return false;
        }
        else {
            $('#confirmpasswordvalidation').hide();
            $('#green-tick').css('background-color', 'green').css('color', 'white')
        }
    }


    $('#submitvalidation').click(function () {
        username_validation();
        password_validation();
        confirm_password();
        email_validation();

        if (username_error == true && passowrd_error == true && confirm_password_error == true && email_error == true) {
            alert("Debe completar todos los campos correctamente.")
            return true;
        }
        else {
            alert("Formulario enviado con éxito");
            location.href="/html/registro.html";
            return false;
        }

    });d

});

function myFunction() {
    location.href="/html/registro.html";
  }
