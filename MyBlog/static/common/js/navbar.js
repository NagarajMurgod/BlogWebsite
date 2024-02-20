


var cbtn = document.getElementById('category-btn');
var cat_itms = document.querySelector('.category-items')
console.log(cat_itms)

cbtn.addEventListener('click', function(){
    var disp = cat_itms.style.display;
    if(disp === 'block'){
        cat_itms.style.display = 'none';
    }
    else{
        cat_itms.style.display = 'block'
    }
    console.log('wroking');
})



