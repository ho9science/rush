//samdasu
function gold_post(){

	console.log("is working");
	var csrf = $("input[name='csrfmiddlewaretoken']").val();
	var srch = $('#id_srch').val();
	console.log(srch)
	$.ajax({
		url : "/gold_post/",
		type : "POST",
		data : { 'samdasu' : srch, 'csrfmiddlewaretoken': csrf },
		success : function(json){
			$("#id_srch").val('');
			$("#result_tbody").append("<tr><th> </th><th>2015</th></tr>");
			$("#result_tbody").append("<tr><td>samdasu</td><td>"+json.samdasu+"</td></tr>");
			
			console.log("success");
		},
		error : function(xhr){
			console.log(xhr.status+": "+xhr.responseText);
		}
	})
}
// using jQuery
