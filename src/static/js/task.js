$(document).ready(function () {
    function updateTaskInfo() {
        const task_id = window.location.href.split('/').reverse()[0]

        $.ajax({
            type: "GET",
            url: "/api/task/" + task_id,
            encode: true,
        }).done(function (data) {

            // $("body").append("<p>" + JSON.stringify(data) + "</p>")
        });
    }

    updateTaskInfo()
    // setInterval(updateTaskInfo, 12000);
});