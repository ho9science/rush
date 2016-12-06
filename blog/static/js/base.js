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
		beforeSend : function(){
			$("#result_tbody").empty();
		},
		success : function(json){
			$("#id_srch").val('');
			var data = JSON.parse(json);
			$("#result_tbody").append("<tr><th> </th><th>2015</th></tr>");
			$("#result_tbody").append("<tr><td>code</td><td><a title='stock code'>"+data[0].pk+"</a></td></tr>");
			$("#result_tbody").append("<tr><td>매출액</td><td>"+data[0].fields.sales+"</td></tr>");
			$("#result_tbody").append("<tr><td>영업이익</td><td>"+data[0].fields.businessprofits+"</td></tr>");
			$("#result_tbody").append("<tr><td>세전계속사업이익</td><td>"+data[0].fields.continuing+"</td></tr>");
			$("#result_tbody").append("<tr><td>당기순이익</td><td>"+data[0].fields.netincome+"</td></tr>");
			$("#result_tbody").append("<tr><td>당기순이익(지배)</td><td>"+data[0].fields.netincomeruling+"</td></tr>");
			$("#result_tbody").append("<tr><td>당기순이익(비지배)</td><td>"+data[0].fields.netincomenon+"</td></tr>");
			$("#result_tbody").append("<tr><td>자산총계</td><td>"+data[0].fields.asset+"</td></tr>");
			$("#result_tbody").append("<tr><td>부채총계</td><td>"+data[0].fields.liabilities+"</td></tr>");
			$("#result_tbody").append("<tr><td>자본총계</td><td>"+data[0].fields.totalequities+"</td></tr>");
			$("#result_tbody").append("<tr><td>자본총계(지배)</td><td>"+data[0].fields.totalequitiesruling+"</td></tr>");
			$("#result_tbody").append("<tr><td>자본총계(비지배)</td><td>"+data[0].fields.totalequitiesnon+"</td></tr>");
			$("#result_tbody").append("<tr><td>자본금</td><td>"+data[0].fields.eqities+"</td></tr>");
			$("#result_tbody").append("<tr><td>영업활동현금흐름</td><td>"+data[0].fields.cashbusiness+"</td></tr>");
			$("#result_tbody").append("<tr><td>투자활동현금흐름</td><td>"+data[0].fields.cashinvestment+"</td></tr>");
			$("#result_tbody").append("<tr><td>재무활동현금흐름</td><td>"+data[0].fields.cashfinance+"</td></tr>");
			$("#result_tbody").append("<tr><td>CAPEX</td><td>"+data[0].fields.capex+"</td></tr>");
			$("#result_tbody").append("<tr><td>FCF</td><td>"+data[0].fields.fcf+"</td></tr>");
			$("#result_tbody").append("<tr><td>이자발생부채</td><td>"+data[0].fields.ibl+"</td></tr>");
			$("#result_tbody").append("<tr><td>영업이익률</td><td>"+data[0].fields.roop+"</td></tr>");
			$("#result_tbody").append("<tr><td>순이익률</td><td>"+data[0].fields.netprofitmargin+"</td></tr>");
			$("#result_tbody").append("<tr><td>ROE</td><td>"+data[0].fields.roe+"</td></tr>");
			$("#result_tbody").append("<tr><td>ROA</td><td>"+data[0].fields.roa+"</td></tr>");
			$("#result_tbody").append("<tr><td>부채비율</td><td>"+data[0].fields.debtratio+"</td></tr>");
			$("#result_tbody").append("<tr><td>자본유보율</td><td>"+data[0].fields.err+"</td></tr>");
			$("#result_tbody").append("<tr><td>EPS</td><td>"+data[0].fields.eps+"</td></tr>");
			$("#result_tbody").append("<tr><td>PER</td><td>"+data[0].fields.per+"</td></tr>");
			$("#result_tbody").append("<tr><td>BPS</td><td>"+data[0].fields.bps+"</td></tr>");
			$("#result_tbody").append("<tr><td>PBR</td><td>"+data[0].fields.pbr+"</td></tr>");
			$("#result_tbody").append("<tr><td>현금DPS</td><td>"+data[0].fields.dps+"</td></tr>");
			$("#result_tbody").append("<tr><td>현금배당수익률</td><td>"+data[0].fields.rcdp+"</td></tr>");
			$("#result_tbody").append("<tr><td>현금배당성향</td><td>"+data[0].fields.cdr+"</td></tr>");
			$("#result_tbody").append("<tr><td>주식수</td><td>"+data[0].fields.stock+"</td></tr>");
		},
		error : function(xhr){
			console.log(xhr.status+": "+xhr.responseText);
		}
	})
}
// using jQuery
