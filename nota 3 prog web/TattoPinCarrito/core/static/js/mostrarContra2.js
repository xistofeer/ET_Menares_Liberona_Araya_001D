const passwordFields = document.querySelectorAll("input[type='password']"),
      icon = document.querySelector(".pass-icon");

icon.addEventListener("click", e => {
    passwordFields.forEach(password => {
        if (password.type === "password") {
            password.type = "text";
        } else {
            password.type = "password";
        }
    });

    if (passwordFields[0].type === "password") {
        icon.src = "image/icons/closeeye2.png";
    } else {
        icon.src = "image/icons/openeye2.png";
    }
});
