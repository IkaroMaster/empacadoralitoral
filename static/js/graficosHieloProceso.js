$(function () {

  // Highcharts.chart('container', {
  //     chart: {
  //         type: 'column'
  //     },
  //     title: {
  //         text: 'Historic World Population by Region'
  //     },
  //     xAxis: {
  //         categories: ['Africa', 'America', 'Asia', 'Europe', 'Oceania']
  //     },
  //     series: [{
  //         name: 'Year 1800',
  //         data: [107, 31, 635, 203, 2]
  //     }, {
  //         name: 'Year 1900',
  //         data: [133, 156, 947, 408, 6]
  //     }, {
  //         name: 'Year 2012',
  //         data: [1052, 954, 4250, 740, 38]
  //     }]
  // });
  if ($("#container").length) {
    $.ajax({
      url: $("#container").attr("data-url"),
      dataType: 'json',
      success: function (data) {
        Highcharts.chart("container", data);
      }
    });
  }else if($('#container2')){
    $.ajax({
      type: 'GET',
      url: $("#container2").attr("data-url"),
      data:{
        mes:$("#container2").attr("data-mes"),
        anio:$("#container2").attr("data-anio"),
      },
      dataType: 'json',
      success: function (data) {
        Highcharts.chart("container2", data);
      }
    });
  }

  

});