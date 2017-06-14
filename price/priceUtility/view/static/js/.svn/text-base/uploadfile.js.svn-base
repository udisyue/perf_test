
$(document).ready(function(){

	$('#upload').click(function(){
		$.ajaxFileUpload({
			url: "./Upload",
			secureuri:false,
			type: 'post',
			fileElementId:'searchCondition',
			dataType:'json',
			//data: "searchCondition="+fileName,
			//contentType: 'multipart/form-data',
			success: function(data, status){
				alert('abcd');
				$('#uploadStatus').html(data);	
			},
			error: function (data, status, e){

				$('#uploadStatus').html(data);	
				alert('test');
				//alert(e);
			}
		});

	});
}
);