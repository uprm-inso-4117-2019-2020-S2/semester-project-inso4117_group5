const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("btn");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.login.value;
    const password = loginForm.password.value;

    const reqObj = {
      "username": username,
      "password": password
    };

    $.ajax({
      url: '/HTH/login',
      type: 'POST',
      data: JSON.stringify(reqObj),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      success: function(data) {
        if(data.logged_in){
          alert("Succesful log in!")
        }
        else{
          alert("Log in unsuccesful!")
        }
      }
    });
})
