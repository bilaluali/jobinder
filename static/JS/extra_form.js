function displayExtraInfoCompany() {
    var phone_field = document.getElementById("phone");
    var city_field = document.getElementById("city");
    var zip_field = document.getElementById("zip");
    var url_field = document.getElementById("url");
    var scope_field = document.getElementById("scope");
    var logo_field = document.getElementById("logo");
    var fields = [phone_field, city_field, zip_field, url_field, scope_field, logo_field]

    for (var i = 0; i < fields.length; i++) {
        if (fields[i].style.display == "block") {
            fields[i].style.display = "none";
        } else {
            fields[i].style.display = "block";
        }
    }

}

function displayExtraInfoApplicant() {
    var phone_field = document.getElementById("phone");
    var city_field = document.getElementById("city");
    var zip_field = document.getElementById("zip");
    var desc_field = document.getElementById("description");
    var scope_field = document.getElementById("scope");
    var theme_field = document.getElementById("theme");
    var photo_field = document.getElementById("photo");
    var fields = [phone_field, city_field, zip_field, desc_field, scope_field, theme_field, photo_field];

    for (var i=0; i<fields.length; i++){
        if (fields[i].style.display == "block"){
            fields[i].style.display = "none";
        }
        else{
            fields[i].style.display = "block";
        }
    }
}

