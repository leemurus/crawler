$(document).ready(function () {
    function updateTaskInfo() {
        const task_id = window.location.href.split('/').reverse()[0]

        $.ajax({
            type: "GET",
            url: "/api/task/" + task_id,
            headers: {
               'X-CSRFToken': getCookie('csrftoken'),
            }
        }).done(function (data) {
            $("header").append("<p>" + JSON.stringify(data) + "</p>")
        });
    }

    updateTaskInfo()
    // setInterval(updateTaskInfo, 12000);
});