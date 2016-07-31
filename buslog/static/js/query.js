$(document).ready(function(){
	$("#select-choferes").change(function(){
		var pk = $(this).val();
		console.log("selected chofer with pk:", pk);
	});
});