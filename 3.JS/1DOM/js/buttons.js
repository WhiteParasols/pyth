function number_inc(){
    console.log("증가");
    let number = document.getElementById('result');
    let number_string = number.textContent;
    //div 요소 안에 있는 글을 가져오는 3가지 방식
    //innerText - 글자만 가져온다(디자인 속성을 적용받음)
    //innerHTML - 글자와 태그 함께 가져온다
    //textContent - 순수 글자만 가져온다
    console.log(number_string);

    let number_string_to_number = Number(number_string);
    let result = number_string_to_number+1;
    number.textContent=result;
}
function number_dec(){
    console.log("감소");
    document.getElementById('result').textContent-=1;
}