$(document).ready(function(){
	//$("h2").on("click", "p.test", function(){
	//$("p span").click(function(){
	$("#jsfiddel").on("click","p span",function(){
		
		current = this;
		question_id = $(current).attr("id");
		
	// finding question id
		//var question_detail = [{"question_id__id":1, "question_id__question_text":"vyvjhvyhvv","choice1":"ad","choice2":"g","choice3":"f","choice1":"gvh"}];
		//find question element
		//find option element
		for (i = 0; i< question_content.length; i++) {
		if (question_content[i].id.toString() === question_id) { break; }
		
	}
	for (j = 0; j < option_content.length; j++) {
		if (option_content[j].sample_question_id.toString() === question_id) { break; }
		
	}



	//finding object
		elem = $(current).parent();
		var txt3 = document.createElement("p");  // Create with DOM
		var node = document.createTextNode(question_content[i].question_text);
		txt3.appendChild(node);
		$(txt3).addClass("Current_question");
		$(txt3).attr("id", question_id);
		//var txt3 = document.createElement("p"); 
		//$(this).parent().last().append(txt3);
		var optionA = document.createElement("div");
		$(optionA).addClass("optionA");
		var response_optionA = document.createTextNode(option_content[j].choice1);
		optionA.appendChild(response_optionA);
		
		
		var optionB = document.createElement("div");
		$(optionB).addClass("optionB");
		var response_optionB = document.createTextNode(option_content[j].choice2);
		optionB.appendChild(response_optionB);

		
		var optionC = document.createElement("div");
		$(optionC).addClass("optionC");
		var response_optionC = document.createTextNode(option_content[j].choice3);
		optionC.appendChild(response_optionC);

		var optionD = document.createElement("div");
		$(optionD).addClass("optionD");
		var response_optionD = document.createTextNode(option_content[j].choice4);
		optionD.appendChild(response_optionD);

		var submiss = document.createElement("button");
		$(submiss).addClass("btn btn-primary btn-lg");
		var submit = document.createTextNode("submit");
		submiss.appendChild(submit);
		$(submiss).attr("type", "submit");
		var txt9 = document.createElement("div");
		$(txt9).addClass("glyphicon glyphicon-remove close_button");
		txt3.appendChild(txt9);
		txt3.appendChild(optionA);
		txt3.appendChild(optionB);
		txt3.appendChild(optionC);
		txt3.appendChild(optionD);
		txt3.appendChild(submiss);
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
		
	 var aaa = ' <p class="title"><span class="comprehension" id ="1"> Republic Day parade: India showcases military might,French troops march in a first </span></p>  <p>NEW DELHI: India\'s military <span class="vocab" id ="hack1">prowess </span> and  \achievements  in different fields, state-of-the-art defence,diverse cultural and social traditions and the government\'s emphasis \on self-reliance dominated the showcase at New Delhi\'s Rajpath on the country\'s 67th Republic Day.</p> <p> For the first time in the history of Republic Day parades, a 123-member French Army <span class="vocab" id = "hack2"  >contingent</span> marched on  Rajpath \
	 and present a ceremonial salute to the President Pranab Mukherjee,  as guest of honor Francois Hollande watched and clapped \
	 seated next to Prime Minister Narendra Modi</p> <p> Another first, after a gap of 26 years, was the \
	 march by an Army dog squad drawn from the RemountVeterinary Corps along with their \
	 handlers.</p> <p><span class="comprehension" id ="comp2">Sticking to the 66-year-old tradition</span>, the colourful Border \
	 Security Force regiment consisting of 56 camels also marched down the Rajpath. For the first time the \parade also witnessed an ex-servicemen tableau where army veterans showcased their role in nation building. </p> <p> Among the weapons on display were the army\'s missile <span class="grammar" id ="gram1">firing</span> capability T-90 Bhishma tank,Infantry Combat Vehicle BMP II (Sarath), Mobile Autonomous Launcher \ of the BrahMos Missile System, Akash weapon system, Smerch Launcher Vehicles and Integrated Communication Electronic Warfare System</p> <p> An <span class="comprehension" id ="comp3">Indian Air Force tableau</span>, themed \'Humanitarian Assistance and Disaster Relief \
 Operations by IAF: \
 In Service of the Nation and Beyond\' showcased models of C-17 Globemaster, C-130 Hercules and MI-17V5 aircraft,\
 emphasising its use in the IAF\'s recent rescue and relief operations in Uttarakhand, Jammu and Kashmir, Yemen and Nepal.</p>\
 <p> The Indian Navy\'s tableau displayed flight deck operations on the new aircraft carrier Vikrant,\
 under construction at the Kochi shipyard,\
 and the indigenously constructed submarine Kalvari by Mazagaon Dock, Mumbai, having a Made in India tag on them.</p> \
 <p> There was a <span class="vocab" id="hack3" >scintillating</span> display of folk and classical dances and performances by school \
 children from Delhi and other parts of India.</p> \
 <p> One of the highlights of the two-hour event at Rajpath was the stunts by \
 daredevils<span class="grammar" id ="gram2"> belonging</span> to the Army Signal Corps as they made various formations on motorbikes.</p> \
 <p> The parade ended with flypasts and stunts over Rajpath by Jaguars and other aircraft, \
  though low visibility due to fog made it difficult for thousands of cheering speactators below to enjoy the display.</p> \
 <p> Delhi was turned into a virtual fortress as an <span class=\"vocab\" id =\"hack4\">unprecedented</span> ground-to-air security cover \
 with thousands of armed  \
 personnel kept a tight vigil for the Republic Day celebrations.</p> ' ;
	 
 var html ='<p class="title"><span class="\
  comprehension\" id ="comp1"> \
 Republic  id kk\'s Day parade: India showcases military might, French troops march in a first </span></p>';
 var lla = "fvgbh";
 $("#jsfiddel").append(article_content);
});


	



