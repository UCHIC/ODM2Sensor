<?php
if (!$logged_in) {
    drupal_goto("user/login");
}

require(path_to_theme() . '/page.tpl.php');

?>