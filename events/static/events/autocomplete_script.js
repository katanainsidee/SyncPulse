var jsonUrl = document.getElementById('script').getAttribute('data-json-url');
var data = [];
console.log("Попытка загрузить файл JSON...");
$.getJSON(jsonUrl, function(result) {
    console.log("Файл JSON успешно загружен!");

    data = result.map(item => {
        return {
            label: `${item.last_name} ${item.first_name} ${item.patronymic}`,
            value: item
        };
    });

    $( "#last_name" ).autocomplete({
        source: data,
        select: function(event, ui) {
            var selectedItem = ui.item.value;
            var last_name = selectedItem.last_name
            console.log(last_name);
            $("#first_name").val(selectedItem.first_name);
            $("#patronymic").val(selectedItem.patronymic);
            $("#date_of_birth").val(selectedItem.date_of_birth);
            $("#district").val(selectedItem.district);
            $("#street").val(selectedItem.street);
            $("#house_number").val(selectedItem.house_number);
            $("#building").val(selectedItem.building);
            $("#apartment_number").val(selectedItem.apartment_number);
            $("#phone_number").val(selectedItem.phone_number);
            $("#additional_phone_number").val(selectedItem.additional_phone_number);
            event.preventDefault()
            $("#last_name").val(selectedItem.last_name);
            return false;
        }
    });
});