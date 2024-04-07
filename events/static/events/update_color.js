function updateColor(selectElement, url) {
    var color = selectElement.value;
    var participantId = selectElement.getAttribute('id');
    var csrftoken = getCookie('csrftoken'); // Получаем CSRF-токен из куки

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken // Передаем CSRF-токен в заголовке запроса
        },
        body: JSON.stringify({
            participant_id: participantId,
            color: color
        })

    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Ошибка при отправке данных');
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
    setTimeout(function() {
    window.location.reload();
}, 10);
}

// Функция для получения CSRF токена из куки
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}