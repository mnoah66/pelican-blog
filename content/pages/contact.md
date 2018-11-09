Title: Contact

If you'd like to get in touch with me, check me out on [Twitter](https://twitter.com/MixMasterMartin) or shoot me a message:

<form id="myForm">
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
				<div class="form-group">
					<button class="btn btn-primary btn-lg" type="submit">Send</button>
				</div>
  			</form>



<script type="text/javascript">
    	$('#myForm').submit(function(e){
		    $('#exampleModal').modal('show');
		    e.preventDefault();
		    $.ajax({
		        url:"https://purring-dodo.prod.with-datafire.io/contact",
		        type:'post',
		        data:$('#myForm').serialize(),
		        success:function(){
		            $('#myForm :input').val('');
		            //whatever you wanna do after the form is successfully submitted
		        }
		    });
		});
    </script>