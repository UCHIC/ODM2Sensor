function deleteEntity(resource, id, callback) {
	if(!confirm('Do you really want to delete this item?')){
		return false;
	}

	if (typeof(callback) === 'undefined') {
		callback = function(){};
	}
	jQuery.ajax({
		url: Drupal.settings.basePath + "services/session/token",
		type: "get",
		dataType: "text",
		error: function (jqXHR, textStatus, errorThrown) {
		    alert(errorThrown);
		},
		success: function (token) {
			jQuery.ajax({
			    type: "DELETE",
			    dataType: "json",
			    url: Drupal.settings.basePath + "entities_service/" + resource + "/" + id,
			    beforeSend: function (request) {
			    	request.setRequestHeader("X-CSRF-Token", token);
			    },
			    complete: function(data) {
			    	callback(data);
			    },
			});
		}
	});
}