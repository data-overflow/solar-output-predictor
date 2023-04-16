extends Panel

signal back

var final_out := 0.0
var out := 0.0

onready var info := $"%Info"
onready var output := $"%Output"

func _ready():
	set_process(false)

func init(loc, lat, lon, dur, out, nums):
	info.text = """
Location: {}
Latitude: {}
Longitude: {}
Duration: {} days
Number of Panels: {}
""".format([loc, lat, lon, dur, nums], "{}")
	final_out = float(out)
	set_process(true)

func _process(delta):
	if final_out > 0.0:
		output.text = str(out) + " KWh"
		if out < final_out:
			out += 5.75
		else:
			out = final_out
			output.text = str(final_out) + " KWh"
			set_process(false)


func _on_Button_pressed():
	emit_signal("back")
