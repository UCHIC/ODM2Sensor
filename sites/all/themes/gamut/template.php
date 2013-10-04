<?php

global $user;
if ($user->uid == 0 && arg(0) != 'user'){
  drupal_goto('user/login');
}
