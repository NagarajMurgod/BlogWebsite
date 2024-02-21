


// var cbtn = document.getElementById('category-btn');

// cbtn.addEventListener('click', function () {
    
//     var cat_itms = document.querySelector('.category-items')
//     console.log(cat_itms)
//     var disp = cat_itms.style.display;
//     if (disp === 'block') {
//         cat_itms.style.display = 'none';
//     }
//     else {
//         cat_itms.style.display = 'block'
//     }
//     console.log('wroking');
// })



var signup = document.getElementById('signup');
console.log(signup);

signup.addEventListener('click', function(){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(
        '/auth/signup/',
        {
            method : "POST",
            headers : {'X-CSRFToken': csrftoken},
            body : new FormData(document.getElementById('signup-form'))

        } 
    )
    .then((response) => {
        return response.json()
    })
    .then((data)=>{
        console.log(data);
    })
})


var login = document.getElementById('login-btn')

login.addEventListener('click', function(){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('auth/signin/',{
        method: "POST",
        headers : {'X-CSRFTokens' : csrftoken},
        body : new FormData(document.getElementById('login-form'))
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log(data);
        // window.location.href = 'test/';
    })
})

