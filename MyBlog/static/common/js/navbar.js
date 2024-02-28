


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





function signup(){
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
        console.log(data.non_field_errors);
        if(data.email){
            document.getElementById('emailHelp').innerText = data.email
        }
        else if(data.non_field_errors){
            document.getElementById('register_non_field_error').innerText = data.non_field_errors
        }
    })
}


function login(){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    var x = document.getElementById('login-btn').innerHTML += `<i class="fa fa-spinner fa-spin"></i>`

    console.log(x);

    fetch('auth/signin/',{
        method: "POST",
        headers : {'X-CSRFTokens' : csrftoken},
        body : new FormData(document.getElementById('login-form'))
    })
    .then((response)=>{
        if(response.ok){
            window.location.href = '/';
        }
        else{
            return response.json()
        }
    })
    .then((data)=>{

        console.log(data);
        document.getElementById('login-btn').innerHTML = "Login"
        
        if(data.non_field_errors){
            document.getElementById('login_non_field_error').innerText = data.non_field_errors;
        }
        else if(data.email){
            document.getElementById('loginEmailError').innerText = data.email;
        }
        else if(data.password){
            document.getElementById('passwordError').innerText = data.password;
        }
        // window.location.href = '/';
    })
}



function clearSignupFormData(){
    document.getElementById('signup-form').reset();
    document.getElementById('register_non_field_error').innerHTML="";
}

function clearLoginFormData(){
    document.getElementById('login-form').reset();
    document.getElementById('login_non_field_error').innerHTML = "";
    document.getElementById('loginEmailError').innerHTML = "";
    document.getElementById('passwordError').innerHTML = "";
}



function get_profile_image() {


    fetch('http://127.0.0.1:8000/user/api/profiledata/')
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log(data);
        document.getElementById('profile_image').src = data.profile_img;
    })

}

get_profile_image()


function appendBlogs(value,idx,arr){
    block = document.querySelector('.all_blog_wrapper')
    console.log(value.title)
    block.innerHTML += `                    
    <div class="blog_card px-5 mt-5">
        <div class="blog_content">
            <h3 class="fw-bold">${value.title}</h3>
            <p>${value.content}</p>
        </div>
        <div class="blog_img">
            <img src="${value.blog_image}" alt="">
        </div>
    </div>`
}

function get_all_blogs(){
    fetch('http://127.0.0.1:8000/blog/api/getallblogs/')
    .then((response)=>{
        return response.json();
    })
    .then((data)=>{
        data.forEach(appendBlogs);
    })
}

get_all_blogs()