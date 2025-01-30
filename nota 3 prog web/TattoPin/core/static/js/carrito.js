document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".add-to-cart").forEach(button => {
        button.addEventListener("click", function () {
            let tattooId = this.dataset.id;

            fetch("/agregar_al_carrito/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": getCSRFToken()
                },
                body: new URLSearchParams({
                    tattoo_id: tattooId
                })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
            })
            .catch(error => console.error("Error:", error));
        });
    });
});

// Función para obtener el token CSRF de la página
function getCSRFToken() {
    let cookieValue = null;
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.startsWith("csrftoken=")) {
            cookieValue = cookie.substring("csrftoken=".length, cookie.length);
            break;
        }
    }
    return cookieValue;
}