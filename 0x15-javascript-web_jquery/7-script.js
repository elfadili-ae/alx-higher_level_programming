//Fetch the name of the character from API
$.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    method: "GET",
    dataType: "json",
    success: function (data) {
        $("DIV#character").text(data.name);
    }
});