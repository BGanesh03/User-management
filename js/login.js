const API = "https://user-management-suuo.onrender.com/api";

$("#loginBtn").click(function () {
    const email = $("#email").val().trim();
    const password = $("#password").val().trim();

    if (!email || !password) {
        show("danger", "Enter email & password");
        return;
    }

    $.ajax({
        url: API + "/login",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ email, password }),

        success: function (res) {
            localStorage.setItem("token", res.token);
            show("success", "Login success");
            setTimeout(() => location.href = "profile.html", 800);
        },

        error: function () {
            show("danger", "Invalid credentials");
        }
    });
});

function show(type, msg) {
    $("#alertBox").removeClass().addClass(`alert alert-${type}`).text(msg);
}