document.addEventListner("DOMContentLoaded",function(){
    //여기는 브라우저가 dom을 다 불러왔을 때 호출됨.
    let fruitSelector=document.getElementById("fruitSelector");
    fruitSelector.addEventListener('change',function(){
        console.log('변경감지됨');
    })
})
function fruitDisplay(){
    let fruit=document.getElementById("fruitSelector").value;
    let result=document.getElementById("fruitResult");
    switch(fruit){
        case 'APPLE':
        case 'apple':
            result.innerText='사과입니다';
            break;
        case 'BANANA':
        case 'banana':
            result.innerText='바나나입니다';
            break;
        case 'ORANGE':
        case 'orange':
            result.innerText='오렌지입니다';
            break;
        case 'PINEAPPLE':
        case 'pineapple':
            result.innerText='파인애플입니다';
            break;
        default:
            result.innerText='몰라요';
    }
}