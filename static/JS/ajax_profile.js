function profile_request(url_name) {
    var req = new XMLHttpRequest(); // Create the request.
    req.open('GET', url_name);
    req.onreadystatechange = function () {
        // State == 4, server response ok.
        if (req.readyState === 4) {

            document.write(req.responseText);
            history.pushState({}, null, url_name);
        }
    };
    // Send request
    req.send();
}