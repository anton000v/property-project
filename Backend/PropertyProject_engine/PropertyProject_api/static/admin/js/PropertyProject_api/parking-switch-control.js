$(document).ready(function () {
    $('#id_parking li').find(`input[value=${parking_default_choice_value}]`).click(function () {
      if($(this).prop('checked'))
      {
         $('#id_parking li input').not(`input[value=${parking_default_choice_value}]`).each(function(i)
         {
            $(this).prop('checked',!'checked');
         });
      }
      else{
        $(this).prop('checked','checked');
      }
    });

    $('#id_parking li input').not(`input[value=${parking_default_choice_value}]`).click(function () {
      $('#id_parking li').find(`input[value=${parking_default_choice_value}]`).prop('checked' , !'checked');
    });
});
