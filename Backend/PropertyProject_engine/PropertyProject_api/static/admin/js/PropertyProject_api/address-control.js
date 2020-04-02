$(document).ready(function () {


  function clear_message(id){
    if($(`#${id}`).length){
      $(`#${id}`).remove();
    }
  }

  function fill_administrative_district(administrative_district_id){
    administrative_district_field =  $("#id_administrative_district");
    administrative_district_field.val(administrative_district_id);
    administrative_district_field.after('<p id="administrative_district_message">Заполнено автоматически</p>');
  }

  function fill_lat_and_lng(lat,lng){
    lat_field = $("#id_lat");
    lng_field = $('#id_lng');
    lat_field.val(lat);
    lng_field.val(lng)
    lat_field.after('<p id="lat_message">Заполнено автоматически</p>');
    lng_field.after('<p id="lng_message">Заполнено автоматически</p>');
  }

  function check_house_number(){
    var street = $("#id_street option:selected").text().split(' - ')[0].trim();
    var house_number = $("#id_house_number").val();
    var house_letter_field = $("#id_house_letter");

    clear_message('house_number_message');

    $.ajax({
      type: 'GET',
      async: true,
      url: '/api/check-address/',
      data: `type=house_number&street=${street}&house_number=${house_number};`,
      success: function(data) {
          var letter_choices = data['choices'];
          letter_choices.forEach(function(item) {
            house_letter_field.append(`<option value="${item[0]}">${item[1]}</option>`);
        });

        house_letter_field.find(`option:contains('${selected_house_letter}')`).attr("selected", "selected");

        $("#id_house_number").after(`<p id="house_number_message">${data['success_message']}</p>`);
        check_house_letter();
      },
      error: function(data, status) {
      $("#id_house_number").after(`<p id="house_number_message">${data.responseJSON.error}</p>`);
      var letter_choices = data.responseJSON.choices;

      // alert('lol');
      letter_choices.forEach(function(item) {
        house_letter_field.append(`<option value="${item[0]}">${item[1]}</option>`);
    });
     },
      dataType: 'json',
    });
  }


  function check_house_letter(){
    var street = $("#id_street option:selected").text().split(' - ')[0].trim();
    var house_number = $("#id_house_number").val();
    var house_letter = $("#id_house_letter").val();
    var house_letter_field = $("#id_house_letter");
    var district;

    clear_message('house_letter_message');

    $.ajax({
      type: 'GET',
      async: true,
      url: '/api/check-address/',
      data: `type=house_letter&street=${street}&house_number=${house_number}&house_letter=${house_letter};`,
      success: function(data) {
        var administrative_district_id = data['administrative_district_id'];
        var lat = data['lat'];
        var lng = data['lng'];
        $("#id_house_letter").after(`<p id="house_letter_message">${data['success_message']}</p>`);
        fill_administrative_district(administrative_district_id);
        fill_lat_and_lng(lat,lng);
      },
      error: function(data, status) {
      $("#id_house_letter").after(`<p id="house_letter_message">${data.responseJSON.error}</p>`);
     },
      dataType: 'json',
    });
  }

  $( "#id_street" ).change(function() {
      if($("#id_street").val() != ''){
        is_street_field_filled = true;
      }
      else{
       is_street_field_filled = false;
      }
      if(is_house_numb_field_filled){
        $( "#id_house_number" ).val('');
        $( "#id_house_number"  ).trigger( "change" );
      }
  });

  $( "#id_house_number" ).change(function() {

        $('#id_house_letter').empty();
        // $('#id_administrative_district').val(0);

        $('#id_lat').val('');
        $('#id_lng').val('');
        clear_message('house_number_message');
        clear_message('house_letter_message');
        clear_message('administrative_district_message');
        clear_message('lat_message');
        clear_message('lng_message');


     if($("#id_house_number").val() != ''){
        is_house_numb_field_filled = true;
        check_house_number();
      }
     else{
       is_house_numb_field_filled = false;
        }
  });


  $( "#id_house_letter" ).change(function() {
        is_house_letter_field_filled = true;
        clear_message('administrative_district_message');
        clear_message('lat_field');
        clear_message('lng_field');
        $('#id_administrative_district').val(0);
        $('#id_lat').val('');
        $('#id_lng').val('');
        if(is_street_field_filled && is_house_numb_field_filled){
          check_house_letter();
        }
  });


  is_street_field_filled = false;
  is_house_numb_field_filled = false;
  is_house_letter_field_filled = false;

  selected_house_letter = $("#id_house_letter option:selected").text();
  selected_administrative_district = $("#id_administrative_district option:selected").text();
  current_lat = $('#id_lat').val();
  current_lng = $('#id_lng').val();
  $( "#id_street" ).trigger('change');
  $('#id_house_number').trigger('change');
  if(!is_street_field_filled && !is_house_numb_field_filled){
    $('#id_house_letter').empty();
  }
  $('#id_administrative_district').find(`option:contains('${selected_administrative_district}')`).attr("selected", "selected");
  $('#id_lat').val(current_lat);
  $('#id_lng').val(current_lng);
});
