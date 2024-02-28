
var jsonUrl = document.getElementById('script').getAttribute('data-json-url');
var data = [];
console.log("Попытка загрузить файл JSON...");
$.getJSON(jsonUrl, function(result) {
    console.log("Файл JSON успешно загружен!");
    
    $.each(result, function(index, item) {
        // Добавляем каждый объект из массива в массив data
        data.push(item);
    });

    console.log(data); // Проверяем, что данные загружены корректно

    // Инициализация Autocomplete после загрузки данных
    $( "#auto_check" ).autocomplete({
        source: data
    });
});