$(document).ready(function(){
	var  score_ele = document.getElementsByClassName("score");
	var user_score = document.createTextNode(correct_question);
	score_ele[0].appendChild(user_score);
	
	function myFunction() {
		$("#instruction_question").css("height", "auto");
		$("#jsfiddel").css("height", "auto");
		var account={ "question_id":2};
		question_no=server_question.length;
		responseText ={q_type:"mcq",question_id:1,question_text:"what is your name",choice1:"kamal",choice2:"tarun",choice3:"kapil",choice4:"chirag"};
		 var q_type=responseText.q_type;
		 for (var i=0; i<question_no; i++) {
			 var j =0;
			 while (server_choices[j].sample_question_id !=  server_question[i].id ){  j+=1}
			
			if (q_type==="mcq") {
				
				var  question_add = document.getElementById("instruction_question");
			//	var elem = $(".instruction");
				
				var test_question_div = document.createElement("div");
				$(test_question_div).attr("id", server_question[i].id);
					
				var txt_question_p = document.createElement("p");
				$(txt_question_p).addClass("Current_question");
				var question_text = document.createTextNode(server_question[i].question_text);
				txt_question_p .appendChild(question_text);
				test_question_div.appendChild(txt_question_p);
				question_add.appendChild(test_question_div);
				
				
				var form = document.createElement("form"); //form
				$(form).attr("action", "localhost:8000/response"); //
				$(form).attr("id", "assessmen_test");
				$(form).attr("method", "POST"); //method
				$(form).attr("class", "mcq");
				var label1 = document.createElement("label");
	//			$(label1).attr("id","choice1");
				var option1 = document.createElement("input");
				$(option1).attr("id","choice2");
				$(option1).attr("type","radio");
				$(option1).attr("class","mcq");
				$(option1).attr("name","selected_choice");
				$(option1).attr("value",1); //onclick="document.getElementById('text').removeAttribute('disabled')
				$(option1).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')");
				var option_text1_node = document.createTextNode(server_choices[j].choice1);
				label1.appendChild(option1)
				label1.appendChild(option_text1_node);
				form.appendChild(label1);
				var space1 = document.createElement("br");
				form.appendChild(space1);
				
				$(option1).attr("disabled","disabled");
				if (server_response[i]==="1"){ $(option1).prop("checked", true); $(label1).css("background-color", "red");}
				if (server_choices[j].right_choice==="1"){ $(label1).css("background-color", "green");}

	//option2	
				var label2 = document.createElement("label");
	//			$(label2).attr("id","choice2");
				 option2 = document.createElement("input");
				$(option2).attr("type","radio");
				$(option2).attr("class","mcq");
				$(option2).attr("name","selected_choice");
				$(option2).attr("id","choice2");
				$(option2).attr("value",2);
				$(option2).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')"); //new to block submit button
				//$(option2).attr("id","choice2");
				var option_text2_node = document.createTextNode(server_choices[j].choice2);
				label2.appendChild(option2);
				label2.appendChild(option_text2_node);
				form.appendChild(label2);
				var space2 = document.createElement("br");
				form.appendChild(space2);
				
				$(option2).attr("disabled","disabled");
				if (server_response[i]==="2"){ $(option2).prop("checked", true); $(label2).css("background-color", "red");}
				if (server_choices[j].right_choice==="2"){ $(label2).css("background-color", "green");}
				
	//option3		
				var label3 = document.createElement("label");
	//			$(label3).attr("id","choice3");
				var option3 = document.createElement("input");
				$(option3).attr("type","radio");
				$(option3).attr("class","mcq");
				$(option3).attr("name","selected_choice");
				$(option3).attr("value",3);
				$(option3).attr("id","choice3");
				$(option3).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')");
				var option_text3_node = document.createTextNode(server_choices[j].choice3);
				label3.appendChild(option3);
				label3.appendChild(option_text3_node);
				form.appendChild(label3);
				var space3 = document.createElement("br");
				form.appendChild(space3);
				
				$(option3).attr("disabled","disabled");
				if (server_response[i]==="3"){ $(option3).prop("checked", true); $(label3).css("background-color", "red");}
				if (server_choices[j].right_choice==="3"){ $(label3).css("background-color", "green");}
				
	//option4	
				var label4 = document.createElement("label");
	//			$(label4).attr("id","choice4");
				var option4 = document.createElement("input");
				$(option4).attr("type","radio");
				$(option4).attr("name","selected_choice");
				$(option4).attr("class","mcq");
				$(option4).attr("value",4);
				$(option4).attr("id","choice4");
				$(option4).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')");
				var option_text4_node = document.createTextNode(server_choices[j].choice4);
				label4.appendChild(option4)
				label4.appendChild(option_text4_node);
				form.appendChild(label4);
				var space4 = document.createElement("br");
				form.appendChild(space4);
				
				$(option4).attr("disabled","disabled");
				
				if (server_response[i]==="4"){ $(option4).prop("checked", true); $(label4).css("background-color", "red");}
				if (server_choices[j].right_choice==="4"){ $(label4).css("background-color", "green");}
				
				question_add.appendChild(form); 
		/*		
				var submiss = document.createElement("button");
				$(submiss).addClass("btn btn-primary btn-lg button_check ");
				$(submiss).attr("id","submiss_type");
				$(submiss).attr(“disabled”, true);
				$( submiss  ).prop( "disabled", true );
				
				
				var submit = document.createTextNode("submit");
				submiss.appendChild(submit);
				$(submiss).attr("type", "submit");
				form.appendChild(submiss);
				question_add.appendChild(form);
				
		*/		var question_instruction_div = document.createElement("div");
				$(question_instruction_div).attr("id","q_id"+"inst");
				$(question_instruction_div).attr("class","ans_explanation");
				
				var question_instruction_p = document.createElement("p");
				$(question_instruction_p).addClass("q_instruction");
				var question_explanation = document.createTextNode("explantaion of question");
				question_instruction_p.appendChild(question_explanation);
				question_instruction_div.appendChild(question_instruction_p);
				question_add.appendChild(question_instruction_div);
			}
		 
		 
		else if(q_type==="multicq"){
			var  question_add = document.getElementById("instruction_question");
			var elem = $(".instruction");
			
			var test_question_div = document.createElement("div");
			$(test_question_div).attr("id", q_type=responseText.question_id);
				
			var txt_question_p = document.createElement("p");
			$(txt_question_p).addClass("Current_question");
			var question_text = document.createTextNode(responseText.question_text);
			txt_question_p .appendChild(question_text);
			test_question_div.appendChild(txt_question_p);
			question_add.appendChild(test_question_div);
			
			
			var form = document.createElement("form"); //form
			$(form).attr("action", "localhost:8000/response"); //
			$(form).attr("id", "assessmen_test");
			$(form).attr("method", "POST"); //method
			$(form).attr("class", "multicq");
			
			var label1 = document.createElement("label");
//			$(label1).attr("id","choice1");
			var option1 = document.createElement("input");
			$(option1).attr("type","checkbox");
			$(option1).attr("class","multicq");
			$(option1).attr("name","selected_choice");
			$(option1).attr("id","choice1");
			$(option1).attr("value",1); //onclick="document.getElementById('text').removeAttribute('disabled')
			$(option1).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')");
			var option_text1_node = document.createTextNode(responseText.choice1);
			label1.appendChild(option1)
			label1.appendChild(option_text1_node);
			form.appendChild(label1);
			var space1 = document.createElement("br");
			form.appendChild(space1);		

//option2	
			var label2 = document.createElement("label");
//			$(label2).attr("id","choice2");
			 option2 = document.createElement("input");
			$(option2).attr("type","checkbox");
			$(option2).attr("class","multicq");
			$(option2).attr("name","selected_choice");
			$(option2).attr("id","choice2");
			$(option2).attr("value",2);
			$(option2).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')"); //new to block submit button
			//$(option2).attr("id","choice2");
			var option_text2_node = document.createTextNode(responseText.choice2);
			label2.appendChild(option2);
			label2.appendChild(option_text2_node);
			form.appendChild(label2);
			var space2 = document.createElement("br");
			form.appendChild(space2);
			
//option3		
			var label3 = document.createElement("label");
//			$(label3).attr("id","choice3");
			var option3 = document.createElement("input");
			$(option3).attr("type","checkbox");
			$(option3).attr("class","multicq");
			$(option3).attr("name","selected_choice");
			$(option3).attr("value",3);
			$(option3).attr("id","choice3");
			$(option3).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')");
			var option_text3_node = document.createTextNode(responseText.choice3);
			label3.appendChild(option3);
			label3.appendChild(option_text3_node);
			form.appendChild(label3);
			var space3 = document.createElement("br");
			form.appendChild(space3);
			
//option4	
			var label4 = document.createElement("label");
//			$(label4).attr("id","choice4");
			var option4 = document.createElement("input");
			$(option4).attr("type","checkbox");
			$(option4).attr("class","multicq");
			$(option4).attr("name","selected_choice");
			$(option4).attr("value",4);
			$(option4).attr("id","choice4");
			$(option4).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')");
			var option_text4_node = document.createTextNode(responseText.choice4);
			label4.appendChild(option4)
			label4.appendChild(option_text4_node);
			form.appendChild(label4);
			var space4 = document.createElement("br");
			form.appendChild(space4);
			
			question_add.appendChild(form); 
			
			var submiss = document.createElement("button");
			$(submiss).addClass("btn btn-primary btn-lg button_check ");
			$(submiss).attr("id","submiss_type");
	//		$(submiss).attr(“disabled”, true);
			$( submiss  ).prop( "disabled", true );
			
			
			var submit = document.createTextNode("submit");
			submiss.appendChild(submit);
			$(submiss).attr("type", "submit");
			form.appendChild(submiss);
			question_add.appendChild(form);
			 
			 
		 }
		else if(q_type==="tf"){
		var  question_add = document.getElementById("instruction_question");
//			var elem = $(".instruction");
			
			var test_question_div = document.createElement("div");
			$(test_question_div).attr("id", q_type=responseText.question_id);
				
			var txt_question_p = document.createElement("p");
			$(txt_question_p).addClass("Current_question");
			var question_text = document.createTextNode(responseText.question_text);
			txt_question_p .appendChild(question_text);
			test_question_div.appendChild(txt_question_p);
			question_add.appendChild(test_question_div);
			
			
			var form = document.createElement("form"); //form
			$(form).attr("action", "localhost:8000/response"); //
			$(form).attr("id", "assessmen_test");
			$(form).attr("method", "POST"); //method
			$(form).attr("class", "tf");
			var label1 = document.createElement("label");
//			$(label1).attr("id","choice1");
			var option1 = document.createElement("input");
			$(option1).attr("id","choice2");
			$(option1).attr("type","radio");
			$(option1).attr("class","mcq");
			$(option1).attr("name","selected_choice");
			$(option1).attr("value",1); //onclick="document.getElementById('text').removeAttribute('disabled')
			$(option1).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')");
			var option_text1_node = document.createTextNode("True");
			label1.appendChild(option1)
			label1.appendChild(option_text1_node);
			form.appendChild(label1);
			var space1 = document.createElement("br");
			form.appendChild(space1);		

//option2	
			var label2 = document.createElement("label");
//			$(label2).attr("id","choice2");
			 option2 = document.createElement("input");
			$(option2).attr("type","radio");
			$(option2).attr("class","mcq");
			$(option2).attr("name","selected_choice");
			$(option2).attr("id","choice2");
			$(option2).attr("value",2);
			$(option2).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')"); //new to block submit button
			//$(option2).attr("id","choice2");
			var option_text2_node = document.createTextNode("False");
			label2.appendChild(option2);
			label2.appendChild(option_text2_node);
			form.appendChild(label2);
			var space2 = document.createElement("br");
			form.appendChild(space2);

			
			question_add.appendChild(form); 
			
			var submiss = document.createElement("button");
			$(submiss).addClass("btn btn-primary btn-lg button_check ");
			$(submiss).attr("id","submiss_type");
	//		$(submiss).attr(“disabled”, true);
			$( submiss  ).prop( "disabled", true );
			
			
			var submit = document.createTextNode("submit");
			submiss.appendChild(submit);
			$(submiss).attr("type", "submit");
			form.appendChild(submiss);
			question_add.appendChild(form);
			 
			 
			
			
		 } 
		 else if(q_type==="fill"){
		//	 alert(1);
			 var str="The writer recommends creating a _ kknknknk";
			 var n = str.indexOf("_");
			 var first = str.substring(0,n);
			 var second = str.substring(n+1,str.length);
			 
			var  question_add = document.getElementById("instruction_question");

			var test_question_div = document.createElement("div");
//			$(test_question_div).attr("id", q_type=responseText.question_id);
				
			var txt_question_p = document.createElement("p");
			$(txt_question_p).addClass("Current_question");
			var question_text = document.createTextNode("instruction");
			txt_question_p .appendChild(question_text);
			test_question_div.appendChild(txt_question_p);
			question_add.appendChild(test_question_div);
			
			var form = document.createElement("form"); //form
			$(form).attr("action", "localhost:8000/response"); //
			$(form).attr("id", "assessmen_test");
			$(form).attr("method", "POST"); //method
			$(form).attr("class", "fill");
			
			var txt_question_p2 = document.createElement("p");
			$(txt_question_p2).addClass("Current_question");
			var question_text2 = document.createTextNode(first);
			txt_question_p2.appendChild(question_text2);
			form.appendChild(txt_question_p2);
			
			
;
			var option1 = document.createElement("input");
			$(option1).attr("id","mytextarea");
			$(option1).attr("type","text");
			$(option1).attr("class","fill");
			$(option1).attr("name","selected_choice");
			$(option1).attr("onclick","document.getElementById('submiss_type').removeAttribute('disabled')");
			form.appendChild(option1);
			
			var txt_question_p3 = document.createElement("p");
			$(txt_question_p3).addClass("Current_question");
			var question_text3 = document.createTextNode(second);
			txt_question_p3.appendChild(question_text3);
			form.appendChild(txt_question_p3);

			
			var space1 = document.createElement("br");
			form.appendChild(space1);		

			question_add.appendChild(form);
			
//			question_add.appendChild(form); 
			
			
				
		
			var submiss = document.createElement("button");
			$(submiss).addClass("btn btn-primary btn-lg button_check ");
			$(submiss).attr("id","submiss_type");
	//		$(submiss).attr(“disabled”, true);
			$( submiss  ).prop( "disabled", true );
			
			
			var submit = document.createTextNode("submit");
			submiss.appendChild(submit);
			$(submiss).attr("type", "submit");
			form.appendChild(submiss);
//			question_add.appendChild(form);
			
			
			 
			 
		 }
		 
		 else if(q_type==="match"){ 
		 
			var  question_add = document.getElementById("instruction_question");
			
			var matchlabel1 = document.createElement("div");  //div
			$(matchlabel1).attr("id","choice1"); 
			var option1 = document.createElement("div"); //div
			$(option1).attr("id","option1"); 
			var option1p = document.createElement("p");
			$(option1p).addClass("matchoption");
			var option1p_text = document.createTextNode("match1a");
			option1p.appendChild(option1p_text);
			option1.appendChild(option1p);
			matchlabel1.appendChild(option1);
			var response1 = document.createElement("div"); //div
			$(response1).attr("id","response1"); 
			$(response1).attr("ondrop","drop(event)");
			$(response1).attr("ondragover","allowDrop(event)");
			var response1p = document.createElement("p");
			$(response1p).addClass("droptarget");
			$(response1p).attr("ondragstart","dragStart(event");
			$(response1p).attr("ondragend","dragEnd(event)");
			$(response1p).attr("draggable","true");
			$(response1p).attr("ondragover","allowDrop(event)");
			var response1p_text = document.createTextNode("match1b");
			response1p.appendChild(response1p_text);
			response1.appendChild(response1p);
			matchlabel1.appendChild(response1);
			
			var matchlabel2 = document.createElement("div");  //div
			$(matchlabel2).attr("id","choice1"); 
			var option2 = document.createElement("div"); //div
			$(option2).attr("id","option1"); 
			var option2p = document.createElement("p");
			$(option2p).addClass("matchoption");
			var option2p_text = document.createTextNode("match2a");
			option2p.appendChild(option2p_text);
			option2.appendChild(option2p);
			matchlabel2.appendChild(option2);
			var response2 = document.createElement("div"); //div
			$(response2).attr("id","response1"); 
			$(response2).attr("ondrop","drop(event)");
			$(response2).attr("ondragover","allowDrop(event)");
			var response2p = document.createElement("p");
			$(response2p).addClass("droptarget");
			$(response2p).attr("ondragstart","dragStart(event");
			$(response2p).attr("ondragend","dragEnd(event)");
			$(response2p).attr("draggable","true");
			$(response2p).attr("ondragover","allowDrop(event)");
			var response2p_text = document.createTextNode("match2b");
			response2p.appendChild(response2p_text);
			response2.appendChild(response2p);
			matchlabel2.appendChild(response2);
			
			
			
			
			question_add.appendChild(matchlabel1);
			question_add.appendChild(matchlabel2);
			 
		 } 
		 };

	};
	$( "#teststart1" ).click(function() {
		$("#teststart1").hide();
		
		$(".instruction").empty();
		myFunction();
		});
		
		
	$(".instruction").on("click","#submiss_type",function(e){
				var className = $('form').attr('class');
				if (className==="mcq"){
					var response = $('input:radio[name=selected_choice]:checked').val();
					alert(response);
				}
				if (className==="multicq"){ 
				    arr=[];
					for (i=0;i<4;i++) {
					j = i+1
					var x = document.getElementById("choice"+j).checked;
					var response = $('input:checkbox[name=selected_choice]:checked').val();
					arr[i]=x;
					}
					alert(arr);
				}
				if (className==="tf"){
					var response = $('input:radio[name=selected_choice]:checked').val();
					alert(response);
					
				}
				
				if (className==="fill"){
//					var response = $('input:radio[name=selected_choice]:checked').val();
					var x = document.getElementById("mytextarea").value;
					alert(x);
					
				}
				
			
			var responseText={q_no:"20"};
		if (responseText.q_no===20) {
			alert("test over");
			
		}
		
		
		
		});
		
	
	
});

	function dragStart(event) {     
	//event.dataTransfer.effectAllowed = "pointer";
	$('body').css('cursor', 'pointer');
	starttext =  event.target;
	alert(starttext);
	starttext.id =  event.target.id;
	startparent = starttext.parentNode;
    event.dataTransfer.setData("Text", starttext.textContent);
 //   document.getElementById("demo").innerHTML = "Started to drag the p element";
	}

	function dragEnd(event) {
    $('body').css('cursor', 'default');
 //   document.getElementById("demo").innerHTML = "Finished dragging the p element.";
	}

	function allowDrop(event) {
  
    event.preventDefault();
	}

	function drop(event) {
	//alert(1);
    event.preventDefault();
	targetparent = event.target;
	targettext = targetparent.textContent;
	
	 data = event.dataTransfer.getData("Text").trim();
	 alert(data);
	 targetparent.innerHTML=data ;    // + '<span class="up_down glyphicon glyphicon-resize-vertical"></span>';
	 starttext.innerHTML=targettext ;    //+ '<span class="up_down glyphicon glyphicon-resize-vertical"></span>';
//f (targetChildren.length>0)  

//(startparent).append(targetChildren);
	//targetChildren ).remove();
//argetparent.appendChild(document.getElementById(data));
//
	}
		


/*
on ready 
on test start button 
first request for question 
after submission of response send response to server then next 
until 20th after it 

*/