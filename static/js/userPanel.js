    window.onload = function() {

    let popup = document.querySelector('.user-popup'); // Само окно
    let popupActive = document.querySelector('.user-popup.active');
    let popupActive2 = document.querySelector('.user-popup.activetwo');
    let openPopupButton = document.querySelector('.menu-user-panel'); // Кнопки для показа окна
    let userBlock = document.querySelector('.user-box');
    let userCheckbox = document.querySelector('.remember-checkbox');
    let userLogin = document.querySelector('.input-login-user-popup');
    let userPassword = document.querySelector('.input-password-user-popup');
    let userLoginButton = document.querySelector('.button-box-enter-user');
    let userRegister = document.querySelector('.menu-login-box-register');

    let coords = openPopupButton.getBoundingClientRect();
    let left2 = coords.left + (openPopupButton.offsetWidth - popup.offsetWidth) / 2;
    let top2 = coords.top + openPopupButton.offsetHeight + 7.5;
    popup.style.left = left2 + 'px';
    popup.style.top = top2 + 'px';

    window.onresize = function() {
        let coords = openPopupButton.getBoundingClientRect();
        let left2 = coords.left + (openPopupButton.offsetWidth - popup.offsetWidth) / 2;
        let top2 = coords.top + openPopupButton.offsetHeight + 7.5;
        popup.style.left = left2 + 'px';
        popup.style.top = top2 + 'px';
    }


    userBlock.addEventListener('mouseenter', (e) => {
        popup.classList.add('active');

        userLogin.addEventListener('click', (e) => {
            popup.classList.add('activetwo');
        });

        userPassword.addEventListener('click', (e) => {
            popup.classList.add('activetwo');
        });

        userCheckbox.addEventListener('click', (e) => {
            popup.classList.add('activetwo');
        });

        if(popup.classList.contains('activetwo')) {
            document.addEventListener('click', (e) => {
                if(e.target !== userLogin && e.target !== userPassword) {
                    popup.classList.remove('activetwo');
                }
            });
        }

        userBlock.addEventListener('mouseleave', (e) => {
            popup.classList.remove('active');
        });
    });
    }







//    userBlock.addEventListener('click', function (e) {
//    if (popup.classList.contains("active2")) {
//        popup.classList.remove('active2');
//        }
//    })


