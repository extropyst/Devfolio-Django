✅

# requisitos:
agregar productos que se vean en el inicio


# django:
autenticacion login
conexion bbdd

objetivos 
conclusion



genera una version de este codigo javascript:

 $(document).ready(function(){
    $.get("https://www.themealdb.com/api/json/v1/1/categories.php",
    function(data){
        $.each(data.categories, function(i,item){
            $("#categorias").append(
                "<tr>"+
                "<td>"+item.idCategory+"</td>"+
                "<td>"+item.strCategory+"</td>"+
                "<td><img src='"+item.strCategoryThumb+"'></img></td>"+
                "<td>"+item.strCategoryDescription+"</td>"+
                "</tr>"
            );
        });
    });
});

que utilice fetch y que funcione para la siguiente api rest: https://trefle.io/api/v1/plants?token=-4GeatwCRGmaD5d8CfvrnxoiMd_aObLSJsMFxxFKAu8



class Meta:
model = Vehiculo
fields =['patente', 'marca', 'modelo', 'categoria']


