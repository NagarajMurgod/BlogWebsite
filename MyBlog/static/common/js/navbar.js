


var cbtn = document.getElementById('category-btn');
console.log(cbtn)
cbtn.addEventListener('click', function () {

    var cat_itms = document.querySelector('.category-items')
    console.log(cat_itms)
    var disp = cat_itms.style.display;
    if (disp === 'block') {
        cat_itms.style.display = 'none';
    }
    else {
        cat_itms.style.display = 'block'
    }
    console.log('wroking');
})





function signup() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(
        '/auth/signup/',
        {
            method: "POST",
            headers: { 'X-CSRFToken': csrftoken },
            body: new FormData(document.getElementById('signup-form'))

        }
    )
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log(data)
            if (data.non_field_errors) {
                document.getElementById('register_non_field_error').innerText = data.non_field_errors
            }
            else if(data.email){
                document.getElementById('emailHelp').innerHTML = data.email
            }
        })
}


function login() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    var x = document.getElementById('login-btn').innerHTML += `<i class="fa fa-spinner fa-spin"></i>`

    console.log(x);

    fetch('auth/signin/', {
        method: "POST",
        headers: { 'X-CSRFTokens': csrftoken },
        body: new FormData(document.getElementById('login-form'))
    })
        .then((response) => {
            if (response.ok) {
                window.location.href = '/';
            }
            else {
                return response.json()
            }
        })
        .then((data) => {

            console.log(data);
            document.getElementById('login-btn').innerHTML = "Login"

            if (data.non_field_errors) {
                document.getElementById('login_non_field_error').innerText = data.non_field_errors;
            }
            else if (data.email) {
                document.getElementById('loginEmailError').innerText = data.email;
            }
            else if (data.password) {
                document.getElementById('passwordError').innerText = data.password;
            }
            // window.location.href = '/';
        })
}



function clearSignupFormData() {
    document.getElementById('signup-form').reset();
    document.getElementById('register_non_field_error').innerHTML = "";
}

function clearLoginFormData() {
    document.getElementById('login-form').reset();
    document.getElementById('login_non_field_error').innerHTML = "";
    document.getElementById('loginEmailError').innerHTML = "";
    document.getElementById('passwordError').innerHTML = "";
}



function get_profile_image() {


    fetch('http://127.0.0.1:8000/user/api/profiledata/')
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log(data);
            document.getElementById('profile_image').src = data.profile_img;
        })

}

get_profile_image()


