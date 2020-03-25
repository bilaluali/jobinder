function ajax_profile(url_name, div_id)
{
    var req = new XMLHttpRequest(); // Create the request.
    req.open('GET', url_name);
    req.setRequestHeader("X-Requested-With" ,"XMLHttpRequest");
    req.onreadystatechange = function () {
        // State == 4, server response ok.
        if (req.readyState === 4) {
            document.getElementById(div_id).innerHTML = req.responseText;
            history.replaceState(history.state, '', url_name);
        }
    };
    // Send request
    req.send();
}
