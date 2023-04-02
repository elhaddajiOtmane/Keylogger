def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox5545e6d6ec844200b01ee5ea1d3e89a1.mailgun.org/messages",
		auth=("api", "a54544242e818cee784dcb3774af464b-d51642fa-036c8776"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox5545e6d6ec844200b01ee5ea1d3e89a1.mailgun.org>",
			"to": "otmane elhaddaji <otmanhaddaji17@gmail.com>",
			"subject": "Hello otmane elhaddaji",
			"text": "Congratulations otmane elhaddaji, you just sent an email with Mailgun!  You are truly awesome!"})
send_simple_message()