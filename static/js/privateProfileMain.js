    let profileBox = document.querySelector('.profile-box');
    let mainHeader = document.querySelector('.main-header');
    let profileInfoBox = document.querySelector('.profile-info-box');
    let shopFooter = document.querySelector('.shop-footer');

    let coordsShopFooter = shopFooter.getBoundingClientRect();

    let heightHeader = mainHeader.offsetHeight;

    let heightProfileBox = window.innerHeight - heightHeader;

    profileBox.style.height = heightProfileBox + 'px'; // Применение позиционирования слайдера по вертикал

    let coordsProfileInfoBox = mainForm.getBoundingClientRect();
    let coordsProfileBox = registerForm.getBoundingClientRect();

        if(coordsMainForm.bottom > coordsRegisterForm.bottom || coordsMainForm.top < coordsRegisterForm.top){

    let coordsRegisterForm = profileBox.getBoundingClientRect();
