<?php

/** 
* Implementation of hook_views_data
*/




function  db_connect_views_data() {
   error_log("Loading views");
   $data = array();

   db_set_active("iutah_equipment");
   $tables = db_query("show tables");
   db_set_active();

  while($table = $tables->fetchObject()) {
    $tableName = $table->Tables_in_lbrequipmentdatabase;

    $data[$tableName]['table']['group'] = t($tableName);
    $data[$tableName]['table']['base'] = array(
       'field' => 'id',
       'title' => t($tableName),
       'help' => t('Autoincremented ID field, to enable views integration'),
       'database' => 'iutah_equipment',
       'weight' => -10,
    );

    db_set_active("iutah_equipment");
    $fields = db_query("show columns from $tableName");
    db_set_active();

    while ($field = $fields->fetchObject()) {
      $fieldName = $field->Field;
      $data[$tableName][$fieldName] = array(
       'title' => t($fieldName),
       'help' => t($fieldName),
       'field' => array(
          'handler' => 'views_handler_field',
          'click sortable' => TRUE,
       ),
       'sort' => array(
          'handler' => 'views_handler_sort',
       ),
       'filter' => array(
          'handler' => 'views_handler_filter_string',
       ),
       'argument' => array(
          'handler' => 'views_handler_argument_string',
       ),
      );
    }
  }
   return $data;
}

?>