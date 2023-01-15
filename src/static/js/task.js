const TaskStatus = {
  STARTED: "STARTED",
  FAILURE: "FAILURE",
  SUCCESS: "SUCCESS",
};


$(document).ready(function () {
    function removeLoader() {
        $("main").removeClass("loader-background")
        $(".loader").hide()
    }

    function setMainUrl(url) {
        $(".url_value a").attr("href", url).text(url)
    }

    function setUrls(urls) {
        if (urls.length === 0) {
            $(".links_list").hide()
            $("main").append("<h1>No urls</h1>")
            return
        }

        urls.sort()
        urls.forEach(
            url => $(".links_list").append("<li><a href=" + url + ">" + url + "</a></li>")
        )
    }

    function updateTaskInfo() {
        const task_id = window.location.href.split("/").reverse()[0]

        $.ajax({
            type: "GET",
            url: "/api/task/" + task_id,
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            }
        }).done(function (data) {
            setMainUrl(data["url"])

            if (data["status"] === TaskStatus.SUCCESS) {
                $(".links_list").empty()
                setUrls(data["result"])
                removeLoader()
            } else if (data["status"] === TaskStatus.FAILURE) {
                $(".links_list").hide()
                removeLoader()
                $("main .error").show()
            } else {
                setTimeout(updateTaskInfo, 1000);
            }
        });
    }

    updateTaskInfo();
});