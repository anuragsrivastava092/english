$(document).ready(function(){
	temp =[];

	 $("#jsfiddel").append(article_content);

	$("#jsfiddel").on("click","p span",function(){
		
		current = this;
		question_id = $(current).attr("id");

		state=1;
		part_state=1;

		right=-1;
		response=-1;

		if (article_status==="attempted"){
				state=0;
		}
		
		
		for (i = 0; i< question_content.length; i++) {
		if (question_content[i].id1.toString() === question_id) { 
			if (state===0) {
			response= parseInt( question_content[i].response.toString() );
							}
			break; 
		}
		
	}
	for (j = 0; j < option_content.length; j++) {
		if (option_content[j].sample_question_id.toString() === question_id) { 
			if (state===0) {
			right= parseInt( option_content[j].right_choice.toString() );
							}

			break; }
		
	}
	for (l = 0; l < temp.length; l++) {
		if (temp[l].id.toString() === question_id) { 
			part_state=0;
			response = parseInt(temp[l].response.toString());
			right = parseInt(temp[l].correct_ans.toString());
			break; 
		}
		
	}



	//finding object
		elem = $(current).parent();
		
		
																		//<input type="hidden" name="firstname" value="vhvh">
		var txt3 = document.createElement("p");
		$(txt3).addClass("Current_question");
		$(txt3).attr("id", question_id);
		
		
		var upper_end =document.createElement("div");
		var txt9 = document.createElement("div");                                  //
		$(txt9).addClass("glyphicon glyphicon-remove close_button");
		upper_end.appendChild(txt9);
		txt3.appendChild(upper_end);
		
		var main_question = document.createElement("p");//question ?
		var question_text = document.createTextNode(question_content[i].question_text);
		main_question.appendChild(question_text);
		txt3.appendChild(main_question);
		
		var form = document.createElement("form"); //form
		//$(form).attr("action", "");
		//$(form).attr("method", "post"); //method
		
		//var node = document.createTextNode("{% csrf_token %}");
		//form.appendChild(node);
		
		
		var label0 = document.createElement("label");
		var option0 = document.createElement("input");
		$(option0).attr("type","hidden");
		$(option0).attr("name","question_id");
		$(option0).attr("value",question_id);
		$(option0).attr("class","question_id");
		label0.appendChild(option0)
		form.appendChild(label0);
				
		
		
		
		
		
		
		var label1 = document.createElement("label");
		$(label1).attr("class","choice_class_1");
		var option1 = document.createElement("input");
		$(option1).attr("type","radio");
		$(option1).attr("name","selected_choice");
		$(option1).attr("id","choice1");
		$(option1).attr("value","1");

		if(state===0 | part_state===0)  {  $(option1).attr("disabled","disabled");                  
		

		if (response===1) { 
			$(option1).prop("checked",true); 
			$(label1).css("background-color","red");
		}

		if (right===1) { 
			$(option1).prop("checked",true); 
			$(label1).css("background-color","green");
		}

	}
		var option_text1_node = document.createTextNode(option_content[j].choice1);
		label1.appendChild(option1)
		label1.appendChild(option_text1_node);
		form.appendChild(label1);
		var space1 = document.createElement("br");
		form.appendChild(space1);		
		
		var label2 = document.createElement("label");
		$(label2).attr("class","choice_class_2");
		var option2 = document.createElement("input");
		$(option2).attr("type","radio");
		$(option2).attr("name","selected_choice");
		$(option2).attr("id","choice2");
		$(option2).attr("value","2");
		if(state===0 | part_state===0)  {  $(option2).attr("disabled","disabled");                  
		
		if (response===2) { 
			$(option2).prop("checked",true); 
			$(label2).css("background-color","red");
		}

		if (right===2) { 
			$(option2).prop("checked",true); 
			$(label2).css("background-color","green");
		}
	}	

		var option_text2_node = document.createTextNode(option_content[j].choice2);
		label2.appendChild(option2)
		label2.appendChild(option_text2_node);
		form.appendChild(label2);
		var space2 = document.createElement("br");
		form.appendChild(space2);
		
		var label3 = document.createElement("label");
		$(label3).attr("class","choice_class_3");
		var option3 = document.createElement("input");
		$(option3).attr("type","radio");
		$(option3).attr("name","selected_choice");
		$(option3).attr("id","choice3");
		$(option3).attr("value","3");

		if(state===0 | part_state===0)  {  $(option3).attr("disabled","disabled");                  
		
		if (response===3) { 
			$(option3).prop("checked",true); 
			$(label3).css("background-color","red");
		}

		if (right===3) { 
			$(option3).prop("checked",true); 
			$(label3).css("background-color","green");
		}
	}
		var option_text3_node = document.createTextNode(option_content[j].choice3);
		label3.appendChild(option3)
		label3.appendChild(option_text3_node);
		form.appendChild(label3);
		var space3 = document.createElement("br");
		form.appendChild(space3);
		
		var label4 = document.createElement("label");
		$(label4).attr("class","choice_class_4");
		var option4 = document.createElement("input");
		$(option4).attr("type","radio");
		$(option4).attr("name","selected_choice");
		$(option1).attr("id","choice4");
		$(option4).attr("value","4");
		if(state===0  | part_state===0)  {  $(option4).attr("disabled","disabled");                  
		


		if (response===4) { 
			$(option4).prop("checked",true); 
			$(label4).css("background-color","red");
		}

		if (right===4) { 
			$(option4).prop("checked",true); 
			$(label4).css("background-color","green");
		}
	}
		var option_text4_node = document.createTextNode(option_content[j].choice4);
		label4.appendChild(option4)
		label4.appendChild(option_text4_node);
		form.appendChild(label4);
		var space4 = document.createElement("br");
		form.appendChild(space4);
		
		var submiss = document.createElement("button");
		$(submiss).addClass("btn btn-primary btn-lg");
		$(submiss).attr("id","submiss_type");
		$(submiss).attr("type", "submit");

		if(state===0 | part_state===0)  {  $(submiss).attr("disabled","disabled");                  
		}

		var submit = document.createTextNode("submit");
		submiss.appendChild(submit);
		form.appendChild(submiss);
		txt3.appendChild(form);

		var feedback = document.createElement("p");//question ?
		var feedback_text = document.createTextNode("");
		feedback.appendChild(feedback_text);
		txt3.appendChild(feedback);


		if ($( ".Current_question" ).length === 1) {
			
			if ($(".Current_question").attr("id")===question_id) {
				$(".Current_question").remove();
			}
			else {
				$(".Current_question").remove();
				$(elem).after(txt3);
				
			}
			}
		else{
			
			$(elem).after(txt3);
		}
	});
	$(document).on('click', ".close_button", function() {
		
		$(".Current_question").remove();
		  
	});
		
	 


 		$("#jsfiddel").on("click","#submiss_type",function(e){
 	
 		e.preventDefault();
 		
        var id = $(".question_id").val();
        
        var response = $('input:radio[name=selected_choice]:checked').val();
     	alert(response	);
        var account = { "question_id":id,
            "selected_choice":response
            };
     
        var xhr = new XMLHttpRequest();
        var url = "http://localhost:8000/responseapi/"; 
        xhr.open("POST", url);
        xhr.setRequestHeader('Content-Type', "application/x-www-form-urlencoded",true);
        
        xhr.send(JSON.stringify(account));
    
      xhr.onreadystatechange = function() {
            
             if (xhr.readyState == 4 && xhr.status == 200) {
             
             		var responseText = xhr.responseText;
             		$("#submiss_type").attr("disabled","disabled"); 
             		len_temp = temp.length;
             		temp[len_temp] ={};
             		temp[len_temp].id=id;
             		temp[len_temp].response=response;
             		temp[len_temp].correct_ans=responseText;

			    	if (String(responseText)===String(response)){ 
			    		
						var inpt_id = "."+"choice_class_" + String(responseText);
					$(inpt_id).css("background-color", "green");

					
					}
					else {
						
				var input_id_1 = "."+"choice_class_" + String(responseText);
					$(input_id_1).css("background-color", "green");
					var input_id_2 = "."+"choice_class_" + String(response);
					$(input_id_2).css("background-color", "red");
					
				}
             
        
             }
        }
        
   /*     	responseText =3;
        if (String(3)===String(response)){ 
			    		alert(222);
						 inpt_id = "."+"choice_class_" + String(responseText);
					
						 	alert(inpt_id);
					$(inpt_id).css("background-color", "green");
					alert(234);
					}
					else {
						alert(2);
					var input_id_1 = "."+"choice_class_" + String(responseText);
					$(input_id_1).css("background-color", "green");
					var input_id_2 = "."+"choice_class_" + String(response);
					$(input_id_2).css("background-color", "red");
					
				}
             
        */
             

 });
});


	



