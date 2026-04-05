const API = "https://user-management-suuo.onrender.com/api";

const token = localStorage.getItem("token");

if (!token) location.href = "login.html";

// LOAD PROFILE
$.ajax({
    url: API + "/profile",
    type: "GET",
    headers: { Authorization: "Bearer " + token },

    success: function (res) {
        $("#email").val(res.email);
        $("#name").val(res.name);
    },

    error: function () {
        logout();
    }
});

// UPDATE
$("#updateProfileBtn").click(function () {
    const name = $("#name").val();

    $.ajax({
        url: API + "/profile",
        type: "PUT",
        headers: { Authorization: "Bearer " + token },
        contentType: "application/json",
        data: JSON.stringify({ name }),

        success: function () {
            show("success", "Updated");
        },

        error: function () {
            show("danger", "Error");
        }
    });
});

// LOGOUT
$("#logoutBtn").click(function () {
    logout();
});

function logout() {
    localStorage.removeItem("token");
    location.href = "login.html";
}

function show(type, msg) {
    $("#alertBox").removeClass().addClass(`alert alert-${type}`).text(msg);
}