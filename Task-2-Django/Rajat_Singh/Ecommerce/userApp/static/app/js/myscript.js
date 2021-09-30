$('#slider1, #slider2, #slider3,#slider4').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var elm = this.parentNode.children[2]
    //console.log(id)
    
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data: {

            prod_id: id
        },
           success: function(data){

              //console.log(data)
              //console.log("succes")
              elm.innerText = data.Quantity
              document.getElementById("ammountHtml").innerText = data.amount
              document.getElementById("TotalAmoutHtml").innerText = data.totalamounts




            }  

    })

    
})


$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var elm = this.parentNode.children[2]
    //console.log(id)
    
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data: {

            prod_id: id
        },
           success: function(data){

              //console.log(data)
              //console.log("succes")
              elm.innerText = data.Quantity
              document.getElementById("ammountHtml").innerText = data.amount
              document.getElementById("TotalAmoutHtml").innerText = data.totalamounts




            }  

    })

    
})





$('.Remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var elm = this
    //console.log(id)
    
    $.ajax({
        type:"GET",
        url:"/Removecart",
        data: {

            prod_id: id
        },
           success: function(data){

              //console.log(data)
              //console.log("succes")
              document.getElementById("ammountHtml").innerText = data.amount
              document.getElementById("TotalAmoutHtml").innerText = data.totalamounts
              elm.parentNode.parentNode.parentNode.parentNode.remove()




            }  

    })

    
})

