document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function () {
            // Usamos setTimeout para esperar que FastAPI recargue la página
            setTimeout(() => {
                alert("✅ Libro registrado con éxito 📘");
            }, 100);
        });
    }
});