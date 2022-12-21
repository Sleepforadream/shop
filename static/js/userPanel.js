    let popup = document.querySelector('.user-popup'); // Само окно
    let popupActive = document.querySelector('.user-popup.active');
    let openPopupButton = document.querySelector('.menu-user-panel'); // Кнопки для показа окна
    let userBlock = document.querySelector('.user-box');
    let userText = document.querySelectorAll('.input-text-user-popup');

    let coords = openPopupButton.getBoundingClientRect();
    let left2 = coords.left + (openPopupButton.offsetWidth - popup.offsetWidth) / 2;
    let top2 = coords.top + openPopupButton.offsetHeight + 7.5;
    popup.style.left = left2 + 'px';
    popup.style.top = top2 + 'px';

    userBlock.addEventListener('mouseenter', (e) => {
        e.preventDefault();
        popup.classList.add('active');

        userBlock.addEventListener('mouseleave', (e) => { // Вешаем обработчик на весь документ
        popup.classList.remove('active'); // И с окна
        });
    });

    userText.forEach((elem) => { // Перебираем все кнопки
        elem.addEventListener('click', (e) => {
            e.preventDefault();
            popup.classList.remove('active');
            popup.classList.add('activetwo');
        })

        document.addEventListener('click', (e) => { // Вешаем обработчик на весь документ
        if(e.target !== elem) { // Если цель клика - фот, то:
        popup.classList.remove('activetwo'); // И с окна
        }
        });
    });



//    userBlock.addEventListener('click', function (e) {
//    if (popup.classList.contains("active2")) {
//        popup.classList.remove('active2');
//        }
//    })


