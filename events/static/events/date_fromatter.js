document.addEventListener('DOMContentLoaded', function() {
        const dateInput = document.getElementById('date_of_birth');
        dateInput.addEventListener('input', function() {
            let value = this.value.replace(/\D/g, '');
            if (value.length > 2) {
                value = value.substring(0, 2) + '.' + value.substring(2);
            }
            if (value.length > 5) {
                value = value.substring(0, 5) + '.' + value.substring(5, 9);
            }
            this.value = value;
        });
    });