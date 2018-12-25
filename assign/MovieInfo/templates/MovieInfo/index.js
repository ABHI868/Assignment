
$(document).ready(function(){
    $.ajax({method:"get", url:'',dataType='json'}).done(function(data){
        $.map(data, function(book,index){
            $('#result').append('<p>'+book.book_name+'</p>')
        })
    });


});