const password=document.getElementById("password"),
        icon=document.querySelector(".pass-icon");

icon.addEventListener("click", e =>{
    if(password.type=== "password"){
        password.type="text";
        icon.src="image/icons/openeye2.png";
    }
    else{
        password.type="password"
        icon.src="image/icons/closeeye2.png";
    }
})