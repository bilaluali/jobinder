function profile_request(url_name) {
    var req = new XMLHttpRequest(); // Create the request.
    req.open('GET', url_name);
    req.onreadystatechange = function () {
        // State == 4, server response ok.
        if (req.readyState === 4) {
            document.getElementById('profile_options').innerHTML = req.responseText;
        }
    };

    // Send request
    req.send();
}