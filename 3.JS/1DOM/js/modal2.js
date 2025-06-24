const open = document.getElementById("open");
const close = document.getElementById("close");
const modal = document.querySelector('.modal-wrapper');
// = const modal = document.getElementsByClassName('modal-wrapper')[0];

open.onclick = () => {
    modal.style.display='flex';
};

function showModal(){
    //모달창 껍데기(div) 만들기
    const modalWrapper=document.createElement('div');
    modalWrapper.className='modal-wrapper';

    modalWrapper.innerHTML =`
        <div class="modal">
            <div class="modal-title">모달 타이틀</div>
            <p>모달 본문</p>
            <div class="close-wrapper">
                <button id="close">닫기</button>
            </div>
        </div> 
    `;
    document.body.appendChild(modalWrapper);

    //닫기버튼 추가
    document.getElementById('close').onclick = () => {
        modalWrapper.remove();
    }
}