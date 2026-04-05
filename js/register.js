const API = "https://user-management-suuo.onrender.com/api";


$("#registerBtn").click(function () {
    const name = $("#name").val().trim();
    const email = $("#email").val().trim();
    const password = $("#password").val().trim();

    if (!name || !email || !password) {
        show("danger", "All fields required");
        return;
    }

    $.ajax({
        url: API + "/register",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ name, email, password }),

        success: function () {
            show("success", "Registered successfully");
            setTimeout(() => location.href = "login.html", 1000);
        },

        error: function (err) {
            show("danger", err.responseJSON?.message || "Error");
        }
    });
});

function show(type, msg) {
    $("#alertBox").removeClass().addClass(`alert alert-${type}`).text(msg);
}