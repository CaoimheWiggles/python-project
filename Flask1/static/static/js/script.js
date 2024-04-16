/* pop up */

document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById("myModal");

   
    var modalShown = localStorage.getItem("modalShown");

    if (!modalShown) {
        showModal();
        localStorage.setItem("modalShown", true);
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    function showModal() {
        modal.style.display = "block";
    }

    document.querySelector('.close-button').addEventListener('click', function() {
        modal.style.display = 'none';
    });
});


/*List Items */


const items = document.querySelectorAll('.fade-in');

const options = {
  threshold: 0.2 
};

const callback = (entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      observer.unobserve(entry.target); 
    }
  });
};

const observer = new IntersectionObserver(callback, options);

items.forEach(item => {
  observer.observe(item);
});

/* Testimonials */


const swiper = new Swiper('.js-testimonials-slider', {
    grabCursor: true,
    spaceBetween:30,
    pagination:{
        el: '.js-testimonials-pagination',
        clickable:true
    },
    mousewheel:true,
    breakpoints:{
        767:{
            slidesPerView: 1
        }
    }
});

