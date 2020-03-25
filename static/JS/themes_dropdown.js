$("#applicant_scope").change(function () {
    var url = $("#applicantForm").attr("data-themes-url");
    var scopeId = $(this).val();
    $.ajax({
        url: url,
        data: {
            'scope': scopeId
        },
        success: function (json_data) {
            var x;
            const themes = json_data.themes;
            console.log(themes);
            const themes_div = $("#themes_applicant");
            themes_div.empty();
            for (x in themes) {
                themes_div.append("<option class=text-muted  value=" + themes[x].id + ">" + themes[x].name + "</option>");
            }
            themes_div.selectpicker('refresh');
        }
    });
});