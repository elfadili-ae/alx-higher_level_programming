// list, add, remove a LI element
$("document").ready(() => {
    $("DIV#add_item").click(() => {
        $("UL.my_list").append("<li>not Item</li>");
    });

    $("DIV#remove_item").click(() => {
        $("UL.my_list li:last").remove();
    });

    $("DIV#clear_list").click(() => {
        $("UL.my_list").empty();
    });
});

