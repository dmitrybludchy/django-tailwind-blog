window.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('#burger');
    const menu = document.querySelector('#menu');
  
    const showHide = function(el, show) {
      el.addEventListener('click', () => {
        if (show.style.display === "none") {
          show.style.display = "";
        } else {
          show.style.display = "none";
        }
      })
    };
  
    showHide(burger, menu);
  

    const btnComponents = document.querySelector('#components');
    const btnComponentsOn = document.querySelector('#componentsOn');
  
    showHide(btnComponents, btnComponentsOn);
    
    const componentsMobile = document.querySelector('#componentsMobile');
    const componentsOnMobile = document.querySelector('#componentsOnMobile');

    showHide(componentsMobile, componentsOnMobile);
});