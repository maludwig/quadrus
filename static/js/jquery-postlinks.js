// Copyright Mitchell Ludwig, Apr 13, 2015.
// This code is used to make links with the class ".post-request" emit HTTP POST requests.

(function($){
    /* Django project code BEGIN */
    var csrftoken = $.cookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    /* Django project code END */
    $(function(){
        $("a.post-request").click(function(e){
            var $this = $(this),
                href = $this.prop("href"),
                reload = $this.data("reload");

            e.preventDefault();
            alert("posting to: " + href + "\nreload: " + reload);
            $.post(href,function(){
                if(reload) {
                    location.reload(true);
                }
            });
        });
    });
}(jQuery));