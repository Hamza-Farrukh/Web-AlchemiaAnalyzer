$(document).on('submit', '#statsForm', function(e){
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/',
        data: {
          atkmatk: $('#atkMatk').val(),
          skill: $("#skill").val(),
          ele_atk: $("#eleAtk").val(),
          enemy_def: $("#enemyDef").val(),
          cdmg: $("#cdmg").val(),
          df: $("#df").val(),
          crit: $('#crit').is(':checked'),
          eleWeak: $('#eleWeak').is(':checked'),
          atkUp: $('#atkUp').val(),
          hits: $('#hits').val(),
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
          if (response.success){
            $('#damage').text(response.message);
          }
          else{
              
          };
        },
        error: function(response){
          alert('Error on the server side');
        }
      });
});