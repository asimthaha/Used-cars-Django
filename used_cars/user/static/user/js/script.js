$('form').submit(function(){
     var pass1 = $('#pass1').val();
     var pass2 = $('#pass2').val();

     if (pass1 != pass2){
         alert('Enter password same as the above password');
         return False;
     }

})

 $(document).ready(function(){
      var date_input=$('input[name="date"]'); //our date input has the name "date"
      var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
      var options={
        format: 'mm/dd/yyyy',
        container: container,
        todayHighlight: true,
        autoclose: true,
      };
      date_input.datepicker(options);
    })


function allowOnlyLetters(e, t)
{
   if (window.event)
   {
      var charCode = window.event.keyCode;
   }
   else if (e)
   {
      var charCode = e.which;
   }
   else { return true; }
   if ((charCode > 64 && charCode < 91) || (charCode > 96 && charCode < 123))
       return true;
   else
   {
      alert("Please enter only alphabets");
      return false;
   }
}
function isNumberKey(evt, obj) {

            var charCode = (evt.which) ? evt.which : event.keyCode
            var value = obj.value;
            var dotcontains = value.indexOf(".") != -1;
            if (dotcontains)
                if (charCode == 46) return false;
            if (charCode == 46) return true;
            if (charCode > 31 && (charCode < 48 || charCode > 57))
                return false;
            return true;
        }

function ValidateEmail(mail){
    	//  alert("You have entered an invalid email address!")
    	if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail.value)){
    		return (true);
    	}
    	alert("You have entered an invalid email address!");
    	return (false);
	}
function ValidateForm(){


}

function DelAlert() {
    alert ("Hello world!");
  }


