
function cleanMicroDistrictList(microDistrictSelect, isDistrictsExist) {

    microDistrictSelect.empty();
    if (isDistrictsExist == true) {
        microDistrictSelect.append('<option value="{{ micro_district_default_choice.0.0 }}" selected>{{ micro_district_default_choice.0.1 }}</option>');
    } else {
        {#microDistrictSelect.prop('disabled', true);#}
        microDistrictSelect.append('<option value="{{ micro_district_does_not_exist_choice.0.0 }}" selected>{{ micro_district_does_not_exist_choice.0.1 }}</option>');
    }

}

function MicroDistrictHandler() {
    var districtSelect = document.getElementById("district");
    var selectedValue = districtSelect.value;

    var microDistrictSelect = $('#micro_district');
    if (selectedValue == '{{ saltovka_dbvalue }}') {
        cleanMicroDistrictList(microDistrictSelect, true);
        {% for choice in micro_district_saltovka_choices %}
            microDistrictSelect.append('<option value="{{ choice.0 }}">{{ choice.1 }}</option>');
        {% endfor %}
        {#microDistrictSelect.prop('disabled', false);#}
    } else if (selectedValue == '{{ severnaya_saltovka_dbvalue }}') {
        cleanMicroDistrictList(microDistrictSelect, true);
        {% for choice in micro_district_severnaya_saltovka_choices %}
            microDistrictSelect.append('<option value="{{ choice.0 }}">{{ choice.1 }}</option>');
        {% endfor %}
        {#microDistrictSelect.prop('disabled', false);#}
    } else {
        cleanMicroDistrictList(microDistrictSelect, false);
    }
}

$("#district").change(function () {
    MicroDistrictHandler();
});
$(document).ready(function () {
    MicroDistrictHandler();
});
