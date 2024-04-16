
/* Contact Form */


document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("contactForm").addEventListener("submit", function(event) {
        event.preventDefault(); // 
    
        var nameInput = document.getElementById("nameInput");
        var emailInput = document.getElementById("emailInput");
        var subjectInput = document.getElementById("subjectInput");
        var messageInput = document.getElementById("messageInput");
    
        var name = nameInput.value;
        var email = emailInput.value;
        var subject = subjectInput.value;
        var message = messageInput.value;
        var smiley = ("&#128512;");
    
    
        var popup = document.createElement("div");
        popup.innerHTML = "Thank you, " + name + "! Your message has been submitted! " + smiley;
        popup.classList.add("popup");
    
        var popupContainer = document.getElementById("popupContainer");
        popupContainer.appendChild(popup);
    
        popup.style.display = "block";
    
        setTimeout(function() {
            popup.style.display = "none";
        }, 3000);
    });
    });



/**FAQ Hidden Scroll **/

    document.addEventListener('DOMContentLoaded', function () {
    const faqItems = document.querySelectorAll('.faq-container dd');

    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function toggleVisible() {
        faqItems.forEach((item) => {
            if (isInViewport(item)) {
                item.classList.add('visible');
            } else {
                item.classList.remove('visible');
            }
        });
    }

    toggleVisible();

    window.addEventListener('scroll', toggleVisible);
});

console.log("Script loaded");


/*About */



const paragraphs = document.querySelectorAll('.story-paragraph');


const options = {
  threshold: 0.2 
};

const callback = (entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target); 
    }
  });
};

const observer = new IntersectionObserver(callback, options);

paragraphs.forEach(paragraph => {
  observer.observe(paragraph);
});

/* Pop up */

function showThankYouMessage() {
  alert("Thank you for booking!");
  return true;
}