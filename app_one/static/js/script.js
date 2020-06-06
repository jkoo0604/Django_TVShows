$(document).ready(function() {

    // on click submit
    // if showid > 0 
    // Show.objects.filter(title__iexact=postData['title']).exclude(id=showid).exists()
    // if not
    // Show.objects.filter(title__iexact=postData['title']).exists()

    // generate dictionary of errors and go through loop to create html tags for a list to be displayed

    // append or prepend to designated class (above form)

    // If error dictionary is empty, process form
        

        //inside form tag: add onsubmit="return errorcheck()"
        // function errorcheck(){
        //      check each field for errors
        //      grab showid frmo url (if no url, then use create)
        //      populate error dictionary if found
        //     if error dictionary is not empty
        //          display errors
        //         returnn false;
        // }
        // this will prevent form submission
    // Comment out ShowManager and test


    
 
});
$(".ajaxform").submit(function(e) {
    e.preventDefault();
    var form = $(this);
    var title = $("#title").val();
    var network = $("#network").val();
    var release_date = $("#release_date").val();
    var current_date = new Date();
    var desc = $("#desc").val();
    var output = 0;
    var url = window.location.pathname;

    if (url.substring(url.length-4) == 'edit') {
        var showid = url.substring(url.indexOf('shows/') + 6, url.length-5);
    } else {
        var showid = -1;
    }

    console.log(showid);

    $('.errtitle').html('');
    $('.errnetwork').html('');
    $('.errrelease_date').html('');
    $('.errdesc').html('');

    $.ajax({
        type: 'GET',
        url: "/shows/ajax/validate",
        data: {"title": title, "showid": showid},
        success: function (response) {
            if (response["used"]) {
                // output+="\n<li>Title already exists.</li>\n"
                output +=1;
                $('.errtitle').html('<p>Title already exists.</p>');
            } 
        },
        error: function(response) {
            console.log(response);
        }
    })

    if (title.length < 2) {
        // output+="\n<li>Title must be at least 2 characters long</li>\n"
        output +=1;
                $('.errtitle').html('<p>Title must be at least 2 characters long.</p>') 
    }
    if (network.length < 3) {
        // output+="\n<li>Network must be at least 3 characters long</li>\n"
        output +=1;
                $('.errnetwork').html('<p>Network must be at least 2 characters long.</p>')
    }
    
    if (release_date == '') {
        // output+="\n<li>Release Date is required</li>\n"
        output +=1;
                $('.errrelease_date').html('<p>Release Date is required.</p>')
    }
    else {
        release_date = new Date($("#release_date").val());
        if (release_date.getTime() > current_date.getTime()) {
        // output+="\n<li>Release Date must be in the past</li>\n"
        output +=1;
                $('.errrelease_date').html('<p>Release Date must be in the past.</p>')
        }
    }
    if (desc.length < 10 && desc.length > 0) {
        // output+="\n<li>Description is optional, but must be at least 10 characters long if provided</li>\n"
        output +=1;
                $('.errdesc').html('<p>Description is optional, but must be at least 10 characters long if provided.</p>')
    }

    // if (output.length > 0) {
    if (output > 0) {
        // output = "\n<ul>" + output + "\n<ul>"
        // document.getElementById("errors").innerHTML = output;
        // $('#errors').html(output);
        return false;
    } else {
        form.unbind('submit').submit();
    }
});