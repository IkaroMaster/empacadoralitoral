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
  if($('#container')){
    $.ajax({
      type: 'GET',
      url: $("#container").attr("data-url"),
      data:{
        mes:$("#container").attr("data-mes"),
        anio:$("#container").attr("data-anio"),
      },
      dataType: 'json',
      success: function (data) {
        Highcharts.chart("container", data);
      }
    });
  }

  

});