$(document).ready(function () {
    $("form").submit(function (event) {
        var formData = {
            url: $("#search-bar").val(),
        };

        $.ajax({
            type: "POST",
            url: "api/task",
            data: formData,
            dataType: "json",
            encode: true,
        }).done(function (data) {
            window.location.assign("task/" + data["task_id"]);
            console.log(data);
        });

        event.preventDefault();
    });
});