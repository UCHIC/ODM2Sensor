<?php




/**
 * Callback for deleting a site.
 *
 * @param int $SiteID
 * @return object
 */
function _delete_site($SiteID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('sites')->condition('SiteID', $SiteID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
  	drupal_set_message("The site was successfully deleted.");
  } else {
  	drupal_set_message("The site is being used and could not be deleted.", "error");
  }
  return (object)array(
    'id' => $SiteID,
    'value' => $returnValue,
  );
}

/**
 * Callback for deleting a site visit.
 *
 * @param int $SiteVisitID
 * @return object
 */
function _delete_sitevisit($SiteVisitID) {
  db_set_active("iutah_equipment");
  
  $txn = db_transaction();
  try {
    db_delete('sitevisitpeople')->condition('SiteVisitID', $SiteVisitID)->execute();
    db_delete('sitevisitphotos')->condition('SiteVisitID', $SiteVisitID)->execute();
    $returnValue = db_delete('sitevisits')->condition('SiteVisitID', $SiteVisitID)->execute();
  } catch (Exception $e) {
    $txn->rollback();
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
    drupal_set_message("The site visit was successfully deleted.");
  } else {
    drupal_set_message("The site visit is being used and could not be deleted.", "error");
  }
  return (object)array(
    'id' => $SiteVisitID,
    'value' => $returnValue,
  );
}

/**
 * Callback for deleting a deployment.
 *
 * @param int $DeploymentID
 * @return object
 */
function _delete_deployment($DeploymentID) {
  db_set_active("iutah_equipment");
  
  $txn = db_transaction();
  try {
    $deployment = db_select('deployments', 'd')->fields('d', array('FieldActivityID'))->condition('DeploymentID', $DeploymentID)->execute()->fetchObject();
    db_delete('deploymentmeasuredvariables')->condition('DeploymentID', $DeploymentID)->execute();
    $returnValue = db_delete('deployments')->condition('DeploymentID', $DeploymentID)->execute();
    db_delete('fieldactivities')->condition('FieldActivityID', $deployment->FieldActivityID)->execute();
  } catch (Exception $e) {
    $txn->rollback();
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
    drupal_set_message("The deployment was successfully deleted.");
  } else {
    drupal_set_message("The deployment is being used and could not be deleted.", "error");
  }
  return (object)array(
    'id' => $DeploymentID,
    'value' => $returnValue,
  );
}

/**
 * Callback for deleting a calibration .
 *
 * @param int $CalibrationID
 * @return object
 */
function _delete_calibration($CalibrationID) {
  db_set_active("iutah_equipment");
  
  $txn = db_transaction();
  try {
    $calibration = db_select('calibrations', 'c')->fields('c', array('FieldActivityID'))->condition('CalibrationID', $CalibrationID)->execute()->fetchObject();
    $returnValue = db_delete('calibrations')->condition('CalibrationID', $CalibrationID)->execute();
    db_delete('fieldactivities')->condition('FieldActivityID', $calibration->FieldActivityID)->execute();
  } catch (Exception $e) {
    $txn->rollback();
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
    drupal_set_message("The calibration was successfully deleted.");
  } else {
    drupal_set_message("The calibration is being used and could not be deleted.", "error");
  }
  return (object)array(
    'id' => $CalibrationID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a field activity.
 *
 * @param int $FieldActivityID
 * @return object
 */
function _delete_fieldactivity($FieldActivityID) {
  db_set_active("iutah_equipment");
  
  $txn = db_transaction();
  try {
    $returnValue = db_delete('calibrations')->condition('FieldActivityID', $FieldActivityID)->execute();
    $returnValue = db_delete('deployments')->condition('FieldActivityID', $FieldActivityID)->execute();
    $returnValue = db_delete('fieldactivities')->condition('FieldActivityID', $FieldActivityID)->execute();
  } catch (Exception $e) {
    $txn->rollback();
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
    drupal_set_message("The field activity was successfully deleted.");
  } else {
    drupal_set_message("The field activity is being used and could not be deleted.", "error");
  }
  return (object)array(
    'id' => $FieldActivityID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting an equipment.
 *
 * @param int $EquipmentID
 * @return object
 */
function _delete_equipment($EquipmentID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('equipment')->condition('EquipmentID', $EquipmentID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
    drupal_set_message("The equipment was successfully deleted.");
  } else {
    drupal_set_message("The equipment is being used and could not be deleted.", "error");
  }
  return (object)array(
    'id' => $EquipmentID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a factory service event.
 *
 * @param int $FactoryServiceEventID
 * @return object
 */
function _delete_factoryserviceevent($FactoryServiceEventID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('factoryserviceevents')->condition('FactoryServiceEventID', $FactoryServiceEventID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
    drupal_set_message("The factory service event was successfully deleted.");
  } else {
    drupal_set_message("The factory service event is being used and could not be deleted.", "error");
  }
  return (object)array(
    'id' => $FactoryServiceEventID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a vendor.
 *
 * @param int $VendorID
 * @return object
 */
function _delete_vendor($VendorID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('vendors')->condition('VendorID', $VendorID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
    drupal_set_message("The vendor was successfully deleted.");
  } else {
    drupal_set_message("The vendor is being used and could not be deleted.", "error");
  }
  return (object)array(
    'id' => $VendorID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a vendortype.
 *
 * @param int $VendorTypeID
 * @return object
 */
function _delete_vendortype($VendorTypeID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('vendortypecv')->condition('Term', $VendorTypeID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  return (object)array(
    'id' => $VendorTypeID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a site group.
 *
 * @param int $SiteGroupID
 * @return object
 */
function _delete_sitegroup($SiteGroupID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('sitegroups')->condition('SiteGroupID', $SiteGroupID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  return (object)array(
    'id' => $SiteGroupID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a site type.
 *
 * @param int $SiteTypeID
 * @return object
 */
function _delete_sitetype($SiteTypeID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('sitetypecv')->condition('Term', $SiteTypeID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  return (object)array(
    'id' => $SiteTypeID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a person.
 *
 * @param int $PersonID
 * @return object
 */
function _delete_people($PersonID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('people')->condition('PersonID', $PersonID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  return (object)array(
    'id' => $PersonID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a deployment type.
 *
 * @param int $DeploymentTypeID
 * @return object
 */
function _delete_deploymenttypes($DeploymentTypeID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('deploymenttypecv')->condition('Term', $DeploymentTypeID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  return (object)array(
    'id' => $DeploymentTypeID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a calibration method.
 *
 * @param int $CalibrationMethodID
 * @return object
 */
function _delete_calibrationmethod($CalibrationMethodID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('calibrationmethods')->condition('CalibrationMethodID', $CalibrationMethodID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  return (object)array(
    'id' => $CalibrationMethodID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a calibration standard.
 *
 * @param int $CalibrationStandardID
 * @return object
 */
function _delete_calibrationstandard($CalibrationStandardID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('calibrationstandards')->condition('CalibrationStandardID', $CalibrationStandardID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  return (object)array(
    'id' => $CalibrationStandardID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a calibration standard type.
 *
 * @param int $CalibrationStandardTypeID
 * @return object
 */
function _delete_calibrationstandardtype($CalibrationStandardTypeID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('calibrationstandardtypecv')->condition('Term', $CalibrationStandardTypeID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  return (object)array(
    'id' => $CalibrationStandardTypeID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a field activity type.
 *
 * @param int $FieldActivityTypeID
 * @return object
 */
function _delete_fieldactivitytype($FieldActivityTypeID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('activitytypecv')->condition('Term', $FieldActivityTypeID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  return (object)array(
    'id' => $FieldActivityTypeID,
    'value' => $returnValue,
  );
}

/**
 * Callback for deleting a deployment measured variables.
 *
 * @param int $DeploymentMeasuredVariables
 * @return object
 */
function _delete_deploymentmeasuredvariable($DeploymentMeasuredVariableID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('deploymentmeasuredvariables')->condition('DeploymentMeasuredVariableID', $DeploymentMeasuredVariableID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
    drupal_set_message("The deployment measured variable was successfully deleted.");
  } else {
    drupal_set_message("The deployment measured variable is being used and could not be deleted.", "error");
  }

  return (object)array(
    'id' => $DeploymentMeasuredVariableID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting an equipment type.
 *
 * @param int $EquipmentTypeID
 * @return object
 */
function _delete_equipmenttypes($EquipmentTypeID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('equipmenttypecv')->condition('Term', $EquipmentTypeID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  return (object)array(
    'id' => $EquipmentTypeID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting an equipment model.
 *
 * @param int $ModelID
 * @return object
 */
function _delete_equipmentmodel($ModelID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('equipmentmodels')->condition('ModelID', $ModelID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
    drupal_set_message("The equipment model was successfully deleted.");
  } else {
    drupal_set_message("The equipment model is being used and could not be deleted.", "error");
  }
  return (object)array(
    'id' => $ModelID,
    'value' => $returnValue,
  );
}

/**
 * Callback for deleting an sensor output variable.
 *
 * @param int $VariableID
 * @return object
 */
function _delete_sensoroutputvariables($VariableID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_delete('sensoroutputvariables')->condition('SensorOutputVariableID', $VariableID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  if ($returnValue == 1) {
    drupal_set_message("The sensor output variable was successfully deleted.");
  } else {
    drupal_set_message("The sensor output variable is being used and could not be deleted.", "error");
  }
  return (object)array(
    'id' => $VariableID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a vertical datum from drupal's database.
 *
 * @param int $DatumID
 * @return object
 */
function _delete_verticaldatum($DatumID) {
  try {
    $returnValue = db_delete('taxonomy_term_data')->condition('name', $DatumID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  return (object)array(
    'id' => $DatumID,
    'value' => $returnValue,
  );
}

/**
 * Callback for retrieving all site visit images.
 *
 * @param int $SiteVisitID
 * @return object
 */
function _get_site_visit_images($SiteVisitID) {
  db_set_active("iutah_equipment");
  
  try {
    $returnValue = db_select('sitevisitphotos', 't')->fields('t')->condition('SiteVisitID', $SiteVisitID)->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  $returnValue = ($returnValue === 0)? 0: $returnValue->fetchAll();

  return (object)array(
    'id' => $SiteVisitID,
    'value' => $returnValue,
  );

}

/**
 * Callback for deleting a site.
 *
 * @param int $SiteVisitID
 * @return object
 */
function _get_next_site_visit($SiteVisitID) {
  db_set_active("iutah_equipment");
  
  try {
    $date = db_select('sitevisits', 'sv')->fields('sv', array('SiteVisitBeginDateTime'))->condition('SiteVisitID', $SiteVisitID)->execute()->fetchObject()->SiteVisitBeginDateTime;
    $returnValue = db_select('sitevisits', 'sv')->fields('sv', array('SiteVisitID'))->condition('SiteVisitBeginDateTime', $date, ">")->orderBy('SiteVisitBeginDateTime', 'ASC')->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  $returnValue = ($returnValue === 0)? 0: $returnValue->fetchObject();

  return (object)array(
    'id' => $SiteVisitID,
    'value' => $returnValue,
  );
}


/**
 * Callback for deleting a site.
 *
 * @param int $SiteVisitID
 * @return object
 */
function _get_previous_site_visit($SiteVisitID) {
  db_set_active("iutah_equipment");
  
  try {
    $date = db_select('sitevisits', 'sv')->fields('sv', array('SiteVisitBeginDateTime'))->condition('SiteVisitID', $SiteVisitID)->execute()->fetchObject()->SiteVisitBeginDateTime;
    $returnValue = db_select('sitevisits', 'sv')->fields('sv', array('SiteVisitID'))->condition('SiteVisitBeginDateTime', $date, "<")->orderBy('SiteVisitBeginDateTime', 'DESC')->execute();
  } catch (Exception $e) {
    $returnValue = 0;
  }

  db_set_active();

  $returnValue = ($returnValue === 0)? 0: $returnValue->fetchObject();

  return (object)array(
    'id' => $SiteVisitID,
    'value' => $returnValue,
  );
}