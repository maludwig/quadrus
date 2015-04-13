// Copyright Mitchell Ludwig, Apr 13, 2015.
// This code is used to make the index page all fancy, with the filter dropdown

(function($){
    //Allows for multiple different filters, I've only implemented one here
    function filterSelector() {
        var sel = "";
        var value;
        $(".filter").each(function(){
            value = $(this).val();
            if (value != "") {
                sel += "." + $(this).val();
            }
        });
        return sel;
    }
    $(function(){
        //When the user selects a new filter
        $(".filter").change(function(){
            var sel = filterSelector(),
                $toShow = $(".vehicle-tile" + sel),
                $toHide = $(".vehicle-tile:visible"),
                i = 0;
            $toHide.fadeOut(800, function() {
                //This event is triggered once for each element, so this code ensures it's only run once.
                i++;
                if(i == $toHide.length) {
                    $toShow.fadeIn(800);
                }
            });
        });
    });
}(jQuery));