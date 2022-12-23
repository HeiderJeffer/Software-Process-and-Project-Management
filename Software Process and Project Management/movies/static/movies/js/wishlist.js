var manage_wishlist =function()
{
	var button_id  = jQuery(this).get(0).id
  var id = jQuery(this).data("id");
  var data = id.split("-");
  var data = {
    movie_id:Number(data[0]),
    user_id:Number(data[1])
  };
  if(button_id === "remove-wishlist")
  { jQuery.ajax({
            
            type: "POST",
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            contentType: "application/json",
            url:"/movies/remove-wishlist/",
            data: JSON.stringify(data),
            success:function(response){
              $(document).ajaxStop(function() { location.reload(true); });
          }
        });
  }
  else if(button_id === "add-wishlist")
  {
    jQuery.ajax({
            
          type: "POST",
          headers: { "X-CSRFToken": getCookie("csrftoken") },
          contentType: "application/json",
          url:"/movies/add-wishlist/",
          data: JSON.stringify(data),
          success:function(response){
            $(document).ajaxStop(function() { location.reload(true); });
        }
      }); 
  }
}
function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

jQuery(function(){
  $('.portfolio-item').on('click', '.the-buttons',manage_wishlist)
})