//Add a <li> element to a list
$("DIV#add_item").click(function () {
    var ul = $("UL.my_list").html();
    ul += "<li>Item</li>";
    $("UL.my_list").html(ul);
});
