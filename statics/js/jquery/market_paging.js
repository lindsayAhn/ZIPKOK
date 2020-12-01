
function setPage(listCount, currentPage, kwd) {
		var kwd = kwd;
		var listCount = listCount;
		var pageCount = (parseInt( listCount/ 10) + 1);
		var currentPage = currentPage;
		var endPage = (parseInt(pageCount/10 + 1) * 5)+1;
		var displayPage = parseInt((currentPage + 4 ) / 5 ) * 5;


		if(parseInt( listCount% 10)==0){
			pageCount -=1;
		};
		console.log("listCount", listCount);
		console.log("pageCount", pageCount);
		console.log("currentPage", currentPage);
		console.log("endPage", endPage);
		console.log("displayPage", displayPage);

        var pager = $('#pager');
        	if(currentPage <= 5){
			pager.prepend('<li><</li>');
		}else{
			pager.append('<li><a href=/market/list/'+(displayPage-5)+'?kwd='+kwd+'>'+'<'+'</li>');
		}

        for (var i = displayPage-4; i <= displayPage; i++) {
			if(i==currentPage){
				pager.append('<li class="selected">'+i+'</li>')
				continue;
			}else if(i>pageCount){
				pager.append('<li>'+i+'</li>')
				continue;
			}
			pager.append('<li><a href=/market/list/'+i+'?kwd='+kwd+'>'+i+'</li>');
		}

        var nextPage = displayPage+1

		if(currentPage < endPage && endPage < pageCount){
			pager.append('<li><a href=/market/list/'+nextPage+ '?kwd='+kwd+'>'+'>'+'</li>');
		}else{
			pager.append('<li>'+'>'+'</li>');
	}

}