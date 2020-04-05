<?php

if (isset($_POST['submit']))
{
	$name = $_POST['name'];
	$emailFrom = $_POST['email'];
	$message = $_POST['message'];
	$help = $_POST['help'];
	$emailTo = "pashagriv77@outlook.com";
	$subject = "Website Contact Form";
	$txt = "From(via website): ".$emailFrom."\n Name: ".$name."\n".$message;
	
	
	if(strcmp("pass",$help)==0)
	{
		if (! @mail($emailTo, $subject, $txt))	
		{
			$output = "The message has been sent.";
		}else{
			$output = "failed";
		}
	}
}

?>
