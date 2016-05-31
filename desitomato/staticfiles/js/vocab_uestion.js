$(document).ready(function(){
	$(".front_question_button").css("display","none"); 
	lis1t = [{ id:1,question_text:"ddsdsdds",choice1:"11",choice2:"21",choice3:"31",choice4:"41"},
		{id:2,question_text:"1",choice1:"1",choice2:"2",choice3:"3",choice4:"4"},
		{id:3,question_text:"2",choice1:"1",choice2:"2",choice3:"3",choice4:"4"},
		{id:4,question_text:"3",choice1:"1",choice2:"2",choice3:"3",choice4:"4"}
	 ];
	 current=1;
	 var question_text_node = document.createTextNode(lit.question_text);
	 var option_text1_node = document.createTextNode(lit.choice1);
	 var option_text2_node = document.createTextNode(lit.choice2);
	 var option_text3_node = document.createTextNode(lit.choice3);
	 var option_text4_node = document.createTextNode(lit.choice4);
	 
	 $(".question_id").attr("id",lit.id);
	 $(".current_question_text").append(question_text_node);
	 $(".label_1").append(option_text1_node);
	 $(".label_2").append(option_text2_node);
	 $(".label_3").append(option_text3_node);
	 $(".label_4").append(option_text4_node);
	 
	 //
	 
	 $(document).on('click', ".submit_question_button", function() {
		$(".front_question_button").css("display","block"); 
		$(".submit_question_button").css("display","none"); 
		
	 var response = $('input:radio[name=selected_choice]:checked').val();
	var id = $(".question_id").attr("id");
	var question_type=1;
	alert(response);
	var account = { "question_id":id,
            "selected_choice":response,
            "question_type":question_type
            };
	alert(JSON.stringify(account));
	if(response===String(lit.right_choice+1)){
					alert(122);
					var inpt_id = "."+"label_" + String(response);
					$(inpt_id).css("background-color", "green");
	}
	else {
						alert(4343);
				var input_id_1 = "."+"label_" + String(lit.right_choice + 1);
					$(input_id_1).css("background-color", "green");
					var input_id_2 = "."+"label_" + String(response);
					$(input_id_2).css("background-color", "red");
					
	}
	alert(JSON.stringify(account));
		var xhr = new XMLHttpRequest();
        var url = "/responseapi/"; 
        xhr.open("POST", url);
        xhr.setRequestHeader('Content-Type', "application/x-www-form-urlencoded",true);
        xhr.send(JSON.stringify(account));
		xhr.onreadystatechange = function() {
            
             if (xhr.readyState == 4 && xhr.status == 200) {
				 
				 var responseText = xhr.responseText;
				 
				 alert(responseText);
				 	lit="";
					lit = JSON.parse(responseText);
			 }
			 
		}
			
	});
	
	 $(document).on('click', "#next_question", function() {
		 $(".front_question_button").css("display","none"); 
		$(".submit_question_button").css("display","inline");
		
		 
		 $(".question_id").attr("id",lit.id);
		form = $("form");
		$(form).empty();
		
		quest_tet = $(".current_question_text");
		$(quest_tet).empty();
		var question_tex_node = document.createTextNode(lit.question_text);
		quest_tet.append(question_tex_node);
		
		var label1 = document.createElement("label");
		$(label1).attr("class","label_1");
		var option1 = document.createElement("input");
		$(option1).attr("type","radio");
		$(option1).attr("name","selected_choice");
		$(option1).attr("id","choice1");
		$(option1).attr("value","1");
		var option_text1_node = document.createTextNode(lit.choice1);
		label1.appendChild(option1)
		label1.appendChild(option_text1_node);
		form.append(label1);
		var space1 = document.createElement("br");
		form.append(space1);
		
		var label2 = document.createElement("labe2");
		$(label2).attr("class","label_2");
		var option2 = document.createElement("input");
		$(option2).attr("type","radio");
		$(option2).attr("name","selected_choice");
		$(option2).attr("id","choice2");
		$(option2).attr("value","2");
		var option_text2_node = document.createTextNode(lit.choice2);
		label2.appendChild(option2)
		label2.appendChild(option_text2_node);
		form.append(label2);
		var space2 = document.createElement("br");
		form.append(space2);
		
		var label3 = document.createElement("label");
		$(label3).attr("class","label_3");
		var option3 = document.createElement("input");
		$(option3).attr("type","radio");
		$(option3).attr("name","selected_choice");
		$(option3).attr("id","choice3");
		$(option3).attr("value","3");
		var option_text1_node = document.createTextNode(lit.choice3);
		label3.appendChild(option3)
		label3.appendChild(option_text3_node);
		form.append(label3);
		var space3 = document.createElement("br");
		form.append(space3);
		
		var label4 = document.createElement("label");
		$(label4).attr("class","label_4");
		var option4 = document.createElement("input");
		$(option4).attr("type","radio");
		$(option4).attr("name","selected_choice");
		$(option4).attr("id","choice1");
		$(option4).attr("value","4");
		var option_text4_node = document.createTextNode(lit.choice4);
		label4.appendChild(option4)
		label4.appendChild(option_text4_node);
		form.append(label4);
		var space4 = document.createElement("br");
		form.append(space4);
		
		
		  
	});
	

});