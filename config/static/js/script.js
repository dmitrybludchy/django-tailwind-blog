window.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('#burger');
    const menu = document.querySelector('#menu');
  
    const showHide = function(el, sh) {
      el.addEventListener('click', () => {
        if (sh.style.display === "none") {
          sh.style.display = "";
        } else {
          sh.style.display = "none";
        }
      })
    };
  
    showHide(burger, menu);
  

    const btnComponents = document.querySelector('#components');
    const btnComponentsOn = document.querySelector('#componentsOn');
  
    showHide(btnComponents, btnComponentsOn);
  
});