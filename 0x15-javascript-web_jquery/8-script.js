//Fetch and list the title of all movies
$.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    dataType: "json",
    success: function (data) {
        var list = "";
        data.results.forEach(function (element) {
            list += "<li>" + element.title + "</li>";
        });
        $("UL#list_movies").html(list);
    }
});