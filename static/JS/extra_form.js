function displayExtraInfoCompany() {
    var phone_field = document.getElementById("phone");
    var city_field = document.getElementById("city");
    var zip_field = document.getElementById("zip");
    var url_field = document.getElementById("url");
    var scope_field = document.getElementById("scope");
    var logo_field = document.getElementById("logo");

    if (phone_field.style.display == "block" &&
        city_field.style.display == "block" &&
        zip_field.style.display == "block" &&
        url_field.style.display == "block" &&
        scope_field.style.display == "block" &&
        logo_field.style.display == "block")
    {
        phone_field.style.display = "none";
        city_field.style.display = "none";
        zip_field.style.display = "none";
        url_field.style.display = "none";
        scope_field.style.display = "none";
        logo_field.style.display = "none";
    }
    else {
        phone_field.style.display = "block";
        city_field.style.display = "block";
        zip_field.style.display = "block";
        url_field.style.display = "block";
        scope_field.style.display = "block";
        logo_field.style.display = "block";
    }
}


function displayExtraInfoApplicant() {
    var phone_field = document.getElementById("phone");
    var city_field = document.getElementById("city");
    var zip_field = document.getElementById("zip");
    var desc_field = document.getElementById("description");
    var scope_field = document.getElementById("scope");
    var theme_field = document.getElementById("theme");

    if (phone_field.style.display == "block" &&
        city_field.style.display == "block" &&
        zip_field.style.display == "block" &&
        desc_field.style.display == "block" &&
        scope_field.style.display == "block"&&
        theme_field.style.display == "block")
    {
        phone_field.style.display = "none";
        city_field.style.display = "none";
        zip_field.style.display = "none";
        desc_field.style.display = "none";
        scope_field.style.display = "none";
        theme_field.style.display = "none";
    }
    else {
        phone_field.style.display = "block";
        city_field.style.display = "block";
        zip_field.style.display = "block";
        desc_field.style.display = "block";
        scope_field.style.display = "block";
        theme_field.style.display = "block";
    }
}

