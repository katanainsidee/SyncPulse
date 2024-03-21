document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#participant-form');
    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        if (data.error) {
            document.querySelector('.error-message').textContent = data.error;
        } else {
            window.location.href = data.redirect_url;
        }
    });
});