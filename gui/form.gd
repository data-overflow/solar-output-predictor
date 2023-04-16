extends Panel

signal submit(pn, cn, sd, ed, no, pr)

var using_area := false

onready var place := $"%Place"
onready var country := $"%Country"
onready var start := $"%Start"
onready var end := $"%End"
onready var power := $"%Power"
onready var count := $"%Count"
onready var countEntry := $"%CountEntry"
onready var submitButton := $"%Submit"

func _on_CheckButton_toggled(button_pressed):
	if button_pressed:
		count.text = "Area (Metre squared) |"
		countEntry.placeholder_text = "4.2"
		using_area = true
	else:
		count.text = "Solar Panels Count   |"
		countEntry.placeholder_text = "10"
		using_area = false


func reverse(area):
	return ceil(float(area) / float(1.6764*1.016))


func _on_Button_button_down():
	submitButton.text = "Processing..."
	submitButton.disabled = true
	var place_name = place.text
	var country_name = country.text
	var start_date = start.text
	var end_date = end.text
	var num := 0.0
	if using_area:
		num = reverse(countEntry.text)
		print("Solar Panel Count: ", num)
	else:
		num = int(countEntry.text)
	var power_rating = int(power.text)
	emit_signal(
		"submit", place_name, country_name,
		start_date, end_date, num, power_rating
	)

func reset():
	submitButton.text = "Calculate!"
	submitButton.disabled = false
