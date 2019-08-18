// 
// How to use:
//
// $('#price,#sum').cleave({ numeral: true, numeralThousandsGroupStyle: 'thousand', autoUnmask: true});
//
// or use pre-defined sets:
//
// $('#price').cleave('money');
// $('#date_at').cleave('date');
// $('#qty').cleave('integer');
//
(function($, window, undefined){ 'use strict'

  $.fn.cleave = function(opts) {

    var defaults = {autoUnmask: false}, options = {};

    var defDate    = {date: true, datePattern: ['d','m','Y'], delimiter: '-'},
        defTime    = {numericOnly: true, delimiters: [':'], blocks: [2, 2]},
        defDateTime= {numericOnly: true, delimiters: ['-', '-', ' ', ':'], blocks: [2, 2, 4, 2, 2]},
        defMoney   = {numeral: true, numeralThousandsGroupStyle: 'thousand', numeralPositiveOnly: true, autoUnmask: true},
        defInteger = {numeral: true, numeralThousandsGroupStyle: 'thousand', numeralPositiveOnly: true, autoUnmask: true, numeralDecimalScale: 0};

    if( typeof opts === 'string') {
      switch( opts ) {
        case 'date':     $.extend(options, defaults, defDate);     break;
        case 'time':     $.extend(options, defaults, defTime);     break;
        case 'datetime': $.extend(options, defaults, defDateTime); break;
        case 'money':    $.extend(options, defaults, defMoney);    break;
        case 'integer':  $.extend(options, defaults, defInteger);  break;
      }
    } else if( $.isPlainObject( opts ) ) {
      $.extend(options, defaults, opts || {});
    }

    return this.each(function(){

      if( this.id == undefined || this.id == null || this.id == '' ) {
        throw 'jquery-cleave.js requires objectID to be initialized';
      }

      var cleave = new Cleave('#'+this.id, options), $this = $(this);

      $this.data('cleave-auto-unmask', options['autoUnmask']);;
      $this.data('cleave',cleave)
    });
  }

  var origGetHook, origSetHook;

  if ($.valHooks.input) {

    origGetHook = $.valHooks.input.get;
    origSetHook = $.valHooks.input.set;

  } else {

    $.valHooks.input = {};
  }

  $.valHooks.input.get = function (el) {

    var $el = $(el), cleave = $el.data('cleave');

    if( cleave ) {

      return $el.data('cleave-auto-unmask') ? cleave.getRawValue() : el.value;

    } else if( origGetHook ) {

      return origGetHook(el);

    } else {

      return undefined;
    }
  }

  $.valHooks.input.set = function (el,val) {

    var $el = $(el), cleave = $el.data('cleave');

    if( cleave ) {

      cleave.setRawValue(val);
      return $el;

    } else if( origSetHook ) {

      return origSetHook(el);

    } else {
      return undefined;
    }
  }
})(jQuery, window);
