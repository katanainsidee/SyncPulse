// document.addEventListener('DOMContentLoaded', function() {
//     const phoneInput = document.getElementById('additional_phone_number');
//     phoneInput.addEventListener('input', function() {
//         let value = this.value.replace(/\D/g, ''); // Удаляем все символы, кроме цифр
//         if (value.length > 1) {
//             value = '+' + value.substring(0, 1) + ' (' + value.substring(1);
//         }
//         if (value.length > 7) {
//             value = value.substring(0, 7) + ') ' + value.substring(7);
//         }
//         if (value.length > 12) {
//             value = value.substring(0, 12) + '-' + value.substring(12);
//         }
//         if (value.length > 15) {
//             value = value.substring(0, 15) + '-' + value.substring(15);
//         }
//         this.value = value;
//     });
// });