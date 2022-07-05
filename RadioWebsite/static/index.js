
$(document).ready(function()
{
    $("form[name='exe_Form']").submit(function(e)
    {
        e.preventDefault();
        // const formData = new FormData(e);
        // fetch('/',{
        //     method: 'POST',
        //     body: formData,
        //
        //     }).then(function(response){
        //         alert("shits done");
        // })
        let inputFields = $(this).serializeArray();
        console.log("????????");
        console.log(inputFields);

        // Send POST request to the Flask server with the body as the field values in JSON format
        const val = async ()=>{
            const response = await fetch('http://192.168.0.19:5000', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                body: JSON.stringify(inputFields),
            });

        }

        val();

        // $.ajax({
        //     type: "POST",
        //     method: "POST",
        //     url:"/",
        //     data: JSON.stringify({ input_fields: inputFields }),
        //     success:function ()
        //     {
        //         alert("HOW ABOUT NOW???");
        //     }
        //     // contentType: "application/json;charset=utf-8",
        //     // dataType: "json",
        //     // data: JSON.stringify({ input_fields: inputFields })
        // });
    });
});


