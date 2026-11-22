function cptaajaxPagination(pnumber,plimit){
	jQuery('.lodear').css('display','block');
	var nth  = pnumber;
	var lmt  = plimit;
	var ajax_url = ajax_params.ajax_url;
	var cpta = jQuery("#post").attr('data-posttype');
	var cptacat = jQuery("#post").attr('data-cattype');
	var cptatax = jQuery("#post").attr('data-taxname');
		var author = jQuery('#author_list').val();
			//alert(author);	
	jQuery.ajax({
		url		:ajax_url,
		type	:'post',
		data	:{ 'action':'cptapagination','number':nth,'limit':lmt,'cptapost':cpta,'cptacatname':cptacat,'cptataxname':cptatax,'author':author },
		beforeSend	: function(){
			//jQuery("#cptapagination-content").html("<p style='text-align:center;'>Loading please wait...!</p>");
			//jQuery('#myblog_loder').html('<img src="<?php echo  get_template_directory_uri(); ?>/images/ajax-loader.gif" class="lodear">');
			
		},
		success :function(pvalue){
			jQuery("#cptapagination-content").html(pvalue);
			jQuery('.lodear').css('display','none');
		}
	});
}