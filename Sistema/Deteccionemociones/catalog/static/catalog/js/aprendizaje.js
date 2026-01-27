document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        const grupos = {};

        document.querySelectorAll("input[type='radio']").forEach(radio => {
            if (!grupos[radio.name]) {
                grupos[radio.name] = false;
            }
            if (radio.checked) {
                grupos[radio.name] = true;
            }
        });

        const incompletas = Object.values(grupos).some(v => v === false);

        if (incompletas) {
            e.preventDefault();
            alert("⚠️ Por favor contesta todas las preguntas antes de continuar.");
        }
    });
});