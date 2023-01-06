$(document).ready(function () {
    $("form").submit(function (event) {
        $.ajax({
            type: "POST",
            url: "api/task",
            headers: {
               'X-CSRFToken': getCookie('csrftoken'),
            },
            data: {
                url: $("#search-bar").val(),
            },
        }).done(function (data) {
            window.location.assign("task/" + data["task_id"]);
            console.log(data);
        });

        event.preventDefault();
    });
});