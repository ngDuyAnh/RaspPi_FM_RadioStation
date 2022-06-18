
$(document).ready(function()
{
    $("form[name='exe_Form']").submit(function(e)
    {
        e.preventDefault();

        // let inputFields = $(this).serializeArray();
        // $.ajax({
        //     method: "POST",
        //     url:"/?",
        //     contentType: "application/json;charset=utf-8",
        //     dataType: "json",
        //     data: JSON.stringify({ input_fields: inputFields })
        // }).done(data=>{
        //     console.log(data);
        // })
    });
});


