extends Control

const SERVER_ADDRESS = "https://incompatiblesmoothbookmarks.kavirajarb1.repl.co/"
#"https://solar-output-predictor.onrender.com/"

var location := ""
var nums := 0.0

onready var form := $Form
onready var output := $Output
onready var request := $"%HTTPRequest"



func get_request(url: String, data: Dictionary, use_ssl:bool = false):
	request.cancel_request()
	var query := JSON.print(data)
	var headers := ["Content-Type: application/json"]
	return request.request(url, headers, use_ssl, HTTPClient.METHOD_GET, query)


func _on_Form_submit(pn, cn, sd, ed, no, pr):
	var url = SERVER_ADDRESS + "api/{}/{}/{}/{}/{}/{}".format(
		[pn, cn, sd, ed, no, pr], "{}"
	)
	location = pn
	nums = no
	get_request(url, {})


func _on_HTTPRequest_request_completed(result, response_code, headers, body):
	if result != OK:
		print("Something went wrong, please try again later")
		return -1
	if response_code != 200:
		print("Server Error. Bad request")
		return -2
	var json := JSON.parse(body.get_string_from_utf8())
	var response: Dictionary = json.result
	var lat = response.get("lat")
	var lon = response.get("lon")
	var out = response.get("output")
	var days = response.get("days")
	print("lat: ", lat)
	print("lon: ", lon)
	print("out: ", out)
	print("days: ", days)
	output_page(lat, lon, out, days)


func output_page(lat, lon, out, days):
	form.hide()
	output.show()
	output.init(location, lat, lon, days, out, nums)


func _on_Output_back():
	form.show()
	output.hide()
	form.reset()
