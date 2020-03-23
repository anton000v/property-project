  $(document).ready(function () {

    function fill_in_house_letter(){

      var street = $("#id_street option:selected").text().split(' - ')[0].trim();
      var house_number = $("#id_house_number").val();
      var house_letter_field = $("#id_house_letter");
      var houses_list;

      if($('#invalid_house_number_error').length){
        $('#invalid_house_number_error').remove();
      }
      // console.log(street + " " + house_number);
      $.ajax({
        type: 'GET',
        async: true,
        url: '/api/check-address/',
        data: `street=${street}&house_number=${house_number};`,
        success: function(data) {
            var houses_list = data['houses'];
            // console.log(houses_list);
            house_letter_field.append(`<option value="${data['without_letter']}" selected>${data['without_letter_for_humans']}</option>`);
            houses_list.forEach(function(item) {
              house_letter_field.append(`<option value="${item}">${item}</option>`);
          });
          house_letter_field.find(`option:contains('${selected_house_letter}')`).attr("selected", "selected");
        },
        error: function(data, status) {
        $("#id_house_number").val('');
        is_house_numb_field_filled = false;
        $("#id_house_number").after(`<p id="invalid_house_number_error">${data.responseJSON.error}</p>`);
       },
        dataType: 'json',
      });
    }

    $( "#id_house_number" ).change(function() {
       if($("#id_house_number").val() != ''){
          is_house_numb_field_filled = true;
           // alert('house number changed');

          if(is_street_field_filled == true){
            $('#id_house_letter').empty();
            fill_in_house_letter();
          }
       }
       else{
         is_house_numb_field_filled = false;
         if(is_street_field_filled == true){
           $('#id_house_letter').empty();
         }
         // alert('house number changed to default');
       }
    });

    $( "#id_street" ).change(function() {
       if($("#id_street").val() != ''){
          is_street_field_filled = true;
          // alert('street changed');
          if(is_house_numb_field_filled == true){
            $( "#id_house_number" ).val('');
            $( "#id_house_number"  ).trigger( "change" );
          }
       }
       else{
         is_street_field_filled = false;
         // alert('street changed to default');
       }
    });


    is_street_field_filled = false;
    is_house_numb_field_filled = false;
    selected_house_letter = $("#id_house_letter option:selected").text();

    $( "#id_street" ).trigger('change');
    $('#id_house_number').trigger('change');

    if(!is_street_field_filled && !is_house_numb_field_filled){
      $('#id_house_letter').empty();
    }
  });
