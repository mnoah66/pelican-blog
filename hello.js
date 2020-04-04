<script type="text/javascript">
    $('#myForm').submit(function(e) {
        $('#exampleModal').modal('show');
        e.preventDefault();
        $.ajax({
            url: "https://purring-dodo.prod.with-datafire.io/contact",
            type: 'post',
            data: $('#myForm').serialize(),
            success: function() {
                $('#myForm :input').val('');
                //whatever you wanna do after the form is successfully submitted
            }
        });
    });
</script>