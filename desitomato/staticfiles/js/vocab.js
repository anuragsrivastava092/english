$(document).ready(function(){
	for (i = 0; i< vocab_lit.length; i++) { 
		//parent 
		 voacab_k=i+1;
		
		vocab_list = $(".vocab_list");
	
		
		 vocab_list_div = document.createElement("div");
		$(vocab_list_div).addClass("vocab_list_word_number");
		$(vocab_list_div).attr("id", voacab_k);
		// child count
		 vocab_list_count_h2 = document.createElement("h2");
		$(vocab_list_count_h2).addClass("vocab_list_count");
		$(vocab_list_count_h2).attr("id", "vocab_list_count" + voacab_k);
		 vocab_list_count_h2_text = document.createTextNode(voacab_k);
		$(vocab_list_count_h2).append(vocab_list_count_h2_text);
		$(vocab_list_div).append(vocab_list_count_h2);
		
		// child word
		vocab_list_word_h2 = document.createElement("h2");
		$(vocab_list_word_h2).addClass("vocab_list_word");
		$(vocab_list_word_h2).attr("id", "vocab_list_word" + voacab_k);
		 vocab_list_word_h2_text = document.createTextNode(vocab_lit[i].word);
		$(vocab_list_word_h2).append(vocab_list_word_h2_text);
		$(vocab_list_div).append(vocab_list_word_h2);
		
		vocab_list_meaning_h2 = document.createElement("h2");
		$(vocab_list_meaning_h2).addClass("vocab_list_meaning");
		$(vocab_list_meaning_h2).attr("id", "vocab_list_meaning" + voacab_k);
		 vocab_list_meaning_h2_text = document.createTextNode(vocab_lit[i].word_meaning);
		$(vocab_list_meaning_h2).append(vocab_list_meaning_h2_text);
		$(vocab_list_div).append(vocab_list_meaning_h2);

		set = vocab_lit[i].sentence;
		if (typeof(set) =="undefined" ) {
			a=0;
		}
		else{
			a=1;
		}


		if (a===1) {
		vocab_list_sentence_h2 = document.createElement("h2");
		$(vocab_list_sentence_h2).addClass("vocab_list_sentence");
		$(vocab_list_sentence_h2).attr("id", "vocab_list_sentence" + voacab_k);
		 vocab_list_sentence_h2_text = document.createTextNode(vocab_lit[i].sentence);
		$(vocab_list_sentence_h2).append(vocab_list_sentence_h2_text);
		$(vocab_list_div).append(vocab_list_sentence_h2);
	}
		set = vocab_lit[i].sentence;
		if (typeof(set)  =="undefined" ){
			b=0;
		}
		else{
			b=1;
		}


		if (b===1) {

		
		vocab_list_article_h2 = document.createElement("h2");
		$(vocab_list_article_h2).addClass("vocab_list_article");
		$(vocab_list_article_h2).attr("id", "vocab_list_article" + voacab_k);
		 vocab_list_article_h2_text = document.createTextNode(vocab_lit[i].article);
		$(vocab_list_article_h2).append(vocab_list_article_h2_text);
		$(vocab_list_div).append(vocab_list_article_h2);
		
		}
	
		
		$(vocab_list).append(vocab_list_div);
		
	}
 
 
});



	



