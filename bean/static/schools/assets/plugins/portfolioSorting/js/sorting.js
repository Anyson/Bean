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
      Dajaxice.schools.get_articles(Dajax.process, {'sid': $('#school').val(),'mid':-1});
    } else {
      Dajaxice.schools.get_articles(Dajax.process, {'sid': $('#school').val(), 'mid':$(this).attr("value")});
    }
  }); // end click event listener
  
});

function paginationOnClick(p) {
	var page = p;
  	var current_page = $("#current_page").val();
  	if (page == "pre") {
  		page = new Number(current_page);
  		page = page - 1;
  	} else if (page == "next") {
  		page = new Number(current_page);
  		page = page + 1;
  	}
  	page = page - 1;
  	Dajaxice.schools.get_articles(Dajax.process, {'sid': $('#school').val(), 'mid':$('#q_major').val(), 'page' : page});
  	
	return false;
}

function searchPaginationOnClick(p) {
	var page = p;
  	var current_page = $("#current_page").val();
  	if (page == "pre") {
  		page = new Number(current_page);
  		page = page - 1;
  	} else if (page == "next") {
  		page = new Number(current_page);
  		page = page + 1;
  	}
  	page = page - 1;
  	Dajaxice.schools.get_search_articles(Dajax.process, {'q_search':$('#q_search').val(), 'page' : page});
  	
	return false;
}

function my_callback(data){
	Dajax.process(data);
}