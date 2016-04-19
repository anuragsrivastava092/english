$(document).ready(function(){
	
   question = 0;
   question_type='';
	
	function myFunction(responseText,responseOption) {
	//	alert(responseText.id);
		var account={ "question_id":2};
		
	//	responseText ={q_type:"mcq",question_id:1,question_text:"what is your name",choice1:"kamal",choice2:"tarun",choice3:"kapil",choice4:"chirag"};
		 var q_type=responseText.question_type;
		 if(q_type==="1") {
			 var  question_add = document.getElementById("instruction_question");
			var elem = $(".instruction");
			
			var test_question_div = document.createElement("div");
			$(test_question_div).attr("id", q_type=responseText.id);
				
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
			
			var label1 = document.createElement("label");
			$(label1).attr("id","choice1");
			var option1 = document.createElement("input");
			$(option1).attr("type","radio");
			$(option1).attr("name","selected_choice");
			$(option1).attr("value",1);
			var option_text1_node = document.createTextNode(responseOption.choice1);
			label1.appendChild(option1)
			label1.appendChild(option_text1_node);
			form.appendChild(label1);
			var space1 = document.createElement("br");
			form.appendChild(space1);		

//option2	
			var label2 = document.createElement("label");
			$(label2).attr("id","choice2");
			 option2 = document.createElement("input");
			$(option2).attr("type","radio");
			$(option2).attr("name","selected_choice");
			$(option2).attr("id","choice2");
			$(option2).attr("value",2);
			//$(option2).attr("id","choice2");
			var option_text2_node = document.createTextNode(responseOption.choice2);
			label2.appendChild(option2);
			label2.appendChild(option_text2_node);
			form.appendChild(label2);
			var space2 = document.createElement("br");
			form.appendChild(space2);
			
//option3		
			var label3 = document.createElement("label");
			$(label3).attr("id","choice3");
			var option3 = document.createElement("input");
			$(option3).attr("type","radio");
			$(option3).attr("name","selected_choice");
			$(option3).attr("value",3);
			$(option3).attr("id","choice3");
			var option_text3_node = document.createTextNode(responseOption.choice3);
			label3.appendChild(option3);
			label3.appendChild(option_text3_node);
			form.appendChild(label3);
			var space3 = document.createElement("br");
			form.appendChild(space3);
			
//option4	
			var label4 = document.createElement("label");
			$(label4).attr("id","choice4");
			var option4 = document.createElement("input");
			$(option4).attr("type","radio");
			$(option4).attr("name","selected_choice");
			$(option4).attr("value",4);
			$(option4).attr("id","choice4");
			var option_text4_node = document.createTextNode(responseOption.choice4);
			label4.appendChild(option4)
			label4.appendChild(option_text4_node);
			form.appendChild(label4);
			var space4 = document.createElement("br");
			form.appendChild(space4);
			
			question_add.appendChild(form); 
			
			var submiss = document.createElement("button");
			$(submiss).addClass("btn btn-primary btn-lg button_check ");
			$(submiss).attr("id","submiss_type");
			
			var submit = document.createTextNode("submit");
			submiss.appendChild(submit);
			$(submiss).attr("type", "submit");
			form.appendChild(submiss);
			question_add.appendChild(form);
			 
			 
		 }
		 else if(q_type==="match"){   
			var matchlabel1 = document.createElement("div"); 
			$(label1).attr("id","choice1");  
			var matchoption1 = document.createElement("p"); 
			$(matchoption1).attr("class","matchoption");
			$(matchoption1).attr("id","1matchoption");   matchans
			var matchresponse= document.createElement("div");
			$(matchresponse).attr("class","dropparent");
			$(matchresponse).attr("ondrop","drop(event)");
			$(matchresponse).attr("ondragover","allowDrop(event)");
			$(matchresponse).attr("id","allow1");
			var matchans = document.createElement("p"); 
			$(matchans).attr("class","droptarget");
			$(matchans).attr("ondragstart","dragStart(event)");
			$(matchans).attr("ondragend","dragEnd(event)");
			$(matchans).attr("draggable","true");
			$(matchans).attr("id","dragtarget");
			

			matchresponse.appendChild(matchans);

			} 
/*		 
		else if(q_type==="multicq"){
			 
			 
		 } 
		 else if(q_type==="tf"){
		 } 
		 else if(q_type==="fill"){
		 } 
		 
		 

			*/
		 question+=1;
		question_type='q_type';
	};
	$( "#teststart1" ).click(function(e) {
		e.preventDefault();
		//alert(2);
		
		
		
		$("#teststart1").hide();
		
		$(".instruction").empty();
		myFunction(responseText,responseOption);
		});
		
		
	$(".instruction").on("click","#submiss_type",function(e){
					ppp={};
					var response = $('input:radio[name=selected_choice]:checked').val();
				//	var response="";
					ppp["selected_choice"] = response;
				//	alert(JSON.stringify(ppp));
			var xhr = new XMLHttpRequest();
			var url = "http://localhost:8000/ass/"; //path de api ka 
			xhr.open("POST", url);
		//	xhr.setRequestHeader('Content-Type', "application/x-www-form-urlencoded",true);
			xhr.send(JSON.stringify(ppp));  //send response
			xhr.onreadystatechange = function() {
				 if (xhr.readyState == 4 && xhr.status == 200) {
				  responsereply = xhr.responseText;
				 alert(responsereply );
				  obj = JSON.parse(responsereply);
			//	 alert(obj);
				 $(".instruction").empty();
				 if (question===6) {
					//	alert("test over");
		
			window.location.assign("http://localhost:8000/review/");
			} 
			   //  myFunction(obj[0],obj[1]);
				 else{
					myFunction(obj[0],obj[1]); 
				 }
				 }
			}
			
			var responseText={q_no:"20"};
		
		
		
		
		});
		
	
});

/*
on ready 
on test start button 
first request for question 
after submission of response send response to server then next 
until 20th after it 

*/