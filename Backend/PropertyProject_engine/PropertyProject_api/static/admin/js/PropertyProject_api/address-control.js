$(document).ready(function () {


  function clear_message(id){
    if($(`#${id}`).length){
      $(`#${id}`).remove();
    }
  }


  function fill_administrative_district(administrative_district_id){
    // alert('fill admin district ');
    // clear_message('administrative_district_message');
    administrative_district_field =  $("#id_administrative_district");
    // $("#id_street option:selected").text().split(' - ')[1].trim();
    administrative_district_field.val(administrative_district_id);
    // create_message('id_administrative_district', 'administrative_district_message', 'Заполнено автоматически');
    administrative_district_field.after('<p id="administrative_district_message">Заполнено автоматически</p>');
  }

  function fill_lat_and_lng(lat,lng){
    // alert(`${lat} ${lng}`);
    lat_field = $("#id_lat");
    lng_field = $('#id_lng');
    lat_field.val(lat);
    lng_field.val(lng)
    lat_field.after('<p id="lat_message">Заполнено автоматически</p>');
    lng_field.after('<p id="lng_message">Заполнено автоматически</p>');
  }
  // function create_message(field_id, div_id, message){
  //   $(`#${field_id}`).after(`
  //   <div class="alert alert-success" role="alert" id=${div_id}>
  //     ${message}
  //   </div>
  //   `
  //   );

  // }

  function check_house_number(){
    alert('Check house number');
    var street = $("#id_street option:selected").text().split(' - ')[0].trim();
    var house_number = $("#id_house_number").val();
    // var house_letter = $("#id_house_letter").val();
    var house_letter_field = $("#id_house_letter");
    // var district;
    // var houses_list;

    clear_message('house_number_message');


    // console.log(street + " " + house_number);
    $.ajax({
      type: 'GET',
      async: true,
      url: '/api/check-address/',
      data: `type=house_number&street=${street}&house_number=${house_number};`,
      success: function(data) {
          var letter_choices = data['choices'];
          // console.log(houses_list);
        //   house_letter_field.append(`<option value="${data['without_letter']}" selected>${data['without_letter_for_humans']}</option>`);
          letter_choices.forEach(function(item) {
            house_letter_field.append(`<option value="${item[0]}">${item[1]}</option>`);
        });
        // house_letter_field.val(selected_house_letter);
        house_letter_field.find(`option:contains('${selected_house_letter}')`).attr("selected", "selected");
        // house_letter_field.val(0);

        $("#id_house_number").after(`<p id="house_number_message">${data['success_message']}</p>`);
        check_house_letter();
        // house_letter_field.find(`option:contains('${selected_house_letter}')`).attr("selected", "selected");
      },
      error: function(data, status) {
      $("#id_house_number").after(`<p id="house_number_message">${data.responseJSON.error}</p>`);
      var letter_choices = data.responseJSON.choices;
      letter_choices.forEach(function(item) {
        house_letter_field.append(`<option value="${item[0]}">${item[1]}</option>`);
    });
     },
      dataType: 'json',
    });
  }


  function check_house_letter(){
    // alert('check house letter');
    var street = $("#id_street option:selected").text().split(' - ')[0].trim();
    var house_number = $("#id_house_number").val();
    var house_letter = $("#id_house_letter").val();
    var house_letter_field = $("#id_house_letter");
    var district;
    // var houses_list;

    clear_message('house_letter_message');
    // clear_message('administrative_district_message');

    // console.log(street + " " + house_number);
    $.ajax({
      type: 'GET',
      async: true,
      url: '/api/check-address/',
      data: `type=house_letter&street=${street}&house_number=${house_number}&house_letter=${house_letter};`,
      success: function(data) {
        var administrative_district_id = data['administrative_district_id'];
        var lat = data['lat'];
        var lng = data['lng'];
        // alert(administrative_district_id);
        // create_message('id_house_letter', 'house_letter_message', data['success_message']);
        $("#id_house_letter").after(`<p id="house_letter_message">${data['success_message']}</p>`);
        fill_administrative_district(administrative_district_id);
        fill_lat_and_lng(lat,lng);
          // console.log(houses_list);
          // house_letter_field.append(`<option value="${data['without_letter']}" selected>${data['without_letter_for_humans']}</option>`);
        //   houses_list.forEach(function(item) {
        //     house_letter_field.append(`<option value="${item}">${item}</option>`);
        // });
        // house_letter_field.find(`option:contains('${selected_house_letter}')`).attr("selected", "selected");

      },
      error: function(data, status) {
      // $("#id_house_number").val('');
      // is_house_numb_field_filled = false;
      $("#id_house_letter").after(`<p id="house_letter_message">${data.responseJSON.error}</p>`);
     },
      dataType: 'json',
    });
  }

  $( "#id_street" ).change(function() {
     if($("#id_street").val() != ''){
        is_street_field_filled = true;
        // alert('street changed');
        if(is_house_numb_field_filled){
          $( "#id_house_number" ).val('');
          // $( "#id_house_letter" ).val('');
          $( "#id_house_number"  ).trigger( "change" );
          // $( "#id_house_letter"  ).trigger( "change" );
        }
     }
     else{
       if(is_house_numb_field_filled){
         $( "#id_house_number" ).val('');
         // $( "#id_house_letter" ).val('');
         $( "#id_house_number"  ).trigger( "change" );
         // $( "#id_house_letter"  ).trigger( "change" );
       }
       is_street_field_filled = false;
       // alert('street changed to default');
     }
  });

  $( "#id_house_number" ).change(function() {
     if($("#id_house_number").val() != ''){
        is_house_numb_field_filled = true;
        $('#id_house_letter').empty();
        $('#id_administrative_district').val(0);
        $('#id_lat').val(0);
        $('#id_lng').val(0);
        clear_message('house_number_message');
        clear_message('house_letter_message');
        clear_message('administrative_district_message');
        clear_message('lat_message');
        clear_message('lng_message');
        check_house_number();
        // if(is_house_letter_field_filled){
        //
        // }

         // alert('house number changed');

        // if(is_street_field_filled == true){
        //   // $('#id_house_letter').empty();
        //   if(is_house_letter_field_filled)
        //   fill_in_house_letter();
        // }
     }
     else{
       is_house_numb_field_filled = false;
       clear_message('house_number_message');
       clear_message('house_letter_message');
       clear_message('administrative_district_message');
       clear_message('lat_field');
       clear_message('lng_field');
       // $('#id_house_letter').empty();
       // if(is_street_field_filled == true){
       //   $('#id_house_letter').empty();
       // }
       // alert('house number changed to default');
     }
  });


  $( "#id_house_letter" ).change(function() {
        is_house_letter_field_filled = true;
        clear_message('administrative_district_message');
        clear_message('lat_field');
        clear_message('lng_field');
        $('#id_administrative_district').val(0);
        $('#id_lat').val(0);
        $('#id_lng').val(0);
        // alert('street changed');
        if(is_street_field_filled && is_house_numb_field_filled){
          check_house_letter();
        }

        // if(is_house_numb_field_filled == true){
        //   $( "#id_house_number" ).val('');
        //   $( "#id_house_number"  ).trigger( "change" );
        // }
  });


  is_street_field_filled = false;
  is_house_numb_field_filled = false;
  is_house_letter_field_filled = false;

  selected_house_letter = $("#id_house_letter option:selected").text();
  //
  $( "#id_street" ).trigger('change');
  $('#id_house_number').trigger('change');
  //
  if(!is_street_field_filled && !is_house_numb_field_filled){
    $('#id_house_letter').empty();
  }
});











  // $(document).ready(function () {
  //
  //   function fill_in_house_letter(){
  //
  //     var street = $("#id_street option:selected").text().split(' - ')[0].trim();
  //     var house_number = $("#id_house_number").val();
  //     var house_letter_field = $("#id_house_letter");
  //     var houses_list;
  //
  //     if($('#invalid_house_number_error').length){
  //       $('#invalid_house_number_error').remove();
  //     }
  //     // console.log(street + " " + house_number);
  //     $.ajax({
  //       type: 'GET',
  //       async: true,
  //       url: '/api/check-address/',
  //       data: `street=${street}&house_number=${house_number};`,
  //       success: function(data) {
  //           var houses_list = data['houses'];
  //           // console.log(houses_list);
  //           house_letter_field.append(`<option value="${data['without_letter']}" selected>${data['without_letter_for_humans']}</option>`);
  //           houses_list.forEach(function(item) {
  //             house_letter_field.append(`<option value="${item}">${item}</option>`);
  //         });
  //         house_letter_field.find(`option:contains('${selected_house_letter}')`).attr("selected", "selected");
  //       },
  //       error: function(data, status) {
  //       $("#id_house_number").val('');
  //       is_house_numb_field_filled = false;
  //       $("#id_house_number").after(`<p id="invalid_house_number_error">${data.responseJSON.error}</p>`);
  //      },
  //       dataType: 'json',
  //     });
  //   }
  //
  //   $( "#id_house_number" ).change(function() {
  //      if($("#id_house_number").val() != ''){
  //         is_house_numb_field_filled = true;
  //          // alert('house number changed');
  //
  //         if(is_street_field_filled == true){
  //           $('#id_house_letter').empty();
  //           fill_in_house_letter();
  //         }
  //      }
  //      else{
  //        is_house_numb_field_filled = false;
  //        if(is_street_field_filled == true){
  //          $('#id_house_letter').empty();
  //        }
  //        // alert('house number changed to default');
  //      }
  //   });
  //
  //   $( "#id_street" ).change(function() {
  //      if($("#id_street").val() != ''){
  //         is_street_field_filled = true;
  //         // alert('street changed');
  //         if(is_house_numb_field_filled == true){
  //           $( "#id_house_number" ).val('');
  //           $( "#id_house_number"  ).trigger( "change" );
  //         }
  //      }
  //      else{
  //        is_street_field_filled = false;
  //        // alert('street changed to default');
  //      }
  //   });
  //
  //
  //   is_street_field_filled = false;
  //   is_house_numb_field_filled = false;
  //   selected_house_letter = $("#id_house_letter option:selected").text();
  //
  //   $( "#id_street" ).trigger('change');
  //   $('#id_house_number').trigger('change');
  //
  //   if(!is_street_field_filled && !is_house_numb_field_filled){
  //     $('#id_house_letter').empty();
  //   }
  // });
