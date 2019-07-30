$(function () {
    
    $.ajax({
        url: $("#container").attr("data-url"),
        dataType: 'json',
        success: function (data) {
          Highcharts.chart("container", data);
        }
    });
    $.ajax({
        url: $("#container2").attr("data-url"),
        dataType: 'json',
        success: function (data) {
          Highcharts.chart("container2", data);
        }
    });
    
    
});