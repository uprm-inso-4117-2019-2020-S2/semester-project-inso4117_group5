const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("btn");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.login.value;
    const password = loginForm.password.value;
    const email = loginForm.email.value;
    const phone = loginForm.phone.value;

    const reqObj = {
      "uusername": username,
      "upassword": password,
      "uemail": email,
      "uphone": phone
    };

    console.log(reqObj)

    $.ajax({
      url: '/register',
      type: 'POST',
      data: JSON.stringify(reqObj),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      success: function(data) {
        window.location.assign("/HTH/profile")
        alert("Form received");
        //TODO add error codes just in case on the return for this request
      }
    });
})
