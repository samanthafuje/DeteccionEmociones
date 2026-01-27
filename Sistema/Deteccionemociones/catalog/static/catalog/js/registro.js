document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        const edad = document.querySelector("#id_edad").value;

        if (edad <= 0) {
            alert("La edad debe ser un número válido");
            e.preventDefault();
        }
    });
});