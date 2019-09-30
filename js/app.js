$(document).ready(function(){
    $("#login").validate({
        errorClass: 'is-invalid',
        rules:{
            email:{
                required:true,
                email:true
            },
            contraseña:{
                required:true,
                minlength:8,
                maxlength:16
            }
        },
        messages:{
            email:{
                required:"Este campo no debe estar vacío",
                email:"Debe ser en formato email"
            },
            contraseña:{
                required:"Este campo no puede estar vacío",
                minlength:"Debe tener un minimo de 8 caracteres",
                maxlength:"Debe tener un maximo de 16 caracteres"
            }
        }
    });
    $('#registro').validate({
        errorClass: 'is-invalid',
        rules:{
            regNombre:{
                required:true,
                maxlength:35
            },
            regApellido:{
                required:true,
                maxlength:35
            },
            regEmail:{
                required:true,
                email:true
            },
            regNumero:{
                required:false,
            },
            newPass:{
                required:true,
                minlength:8,
                maxlength:16
            }
        },
        messages:{
            regNombre:{
                required:"Este campo no puede estar vacio"
            },
            regApellido:{
                required:"Este campo no puede estar vacio",
                maxlength:35
            },
            regEmail:{
                required:"Este campo no puede estar vacio",
                email:"Debe ser en formato de mail"
            },
            newPass:{
                required:"Este campo no puede estar vacio",
                minlength:"Debe tener un minimo de 8 caracteres",
                maxlength:"Debe tener un maximo de 16 caracteres"
            }
        }
    })
    $('#recuperacion').validate({
        errorClass: 'is-invalid',
        rules:{
            mailRecu:{
                required:true,
                email:true
            }
        },
        messages:{
            mailRecu:{
                required:"Porfavor ingrese su correo",
                email:"Debe ser formato de email"
            }
        }
    })
    $( ".respErronea" ).click(function() {
        swal("Muy cerca, mas suerte la próxima!");
    });
    $( ".respCorrec" ).click(function() {
        swal("Bien Hecho!", "Se nota que sabes", "success");
    });
});