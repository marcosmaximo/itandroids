function change_value(element, new_value) {
	element.defaultValue = new_value;
	element.value = new_value;
}

function delete_hint(field) {
	if(field.defaultValue == field.value) {
		field.value = '';
		field.style.color = '#FFFFFF';
		field.style.fontStyle = 'normal';
	} else if(field.value == '') {
		field.value = field.defaultValue;
		field.style.color = '#BCBCBC';
		field.style.fontStyle = 'italic';
	}
}

function change_image(element, filename) {
	element.src='/media/images/'+filename;
}
