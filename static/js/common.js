jQuery.noConflict();
jQuery(document).ready(function(){

	//表格行，鼠标放上去变色
	jQuery(".tr:odd").css("background", "#FFFCEA");
	jQuery(".tr:odd").each(function(){
		jQuery(this).hover(function(){
			jQuery(this).css("background-color", "#FFE1FF");
		}, function(){
			jQuery(this).css("background-color", "#FFFCEA");
		});
	});
	jQuery(".tr:even").each(function(){
		jQuery(this).hover(function(){
			jQuery(this).css("background-color", "#FFE1FF");
		}, function(){
			jQuery(this).css("background-color", "#fff");
		});
	}); 

	/*ie6,7下拉框美化*/
    if ( jQuery.browser.msie ){
    	if(jQuery.browser.version == '7.0' || jQuery.browser.version == '6.0'){
    		jQuery('.select').each(function(i){
			   $(this).parents('.select_border,.select_containers').width(jQuery(this).width()+5);
			 });
    		
    	}
    }
 
});