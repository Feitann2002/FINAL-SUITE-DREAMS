document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        const startDateInput = document.getElementById("start_date");
        const endDateInput = document.getElementById("end_date");

        const startDate = new Date(startDateInput.value);
        const endDate = new Date(endDateInput.value);
        const currentDate = new Date();

        const errorMessages = document.querySelectorAll(".error-message");
        errorMessages.forEach(msg => msg.remove());

        let isValid = true;

        if (!startDateInput.value) {
            showError(startDateInput, "Start date and time is required.");
            isValid = false;
        } else if (startDate < currentDate) {
            showError(startDateInput, "Start date and time cannot be in the past.");
            isValid = false;
        }

        if (!endDateInput.value) {
            showError(endDateInput, "End date and time is required.");
            isValid = false;
        } else if (endDate < startDate) {
            showError(endDateInput, "End date and time must be after the start date and time.");
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
        }
    });

    function showError(input, message) {
        const errorMessage = document.createElement("div");
        errorMessage.className = "error-message";
        errorMessage.style.color = "red";
        errorMessage.textContent = message;
        input.parentNode.appendChild(errorMessage);
    }
});