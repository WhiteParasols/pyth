const open = document.getElementById("open");
const close = document.getElementById("close");
const modal = document.querySelector('.modal-wrapper');
// = const modal = document.getElementsByClassName('modal-wrapper')[0];

open.onclick = () => {
    modal.style.display='flex';
};
close.onclick = () => {
    modal.style.display='none';
};
