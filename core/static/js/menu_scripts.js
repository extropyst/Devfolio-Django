

// fetch("https://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8"

// // , {
// //     mode: 'cors',
// //     headers: {
// //         "Access-Control-Allow-Origin": '*'
// //     }
// // }

// )
//         .then(response => response.json())
//         .then(data => {
//             data.data.forEach(item => {
//               console.log(item.id, item.scientific_name, item.common_name, item.bibliography)

//             });
//         });


// fetch("https://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8")
// .then(response => response.json())
// .then(data => {
//     data.data.forEach(item => {
//         $("#categorias").append(item.id, item.scientific_name, item.common_name, item.bibliography

//         );
//     });
// });







// fetch("https://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8")
// .then(response => response.json())
// .then(data => {
//    let tableContent = "<table>";

//    // Genera la tabla HTML
//    data.data.forEach(item => {
//       tableContent += `<tr>
//                        <td>${item.name}</td>
//                        <td>${item.family}</td>
//                        <td>${item.genus}</td>
//                        </tr>`;
//    });
//    tableContent += "</table>";

//    // Agregar el contenido de la tabla al documento DOM 
//    document.getElementById("table_div").innerHTML = tableContent;
// });



// $(document).ready(function(){
//     fetch("https://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8") 
//         .then(response => response.json()) 
//         .then(data => { 
//             let table = document.createElement('table');
//             data.data.forEach(item => { 
//                 let tr = document.createElement('tr');
//                 let td1 = document.createElement('td');
//                 let td2 = document.createElement('td');
//                 td1.innerHTML = item.name; 
//                 td2.innerHTML = item.id; 
//                 tr.appendChild(td1); 
//                 tr.appendChild(td2); 
//                 table.appendChild(tr);
//             });

//         document.body.appendChild(table);
//     });
// });



// $(document).ready(function(){
    //     var table = $("#myTable");
    //     fetch("https://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8")
    //         .then(response => response.json())
    //         .then(data => { 
    //             data.data.forEach(item => {
    //                 var row = $("<tr />");
    //                 //Create each row in the table by adding a new 'td' element
    //                 $("<td />").text(item.id).appendTo(row);
    //                 $("<td />").text(item.name).appendTo(row);
    //                 $("<td />").text(item.common_name).appendTo(row);
    //                 //add this row to the end of table
    //                 row.appendTo(table);
    //             });
    //         });
    // });











// var myObject = { 
//     "clave con espacio": "valor"
// };

// // Obtener el valor de la clave
// var value = myObject["clave con espacio"];

// "<td>img src="+item["Species Illustration Photo"]+"></img></td>"+


// $(document).ready(function(){
//     $.get("https://www.fishwatch.gov/api/species",
//     function(data){
//         $.each(data, function(i,item){
//             $("#categorias").append(
//                 "<tr>"+
//                 "<td>"+item.Habitat+"</td>"+
//                 "<td>"+item.Habitat+"</td>"+
//                 "<td>"+item.Location+"</td>"+
//                 "<td>"+item.Population+"</td>"+
//                 "</tr>"
//             );
//         });
//     });
// });



// $(document).ready(function(){
//     $.get("https://www.fishwatch.gov/api/species",
//     function(data){
//         $.each(data.data, function(i,item){
//             $("#categorias").append(
//                 "<tr>"+
//                 "<td>"+item.Species Name+"</td>"+
//                 "<td>"+item.Scientific Name+"</td>"+
//                 "<td>"+item.Environmental Considerations+"</td>"+
//                 "<td>"+item.Physical Description+"</td>"+
//                 "</tr>"
//             );
//         });
//     });
// });




// $.ajax({
//     url: 'https://www.fishwatch.gov/api/species',
//     type: 'GET',
//     success: function(data) {
//         // Almacenar los datos en una variable
//         var apiData = data;
//     }
// })





// // Crear una tabla HTML
// var table = $('<table>');

// // Obtener los datos de la API utilizando el bucle for
// for(var i=0; i < apiData.length; i++) {

//     // Crear una tabla de filas
//     var row = $('<tr>');
    
//     // Obtener los datos de API
//     var name = apiData[i]['name'];
//     var shortName = apiData[i]['short_name'];
//     var scientificName = apiData[i]['scientific_name'];
    
//     // Agregar los datos a la tabla de filas
//     row.append('<td>'+name+'</td>');
//     row.append('<td>'+shortName+'</td>');
//     row.append('<td>'+scientificName+'</td>');
    
//     // Agregar la fila a la tabla
//     table.append(row);
// }

// ('#myTable').append(table);













// const settings = {
// 	"async": true,
// 	"crossDomain": true,
// 	"url": "https://horizon-trees-services.p.rapidapi.com/%7BPATH%7D",
// 	"method": "GET",
// 	"headers": {}
// };

// $.ajax(settings).done(function (response) {
// 	console.log(response);
// });





// $(document).ready(function(){
//     $.getJSON("https://www.themealdb.com/api/json/v1/1/categories.php", function(data) {
//         var table = "<table>";
//         table += "<tr><th>Plant Name</th><th>Family Name</th><th>Common Name</th></tr>"
//         $.each(data, function(key, value){
//             table += "<tr>";
//             table += "<td>" + value.idCategory + "</td>";
//             table += "<td>" + value.strCategory + "</td>";
//             table += "<td>" + strCategoryDescription + "</td>";
//             table += "</tr>";
//         });
//         table += "</table>";
//         $("#dataTable").html(table);
//     });

// });








$(document).ready(function(){
    $.get("http://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8",
    function(data){
        $.each(data.data, function(i,item){
            $("#categorias").append(
                "<tr>"+
                "<td>"+item.common_name+"</td>"+
                "<td>"+item.scientific_name+"</td>"+
                "<td><img src='"+item.image_url+"'></img></td>"+
                "<td>"+item.genus+"</td>"+
                "</tr>"
            );
        });
    });
});







// let request = new XMLHttpRequest();
// request.open("GET", "http://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8");
// request.send();

// request.onload = function() {
//     if (request.status === 200) {
//         let data = JSON.parse(request.response);

//         let table = "<table>";
//         table += "<tr><th>Plant Name</th><th>Family Name</th><th>Common Name</th></tr>"

//         data.forEach(function(value){
//             table += "<tr>";
//             table += "<td>" + value.scientific_name + "</td>";
//             table += "<td>" + value.family_common_name + "</td>";
//             table += "<td>" + value.common_name + "</td>";
//             table += "</tr>";
//         });
    
//         table += "</table>";
//         document.getElementById("dataTable").innerHTML = table;
//     }
// }




//recupera los datos de la API como un objeto json
fetch("https://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8Y")
    .then((response) => response.json())
    .then((data) => {
        //crea la tabla
        let tabla = document.createElement('table');
        tabla.border = 1;

        //recorre los resultados y agrega el contenido a la tabla
        data.result.forEach(element => {
            //crea una fila
            let row = tabla.insertRow();

            //agrega el nombre
            let nombre = row.insertCell();
            nombre.innerHTML = element.name;

            //agrega la familia
            let familia = row.insertCell();
            familia.innerHTML = element.family;

            //agrega la distribución
            let distribucion = row.insertCell();
            distribucion.innerHTML = element.distribution;
        });

        //agrega la tabla al documento
        document.body.appendChild(tabla);

    });     





// $(document).ready(function() {
//     $.ajax({
//         url: "http://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8",
//         method: 'GET',
//         success: function(data) {
//             var table = "<table>";
//             table += "<tr><th>Plant Name</th><th>Family Name</th><th>Common Name</th></tr>"
//             $.each(data.Data, function(key, value){
//                 table += "<tr>";
//                 table += "<td>" + value.scientific_name + "</td>";
//                 table += "<td>" + value.family_common_name + "</td>";
//                 table += "<td>" + value.common_name + "</td>";
//                 table += "</tr>";
//             });
//             table += "</table>";
//             $("#dataTable").html(table);}
//     });
// });








// $(document).ready(function(){
//     $.get("https://www.themealdb.com/api/json/v1/1/categories.php",
//     function(data){
//         $.each(data.categories, function(i,item){
//             $("#categorias").append(
//                 "<tr>"+
//                 "<td>"+item.idCategory+"</td>"+
//                 "<td>"+item.strCategory+"</td>"+
//                 "<td><img src='"+item.strCategoryThumb+"'></img></td>"+
//                 "<td>"+item.strCategoryDescription+"</td>"+
//                 "</tr>"
//             );
//         });
//     });
// });





// $("#boton").click(function(){
//     $.get("https://www.themealdb.com/api/json/v1/1/categories.php",
//     function(data){
//         $.each(data.categories, function(i,item){
//             $("#categorias").append(
//                 "<tr>"+
//                 "<td>"+item.idCategory+"</td>"+
//                 "<td>"+item.strCategory+"</td>"+
//                 "<td><img src='"+item.strCategoryThumb+"'></img></td>"+
//                 "<td>"+item.strCategoryDescription+"</td>"+
//                 "</tr>"
//             );
//         });
//     });
// });



// $("#boton1").click(function(){
//     $.get("https://www.themealdb.com/api/json/v1/1/categories.php",
//     function(data){
//         $.each(data.categories, function(i,item){
//             $("#categorias").append(
//                 "<tr>"+
//                 "<td>"+item.idCategory+"</td>"+
//                 "<td>"+item.strCategory+"</td>"+
//                 "<td><img src='"+item.strCategoryThumb+"'></img></td>"+
//                 "<td>"+item.strCategoryDescription+"</td>"+
//                 "</tr>"
//             );
//         });
//     });
// });





// $("#boton3").click(function(){
//     $.get("https://www.themealdb.com/api/json/v1/1/categories.php",
//     function(data){
//         $.each(data.categories, function(i,item){
//             $("#categorias").append(
//                 "<tr>"+
//                 "<td>"+item.idCategory+"</td>"+
//                 "<td>"+item.strCategory+"</td>"+
//                 "<td><img src='"+item.strCategoryThumb+"'></img></td>"+
//                 "<td>"+item.strCategoryDescription+"</td>"+
//                 "</tr>"
//             );
//         });
//     });
// });



// fetch('http://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8')
// .then((response) => {
//   return response.json(); // or .text() or .blob() ...
// });




// $(document).ready(function() {
//     // Create a new DataTable object
//     table = $('#example').DataTable({
//          "lengthMenu": [ [15, 50, 100, -1], [15, 50, 100, "All"] ],
//          "pagingType": "simple",
//          scrollY: 400,
//          scrollCollapse: true,
//          order: [[ 0, 'asc' ], [3, 'desc' ]],
//          ajax: {
//            url: 'https://jsonplaceholder.typicode.com/todos',
//            dataSrc: ''
//          },
//          columns: [
//             { data: 'userId' },
//             { data: 'id' },
//             { data: 'title' },
//             { data: 'completed' }
//            ]
//          })
//   });


























// $("#boton").click(function(){
//     $.get("http://api.tropicalfruitandveg.com/tfvjsonapi.php?tfvitem=Mango",
//     function(data){
//         $.each(data.results, function(i,item){
//             $("#categorias").append(
//                 "<tr>"+
//                 "<td>"+item.tfvname+"</td>"+
//                 "<td>"+item.botname+"</td>"+
//                 "<td><img src='"+item.imageurl+"'></img></td>"+
//                 "<td>"+item.description+"</td>"+
//                 "</tr>"
//             );
//         });
//     });
// });


// {"categories":[{"idCategory":"1","strCategory":"Beef","strCategoryThumb":"https:\/\/www.themealdb.com\/images\/category\/beef.png","strCategoryDescription":"Beef is the culinary name for meat from cattle, particularly skeletal muscle. Humans have been eating beef since prehistoric times.[1] Beef is a source of high-quality protein and essential nutrients.[2]"},

// {"_index":"seeds_production_20200824003934791","_type":"_doc","_id":"798","_score":21.214535,"slug":"lejun-sunflower-7c2b9297-c164-4b16-b40a-837d6a368a73","finished":false,"gmo":"unknown","active":true,"heirloom":"hybrid","location":"67000 Strasbourg, France","organic":"non-certified organic","quantity":50,"plant_before":null,"tradable_to":"locally","tradable":true,"crop_id":205,"crop_name":"sunflower","crop_slug":"sunflower","owner_id":8230,"owner_location":"67000 Strasbourg, France","owner_login_name":"lejun","owner_slug":"lejun","parent_planting":null,"photos_count":0,"has_photos":false,"thumbnail_url":"https://s3.amazonaws.com/openfarm-project/production/media/pictures/attachments/5935cc53113c950004000237.jpg?1496697934","created_at":1634390299,"id":"798"},











// $("#boton2").click(function(){
//     $.get("https://www.themealdb.com/api/json/v1/1/categories.php",
//     function(data){
//         $.each(data.categories, function(i,item){
        
//             if(i == 0){
//                 $("#carro").append(
//                     "<div class='carousel-item active'>"+
//                         "<img src='"+item.strCategoryThumb+"'' class='d-block w-100' alt='...'>"+
//                     "</div>"
//                 );   
//             }else{
//                 $("#carro").append(
//                     "<div class='carousel-item'>"+
//                         "<img src='"+item.strCategoryThumb+"'' class='d-block w-100' alt='...'>"+
//                     "</div>"
//                 );
//             }
//         });
//     });
// });





// var largo = document.getElementById("nombre").value.length;
// // cuenta la cantidad de caracteres del imput ingresado

// if (largo+1>10 || largo+1 <3){  
// // <!-- Funcion que valida si son incorrectos la cantidad de caracteres ingresados -->
//     //   <!-- Se aplican los siguientes eventos si se cumple dicha condicion: -->
//   document.getElementById("nombre").innerHTML = "error, largo no valido";
//   document.getElementById("nombre").style.color = "blue";
//   document.getElementById("nombre").style.fontsize = "16px";
//   document.getElementById("nombre").disabled = "false";
// }
