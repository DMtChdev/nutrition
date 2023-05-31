$(document).ready(function () {
    $("tr").click(function () {
      // Desmarcar todas las filas excepto la seleccionada
      $("tr").not(this).removeClass("selected");
  
      // Alternar la clase "selected" en la fila seleccionada
      $(this).toggleClass("selected");
    });
  
    $("#agregarBtn").click(function () {
      var selectedRow = $("tr.selected");
      if (selectedRow.length > 0) {
        var rowData = [];
        selectedRow.find("td").each(function () {
          rowData.push($(this).text());
        });
  
        // Realizar una solicitud al servidor para enviar los datos seleccionados
        $.ajax({
          url: '/agregar_desayuno',
          method: 'POST',
          data: JSON.stringify({ 'rowData': rowData }),
          contentType: 'application/json',
          success: function (response) {
            console.log(response);
            window.location.href = "/";
          }
        });
      }
    });
  });
  