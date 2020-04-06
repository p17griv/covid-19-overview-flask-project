function myFunction() {
  var name,email,message,txt,bool_name,bool_email,bool_message;
  var re = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
  
  // Get the value of the input field with id
  name = document.getElementById("name").value;
  email = document.getElementById("email").value;
  message = document.getElementById("message").value;

  if(!isNaN(name))
  {
	if(name.length > 0)
		document.getElementById("name_err_alert").innerHTML = "Λανθασμένο ονοματεπώνυμο";
	bool_name = false;
  }
  else
  {
	document.getElementById("name_err_alert").innerHTML = "";
	if(name.length > 4)
		bool_name = true;
  }
  if (!re.test(email))
  {
	if(email.length > 0)
		document.getElementById("email_err_alert").innerHTML = "Μη έγκυρη διεύθυνση email";
	bool_email = false;
  }
  else
  {
	document.getElementById("email_err_alert").innerHTML = "";
	bool_email = true;
  }
  
  if (bool_email && bool_name)
  {
	document.getElementById("help_input").value="pass"
  }
  
  if (message.length > 9)
  {
	bool_message = true;
  }
  else
  {
	bool_message = false;
  }
  if (bool_email && bool_name && bool_message)
  {
	document.getElementById("success_alert").innerHTML = "Το μήνυμα στάλθηκε επιτυχώς! Θα επικοινωνήσουμε σύντομα μαζί σας!";
	document.getElementById("form_button").style.visibility = "hidden";
  }
}