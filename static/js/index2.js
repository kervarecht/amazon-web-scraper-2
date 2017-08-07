$(document).ready(function() {
    var minPrice;
    var maxPrice;
    //initializing slider
    $("#slider-range" ).slider({
      range: true,
      min: 0,
      max: 40,
      values: [ 0, 40 ],
      slide: function( event, ui ) {
        $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        minPrice = ui.values[0];
        maxPrice = ui.values[1];
    }
    });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
      " - $" + $( "#slider-range" ).slider( "values", 1 ) );

      //table filter function based on slider
      $('.ui-slider-handle').on('click', function(event, ui){
          $('tbody tr td:nth-child(3)').each(function(){
             var price = $(this).html().replace('$', "");
             price = parseFloat(price);
             if (price <= maxPrice && price >= minPrice){
                 $(this).parent().css('display', 'display');
             }
             else {
                 $(this).parent().css('display', 'none');
             }
          });
      });


      //AJAX call in here
      $('#get-results').on('click', function() {
        $('body').addClass("loading");
        var dataToSend = $('#genre-select').val();
        $('#info').css('visibility', 'hidden');
        $('#info-body').empty();
        var sortable = true;
        $.ajax({
            url: './deals',
            dataType: 'json',
            data: dataToSend,
            success: function(data) {
                $('body').removeClass("loading");
                //process the AJAX call data into a tablesorter table
                for (var i = 0; i < data.length; i++) {
                    for (var j = 0; j < data[i].length; j++) {
                        var author = data[i][j].author;
                        var title = data[i][j].title;
                        var price = data[i][j].price;
                        var book_asin = data[i][j].asin;

                        var rowConstructor = "<tr><td>" + author + "</td><td>" + title + "</td><td>" + price + "</td><td>" + book_asin + "</td><td><a href='https://www.amazon.com/dp/" + book_asin + "/'>Link</a></td></tr>";
                        $('#info tbody').append(rowConstructor);

                    }

                }
                $('#info').css('visibility', 'visible');
                //need to trigger an update of tablesorter each time a new AJAX call is made
                $("#info").tablesorter();
                $('#info').tablesorter().trigger('update');

            }
        }
    );
});
});

/*
*/
