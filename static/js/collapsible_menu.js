var coll = document.getElementsByClassName("collapsible"); //Get all menu buttons
var i;

for (i = 0; i < coll.length; i++) //For each button
{
	coll[i].addEventListener("click", function() //If button gets clicked
	{
		this.classList.toggle("active");
		var content = this.nextElementSibling; //Get the following div
		if (content.style.maxHeight) //If expanded
		{
	  		content.style.maxHeight = null; //Set height to null
		} else
		{
	  		content.style.maxHeight = content.scrollHeight + "px"; //Set height equal to the height of the contents
		}
	});
}
