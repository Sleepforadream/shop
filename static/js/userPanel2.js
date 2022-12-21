let popup = document.querySelector('.user-popup'); // Само окно
let popupActive = document.querySelector('.user-popup.active');
let openPopupButton = document.querySelector('.menu-user-panel'); // Кнопки для показа окна
let userBlock = document.querySelector('.user-box');

let coords = openPopupButton.getBoundingClientRect();
let left2 = coords.left + (openPopupButton.offsetWidth - popup.offsetWidth) / 2;
let top2 = coords.top + openPopupButton.offsetHeight + 7.5;
popup.style.left = left2 + 'px';
popup.style.top = top2 + 'px';

    userBlock.addEventListener('mouseenter', (e) => {
        e.preventDefault();
        popup.classList.add('active');
    });

    userBlock.addEventListener('mouseleave', (e) => { // Вешаем обработчик на весь документ
        popup.classList.remove('active'); // И с окна
    });



