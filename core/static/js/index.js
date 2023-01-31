

$(document).ready(function(){
    $.get("https://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8",
    function(data){
        $.each(data.data, function(i,item){
            $("#categorias").append(
                "<tr>"+
                "<td>"+item.common_name+"</td>"+
                "<td>"+item.scientific_name+"</td>"+
                "<td><img src='"+item.image_url+"'></img></td>"+
                "<td>"+item.bibliography+"</td>"+
                "</tr>"
            );
        });
    });
});




// $(document).ready(function() {
//     fetch("https://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8")
//         .then(response => response.json())
//         .then(data => {
//             data.data.forEach(item => {
//                 $("#categorias").append(
//                         "<tr>"+
//                         "<td>"+item.common_name+"</td>"+
//                         "<td>"+item.scientific_name+"</td>"+
//                         "<td><img src='"+item.image_url+"'></img></td>"+
//                         "<td>"+item.bibliography+"</td>"+
//                         "</tr>"
//                 );
//             });
//         });
// });




