var jsonUrl = document.getElementById('script').getAttribute('data-json-url');
var data = [];
console.log("Попытка загрузить файл JSON...");
$.getJSON(jsonUrl, function(result) {
    console.log("Файл JSON успешно загружен!");

    // Преобразуем данные для автозаполнения
    data = result.map(item => {
        return {
            label: item.phone_number, // Отображаемый в списке номер телефона
            value: item // Вся запись о человеке
        };
    });

    console.log(data); // Проверяем, что данные загружены корректно

    // Инициализация Autocomplete после загрузки данных
    $( "#phone_number" ).autocomplete({
        source: data,
        select: function(event, ui) {
            var selectedItem = ui.item.value; // Получаем всю запись о человеке
            var phone_number = selectedItem.phone_number
            console.log(phone_number);
            $("#first_name").val(selectedItem.first_name);
            $("#patronymic").val(selectedItem.patronymic);
            $("#date_of_birth").val(selectedItem.date_of_birth);
            $("#district").val(selectedItem.district);
            $("#street").val(selectedItem.street);
            $("#house_number").val(selectedItem.house_number);
            $("#building").val(selectedItem.building);
            $("#apartment_number").val(selectedItem.apartment_number);
            $("#last_name").val(selectedItem.last_name);
            $("#additional_phone_number").val(selectedItem.additional_phone_number);
            event.preventDefault()
            $("#phone_number").val(selectedItem.phone_number);
            return false;
        }
    });
});