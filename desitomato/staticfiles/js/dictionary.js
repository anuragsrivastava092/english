$(document).ready(function () {
	$("#tooltip").hide(); //popup1
	$("#tooltip_bookmark").hide();
	 $("#popup").hide();
	 $('#longtext').mouseup(function (e) {
	 
	 e.preventDefault();
	 $("#tooltip").hide();
	 $("#popup").hide();
	 $("#tooltip_bookmark").hide();
	 // x = e.clientX + + window.pageXOffset+ 'px';
    //  y = e.clientY + + window.pageYOffset+ 'px';
	// var tet = getSelectionText();
	 selected_area = window.getSelection();
	 selected_text = selected_area.toString();
	oRange = selected_area.getRangeAt(0); 
	oRect = oRange.getBoundingClientRect();
	if (selected_text.length>1 && oRect.height <25){ //bases on device
		x = oRect.right +  window.pageXOffset+ 'px';
	   y = oRect.top -10 + window.pageYOffset+ 'px';
	   lef = oRect.left -100  + window.pageXOffset+ 'px';
	   bottom = oRect.bottom + 10 + window.pageYOffset+ 'px';
	
		placeTooltip(x, y);
		placeTooltip_bookmark(lef, y);
		$("#tooltip").show();
		$("#tooltip_bookmark").show();
	}
	 
	 })
	 function placeTooltip(x_pos, y_pos) {
    var d = document.getElementById('tooltip');
    d.style.position = "absolute";
    d.style.left = x_pos;
    d.style.top = y_pos;
}
	function placeTooltip_bookmark(x_posi, y_posi) {
    var dd = document.getElementById('tooltip_bookmark');
    dd.style.position = "absolute";
    dd.style.left = x_posi;
    dd.style.top = y_posi;
}
	

  function placePopup(x_pos, y_pos) {
    var d = document.getElementById('popup');
    d.style.position = "absolute";
    d.style.left = x_pos;
    d.style.top = y_pos;
}
  document.getElementById("tooltip").addEventListener('click', function() {
  

  var xhr = new XMLHttpRequest();
        //var url = "/bookmark/"; //path de api ka 
        var url = "/lookup/";
        xhr.open("POST", url);
        //xhr.setRequestHeader('Content-Type', "application/x-www-form-urlencoded",true);
        var word = { "word":selected_text };
        
        xhr.send(JSON.stringify(word));
      alert(JSON.stringify(word));
       //alert(JSON.stringify(word));
        xhr.onreadystatechange = function() {
          //alert(2);
            
             if (xhr.readyState == 4 && xhr.status == 200) {
             	responsereply = xhr.responseText;
              alert(responsereply);
             	
             	//	$("#word_meaning_ans").text(responsereply);
              //  alert(responsereply);
              //responsereply =1122;
              placePopup(lef, bottom);
              $("#word_meaning").text(selected_text);
              $("#word_meaning_ans").text(responsereply);
              $("#popup").show();
              $("#tooltip").hide();
              $("#tooltip_bookmark").hide();
            }

             
    }


  //placePopup(lef, bottom);
  //responsereply ="i am hhh czczxxchxzchxzc xziuqphqw qwertyuipasd fghjklzxcvbnm asd ff xdi  ihuukkhd dshddugddsd uuhidsidyds sdsidussuudsu i am hhh czczxxchxzchxzc xziuqphqw qwertyuipasd fghjklzxcvbnm asd ff xdi  ihuukkhd dshddugddsd uuhidsidyds sdsidussuudsu i am hhh czczxxchxzchxzc xziuqphqw qwertyuipasd fghjklzxcvbnm asd ff xdi  ihuukkhd dshddugddsd uuhidsidyds sdsidussuudsu";
  //$("#word_meaning").text(selected_text);
  //$("#word_meaning_ans").text(responsereply);
  ///$("#popup").show();
  //$("#tooltip").hide();
  //$("#tooltip_bookmark").hide();
// //alert(selected_text);
 });

 document.getElementById("tooltip_bookmark").addEventListener('click', function() {

	// sent selected text to user
  //var url = "/lookup/"; //path de api ka 
  var xhr = new XMLHttpRequest();
  var url = "/bookmark/"; 
        xhr.open("POST", url);
        //xhr.setRequestHeader('Content-Type', "application/x-www-form-urlencoded",true);
        var word = { "word":selected_text };
        
        xhr.send(JSON.stringify(word));
        //alert(JSON.stringify(word));
       ////alert(JSON.stringify(account));
        xhr.onreadystatechange = function() {
            
             if (xhr.readyState == 4 && xhr.status == 200) {
             	responsereply = xhr.responseText;
             	if (responsereply!="Bookmarked") {
             		//saved
					alert("word bookmarked");

                                  	}
             	else  {
             		//not saved
					alert("Already bookmarked");
                	}


              }

              else {
             	//word_meaning_ans
             	//not saved
             	
                }
              }
  
  $("#tooltip").hide();
  $("#tooltip_bookmark").hide();

  });
 
	
});