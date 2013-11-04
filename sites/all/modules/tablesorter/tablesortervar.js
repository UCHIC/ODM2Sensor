/**
 * @file
 * jQuery Tablesorter
 */

(function ($) {
  Drupal.behaviors.tablesorter = {
    attach: function (context, settings) {
      $(".tablesorter").tablesorter();
    }
  };
})(jQuery);
