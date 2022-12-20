    let tooltipElem2;
    let tooltipElem3;


    document.onmouseover = function(event) {
      let target = event.target;

      // если у нас есть подсказка...

      let tooltipHtml2 = target.dataset.tooltip;
      let tooltipHtml3 = target.dataset.tooltip;

      if (!tooltipHtml2) return;
      if (!tooltipHtml3) return;

      // ...создадим элемент для подсказки


      tooltipElem2 = document.createElement('div');
      tooltipElem3 = document.createElement('div');

      tooltipElem2.className = 'tooltip-inner';
      tooltipElem3.className = 'tooltip-arrow';

      tooltipElem2.innerHTML = tooltipHtml2;

      document.body.append(tooltipElem2);
      document.body.append(tooltipElem3);

      // спозиционируем его сверху от аннотируемого элемента (top-center)
      let coords = target.getBoundingClientRect();

      let left = coords.left + (target.offsetWidth - tooltipElem2.offsetWidth) / 2;
      let left2 = coords.left + (target.offsetWidth) / 2

      let top = coords.top + 5 + target.offsetHeight;


      tooltipElem2.style.left = left + 'px';
      tooltipElem2.style.top = top + 2 + 'px';

      tooltipElem3.style.left = left2 + 'px';
      tooltipElem3.style.top = top + 'px';

    };

    document.onmouseout = function(e) {


      if (tooltipElem2) {
        tooltipElem2.remove();
        tooltipElem2 = null;
      }

      if (tooltipElem3) {
        tooltipElem3.remove();
        tooltipElem3 = null;
      }

    };