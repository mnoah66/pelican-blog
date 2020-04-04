Title: Contact
JavaScripts: main.js

If you'd like to get in touch with me, check me out on [Twitter](https://twitter.com/MixMasterMartin) or shoot me a message:

<form id="myForm" onsubmit=";myFunc(); return false;">
	<div class="form-group">
		<label for="formGroupExampleInput">Name</label>
		<input required type="text" class="form-control" id="fromName" placeholder="Enter name" name="name">
	</div>
	<div class="form-group">
		<label for="exampleInputEmail1">Email address</label>
		<input type="email" class="form-control" id="fromEmail" aria-describedby="emailHelp" placeholder="Enter email" name="emailAddress" required>
		<small id="emailHelp" class="form-text text-muted">Your email is safe with me!</small>
	</div>
	<div class="form-group">
		<label for="exampleFormControlTextarea1">Message</label>
		<textarea required class="form-control" id="fromMessage" rows="3" name="message"></textarea>
		<input type="text" name="_gotcha" style="display:none" />
		<input type="hidden" name="_next" value="https://martindnoah.com/index.html" />
	</div>
	<div class="g-recaptcha form-group" data-sitekey="6LeYF3EUAAAAAObkuXXTj4BpF2xpIsIt-CZTWMqo"></div>
	<div class="form-group">
		<button class="btn btn-primary btn-lg" type="submit">Send</button>
	</div>
</form>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Thank you</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        I'll reach out to you shortly!
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary btn-lg" data-dismiss="modal" onclick="window.location.replace('https://martinnoah.com');">Close</button>
      </div>
    </div>
  </div>
</div>



<script type="text/javascript">
function myFunc() {
    if (grecaptcha.getResponse() === '') {                            
      alert('Please check the recaptcha');
      return;
    }
    $("#exampleModal").modal("show");
    //e.preventDefault();
    $.ajax({
        url: "https://black-clownfish.prod.with-datafire.io/contact",
        type: "post",
        data: $("#myForm").serialize(),
    success: function() {
        //$("#myForm :input").val("");
        //window.location.replace("https://martinnoah.com");
        //$("#exampleModal").modal("show");
    //whatever you wanna do after the form is successfully submitted
  }
});
};
</script>



<!-- attr to SO uer ryanlb: https://stackoverflow.com/questions/31017261/require-user-to-click-googles-new-recaptcha-before-form-submission -->

<!--
<script type="text/javascript">
  var form = document.getElementById('myForm');
  form.addEventListener("click", function(event){
    if (grecaptcha.getResponse() === '') {                            
      event.preventDefault();
      alert('Please check the recaptcha');
    } else {
      $.ajax({
      url: "https://purring-dodo.prod.with-datafire.io/contact",
      type: "post",
      data: $("#myForm").serialize(),
    success: function() {
      $("#myForm :input").val("");
    //whatever you wanna do after the form is successfully submitted
    }
  }
, false);
</script>
-->
  