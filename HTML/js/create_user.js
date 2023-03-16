
local_host = 'http://127.0.0.1:8888/';

let submit_button = document.getElementById("submit");


submit_button.addEventListener('click', event=> 
{
    const user = document.getElementById('user');
    const email = document.getElementById('email');
    

    const password = document.getElementById('password');
    const id = document.getElementById('id');
    const name = document.getElementById('name');

    if (!user.checkValidity() | !email.checkValidity() | !password.checkValidity() | !id.checkValidity() | !name.checkValidity() )
    {
        document.getElementById('error-logger').innerHTML = 'Complete todos los campos de manera correcta.';
    } else
      {
        orchestrator(user.value, email.value, password.value, id.value, name.value);
      }
});


/**
 * Función que nos ayuda a ejecutar nuestras funciones. Es async para que nos permita 
 * hacer await y que se completen los procesos de get antes de seguir con el 
 * flujo de programa.
 * @param {string} user Campo de usuario.
 * @param {string} email Campo de email.
 * @param {string} password Campo de contraseña.
 * @param {string} id Campo de cédula.
 * @param {string} name Campo de nombre.
 */
async function orchestrator(user, email, password, id, name)
{

    let emailExists = await checkAttributes(local_host + 'getEmailExists/' + email);
    let userExists = await checkAttributes(local_host + 'getUserExists/' + user);

    if (emailExists == false & userExists == false)
    {
        createUserInDb(user, email, password, id, name);
        window.location.replace('home.html');
    } else
      {
        let errorMessage = '';

        if (userExists)
        {
            errorMessage = 'El usuario ya se encuentra registrado.'
        }

        if(emailExists)
        {
            errorMessage += '<br>El correo ya se encuentra registrado.'
        }
        document.getElementById('error-logger').innerHTML = errorMessage;
      }
    
}

/**
 * Hace un llamado post al API de python y crea el usuario en nuestra base de datos.
 * @param {string} user Campo de usuario.
 * @param {string} email Campo de email.
 * @param {string} password Campo de contraseña.
 * @param {string} id Campo de cédula.
 * @param {string} name Campo de nombre.
 */
function createUserInDb(user, email, password, id, name)
{

    const apiUrl = local_host + 'postUser/';
    let finalUrl = apiUrl.concat(user , '-', password , '-' , email , '-' , id, '-' , name);
    fetch(finalUrl, 
    {
        method: 'POST',
        headers:
        {
            accept: 'application/json'
        }
    });
}


/**
 * Hace un llamado al API de python que se le indica para validar campos
 *
 * @param {string} finalUrl API al cuál debe de llamar.
 * @return {boolean} Si el campo fue encontrado o no.
 */
async function checkAttributes(finalUrl)
{

    let response = await fetch(finalUrl);

    let data = await response.json();

    let result = await data.Exists === 'True';

    return result
}