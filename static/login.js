const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("btn");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.login.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "web_dev") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.visibility = "visible";
    }
})
