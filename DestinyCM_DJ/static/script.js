$(document).ready(function() {
    // console.log(localStorage.getItem('access_token'))

    //send OAuth token to back-end on Overview page
    if(document.title == 'Overview'){
        const auth_token = localStorage.getItem('access_token')
        const dict_values = {auth_token} //Pass the javascript variables to a dictionary.
        const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
        console.log(s); // Prints the variables to console window, which are in the JSON format
        $.ajax({
            url:"/fetcheddata", // arbitrary url associated with a python function on view.py
            type:"POST",
            contentType: "application/json",
            data: JSON.stringify(s)
        });
    }
});

function testPassing() {
    console.log('bro')
};