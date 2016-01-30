$(document).ready(function(){
    $("#submit").removeAttr("form");
    $("#submit").removeAttr("type");
    $("#submit").attr("onclick", "submit_form()");
});

function submit_form() {
    if ($("#url").val() != "") {
        $("#submit").hide();
        $("#info").show();
        $("#dlform").submit();
    }
}
