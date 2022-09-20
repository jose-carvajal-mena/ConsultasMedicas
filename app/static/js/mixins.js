let si = document.querySelector('#si');

si.addEventListener('click',()=>{
    let tiempo = document.querySelector('#tiempo');
    tiempo.disabled = false;
});

no.addEventListener('click',()=>{
    let tiempo = document.querySelector('#tiempo');
    tiempo.value = 0;
    tiempo.disabled = true;
});