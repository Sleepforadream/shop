window.onload = function () {

//начало tooltipSocial

let tooltipInner;
let arrow;

document.onmouseover = function (event) {
    let target = event.target;

    // если у нас есть подсказка...

    let tooltipInnerHtml = target.dataset.tooltip;
    let arrowHtml = target.dataset.tooltip;

    if (!tooltipInnerHtml) return;
    if (!arrowHtml) return;

    // ...создадим элемент для подсказки


    tooltipInner = document.createElement('div');
    arrow = document.createElement('div');

    tooltipInner.classList.add('tooltip-inner');

    arrow.className = 'tooltip-arrow';

    tooltipInner.innerHTML = tooltipInnerHtml;

    document.body.append(tooltipInner);
    document.body.append(arrow);

    // спозиционируем его сверху от аннотируемого элемента (top-center)
    let coords = target.getBoundingClientRect();

    let leftTooltip = coords.left + (target.offsetWidth - tooltipInner.offsetWidth) / 2;
    let leftTooltip2 = coords.left + (target.offsetWidth) / 2

    let topTooltip = coords.top + 2 + target.offsetHeight;


    tooltipInner.style.left = leftTooltip + 'px';
    tooltipInner.style.top = topTooltip + 2 + 'px';

    arrow.style.left = leftTooltip2 + 'px';
    arrow.style.top = topTooltip + 'px';

    tooltipInner.style.transition = "0.5s";
    tooltipInner.style.opacity = 0.9;

    arrow.style.transition = "0.5s";
    arrow.style.opacity = 0.9;

};

document.onmouseout = function () {


    if (tooltipInner) {
        tooltipInner.remove();
        tooltipInner = null;
    }

    if (arrow) {
        arrow.remove();
        arrow = null;
    }

};

//конец tooltipSocial

//начало userBlock

let popup = document.querySelector('.user-popup'); // Само окно
let openPopupButton = document.querySelector('.menu-user-panel'); // Кнопка для показа окна
let userBlock = document.querySelector('.user-box'); // Весь юзерблок (само окно + кнопка для показа)
let userCheckbox = document.querySelector('.remember-checkbox'); // Чекбокс
let userLogin = document.querySelector('.input-login-user-popup'); // Поле ввода логина
let userPassword = document.querySelector('.input-password-user-popup'); // Поле ввода пароля

let coordsPopupButton = openPopupButton.getBoundingClientRect(); //Координаты кнопки показа окна
let leftUserBlock = coordsPopupButton.left + (openPopupButton.offsetWidth - popup.offsetWidth) / 2; // Координаты позиционирования окна по горизонтали
let topUserBlock = coordsPopupButton.top + openPopupButton.offsetHeight; // Координаты позиционирования окна по вертикали
popup.style.left = leftUserBlock + 'px'; // Применение позиционирования окна по горизонтали
popup.style.top = topUserBlock + 'px'; // Применение позиционирования окна по вертикали

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

    if (popup.classList.contains('activetwo')) {
        document.addEventListener('click', (e) => {
            if (e.target !== userLogin && e.target !== userPassword) {
                popup.classList.remove('activetwo');
            }
        });
    }

    userBlock.addEventListener('mouseleave', (e) => {
        popup.classList.remove('active');
    });
});

//конец userBlock

//начало searchBlock

    let popupSearch = document.querySelector('.menu-search'); // Само окно
    let openSearchPopupButton = document.querySelector('.search-icon-box'); // Кнопка для показа окна
    let headerMenu = document.querySelector('.header-menu'); //Хэдер
    let InputSearch = document.querySelector('.input-search'); //Поле ввода для поиска

    let coordsSearchPopupButton = openSearchPopupButton.getBoundingClientRect(); //Координаты кнопки показа окна
    let leftSearchPopup = coordsSearchPopupButton.left + (openSearchPopupButton.offsetWidth - popupSearch.offsetWidth); // Координаты позиционирования окна по горизонтали
    let topSearchPopup = coordsSearchPopupButton.top + openSearchPopupButton.offsetHeight + (headerMenu.offsetHeight / 2) - 1; // Координаты позиционирования окна по вертикали
    popupSearch.style.left = leftSearchPopup + 'px'; // Применение позиционирования окна по горизонтали
    popupSearch.style.top = topSearchPopup + 'px'; // Применение позиционирования окна по вертикали

    const toggleMenu = () => {
        popupSearch.classList.toggle('active');
        InputSearch.focus();
    }

    openSearchPopupButton.addEventListener('click', e => {
        e.stopPropagation();
        toggleMenu();
    });



    document.addEventListener('click', e => {
        let target = e.target;
        let its_SearchMenu = target === popupSearch || popupSearch.contains(target);
        let its_button = target === openSearchPopupButton;
        let menu_is_active = popupSearch.classList.contains('active');

        if (!its_SearchMenu && !its_button && menu_is_active) {
            toggleMenu();
        }
    })
//конец searchBlock

//начало hamburgerBlock

    let popupMobileMenu = document.querySelector('.mobile-menu-box'); // Само окно
    let openMobileMenuButton = document.querySelector('.hamburger-menu'); // Кнопка для показа окна

    let mobileMenuCategories = document.querySelector('.mobile-sub-menu'); // Расширенное меню категорий
    let openMobileSubMenuButton = document.querySelector('.indicator-dropdown-medium'); // Кнопка для показа категорий

    const toggleMobileMenu = () => {
        popupMobileMenu.classList.toggle('active');
    }

    openMobileMenuButton.addEventListener('click', e => {
        e.stopPropagation();
        toggleMobileMenu();
    });

    const toggleMobileSubMenu = () => {
        mobileMenuCategories.classList.toggle('active');
    }

    openMobileSubMenuButton.addEventListener('click', e => {
        e.stopPropagation();
        toggleMobileSubMenu();
    });
//конец hamburgerBlock

// начало resizeBloks

    window.addEventListener('resize', function(event) {
        let coordsSearchPopupButton = openSearchPopupButton.getBoundingClientRect(); //Координаты кнопки показа окна
        let leftSearchPopup = coordsSearchPopupButton.left + (openSearchPopupButton.offsetWidth - popupSearch.offsetWidth); // Координаты позиционирования окна по горизонтали
        let topSearchPopup = coordsSearchPopupButton.top + openSearchPopupButton.offsetHeight + (headerMenu.offsetHeight / 2) - 1; // Координаты позиционирования окна по вертикали
        popupSearch.style.left = leftSearchPopup + 'px'; // Применение позиционирования окна по горизонтали
        popupSearch.style.top = topSearchPopup + 'px'; // Применение позиционирования окна по вертикали
        popupSearch.style.transition = "none"; // Удаление анимации окна при изменении окна

        let coordsPopupButton = openPopupButton.getBoundingClientRect(); //Координаты кнопки показа окна
        let leftUserBlock = coordsPopupButton.left + (openPopupButton.offsetWidth - popup.offsetWidth) / 2; // Координаты позиционирования окна по горизонтали
        let topUserBlock = coordsPopupButton.top + openPopupButton.offsetHeight; // Координаты позиционирования окна по вертикали
        popup.style.left = leftUserBlock + 'px'; // Применение позиционирования окна по горизонтали
        popup.style.top = topUserBlock + 'px'; // Применение позиционирования окна по вертикали
    }, false);
}

//конец resizeBlocks