
$(document).ready(function () {

    fill_micro_district_choices();
    MicroDistrictHandler();

    function fill_micro_district_choices(){
      $.ajax({
        type: 'GET',
        async: false,
        url: '/get-micro-districts/',
        success: function(data) {
            // micro_district_choices = JSON.parse(data['micro_district_choices']);
            micro_district_choices = data['micro_district_choices'];
            db_values = data['db_values']
            // console.log(data);
        },
        error: function(data, status) {
        console.log(`Error: ${data.responseJSON}`)
       },
        dataType: 'json',
      });

    }
    //--------------------------------------------------------------------
    function cleanMicroDistrictList(microDistrictSelect, isDistrictsExist) {
           microDistrictSelect.empty();
           if (isDistrictsExist == true) {
               microDistrictSelect.append(`<option value="${micro_district_choices["default"][0][0]}" selected>${micro_district_choices["default"][0][1]}</option>`);
           } else {
               microDistrictSelect.append(`<option value="${micro_district_choices["default"][1][0]}" selected>${micro_district_choices["default"][1][1]}</option>`);
           }

       }
       function UpdateMicroDistrictValues(districtSelectedValue,microDistrictSelect,currentMicroDistrict=null){
         if (districtSelectedValue == db_values['saltovka_dbvalue']) {
             cleanMicroDistrictList(microDistrictSelect, true);
             micro_district_choices['saltovka'].forEach(function(entry) {
              if(currentMicroDistrict){
                if(currentMicroDistrict == entry[0]){
                  microDistrictSelect.append(`<option value="${entry[0]}" selected>${entry[1] }</option>`);
                  return;
                }
              }
              microDistrictSelect.append(`<option value="${entry[0]}">${entry[1] }</option>`);
          });

         } else if (districtSelectedValue == db_values['severnaya_saltovka_dbvalue']) {
             cleanMicroDistrictList(microDistrictSelect, true);
             micro_district_choices['severnaya_saltovka'].forEach(function(entry) {
               if(currentMicroDistrict){
                 if(currentMicroDistrict == entry[0]){
                   microDistrictSelect.append(`<option value="${entry[0]}" selected>${entry[1] }</option>`);
                   return;
                 }
               }
             microDistrictSelect.append(`<option value="${entry[0]}">${entry[1] }</option>`);
             });
         } else {
             cleanMicroDistrictList(microDistrictSelect, false);
         }
       }

     function MicroDistrictHandler() {
           var districtSelect = $('#id_district');
           var districtSelectedValue = districtSelect.val();
           var microDistrictSelect = $('#id_micro_district');
           currentMicroDistrict = microDistrictSelect.val();
           UpdateMicroDistrictValues(districtSelectedValue, microDistrictSelect,currentMicroDistrict);
       }

       $("#id_district").change(function () {
           MicroDistrictHandler();
       });
});
