$(document).ready(function(){
  var pclone = $(".portfolio").clone();
  $("#sort a").on("click", function(e){
    e.preventDefault();
    var sorttype = $(this).attr("class");
    
    // determine if another link is selected
    if(!$(this).hasClass("selected")) {
      $("#sort a").removeClass("selected");
      $(this).addClass("selected");
    }
    // check filter sort type
    if(sorttype == "all") {
      var filterselect = pclone.find("li");
      Dajaxice.schools.get_articles(Dajax.process, {'sid': $('#school').val(),'mid':-1})
    } else {
      var filterselect = pclone.find("li[class="+sorttype+"]");
      Dajaxice.schools.get_articles(Dajax.process, {'sid': $('#school').val(), 'mid':$(this).attr("value"), 'page':1})
    }
     
    /*
    $(".portfolio").quicksand(filterselect, 
    {
      adjustHeight: 'auto',
      duration: 550
    }, function() { 
      // callback function
    });
    */
  }); // end click event listener
});

function my_callback(data){
	Dajax.process(data);
}