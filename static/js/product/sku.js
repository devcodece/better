
function jumpTo(id){
    //location.href = "{% url 'home' %}"
    location.hash = "#" + id
    }




//let currentUrl = document.getElementById('cUrl')
//let cUrl = currentUrl.innerHTML
//alert(cUrl)

//AJAX with jquery
/* var $ = jQuery.noConflict(); */

/* function listSku(){
    $.ajax({
        url:"/create-sku/",
        type:"get",
        //dataType:"json",
        success: function(response){
            console.log(response)
        },
        error: function(e){
            console.log(e)
        }
    })
} */

/* $(document).ready(function(){
    $(document).on('submit', '#form_sku', function(){
        $.ajax({
            type:'post',
            url:'/create-sku/',
            data: data,

            success:function(data){
                $('#elements').html(data).fadeIn()
            }
        })
        return false
    })
}) */