function confirmBack() {
    return confirm("Are you sure you want to go back? Any unsaved changes will be lost.");
}

function validateForm() {
    const startDateInput = document.getElementById("start_date").value;
    const endDateInput = document.getElementById("end_date").value;

    if (!startDateInput || !endDateInput) {
        alert("Please fill in all required fields.");
        return false;
    }

    const startDate = new Date(startDateInput);
    const endDate = new Date(endDateInput);
    const currentDate = new Date();

    if (startDate < currentDate) {
        alert("Start date cannot be in the past.");
        return false;
    }

    if (endDate <= startDate) {
        alert("End date must be after the start date.");
        return false;
    }

    return true;

}