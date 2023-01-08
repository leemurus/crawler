$(document).ready(function () {
    function setMainUrl(url) {
        $(".url_value a").attr("href", url).text(url)
    }

    function setUrls(urls) {
        urls.forEach(
            url => $(".links_list").append("<li><a href=" + url + ">" + url + "</a></li>")
        )
    }

    function updateTaskInfo() {
        const task_id = window.location.href.split('/').reverse()[0]

        $.ajax({
            type: "GET",
            url: "/api/task/" + task_id,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        }).done(function (data) {
            setMainUrl(data["url"])

            if (data["status"] === 'SUCCESS') {
                $("main").removeClass("loader-background")
                $(".links_list").empty()
                $(".loader").hide()
                setUrls(data["result"])
            } else {
                setTimeout(updateTaskInfo, 1000);
            }
        });
    }

    updateTaskInfo();
});