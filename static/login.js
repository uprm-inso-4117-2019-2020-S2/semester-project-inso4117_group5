+-const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("btn");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.login.value;
    const password = loginForm.password.value;

    const reqObj = {
      "uusername": username,
      "upassword": password
    };

    $.ajax({
      url: '/HTH/login',
      type: 'POST',
      data: JSON.stringify(reqObj),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      success: function(data) {
        if(data.logged_in){
         window.location.assign("127.0.0.1:5000/HTH/helpsomehommies")
        }
        else{
          alert("Log in unsuccesful!")
        }
      }
    });
})
