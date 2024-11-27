function confirmBack() {
return confirm("Are you sure you want to go back? Any unsaved changes will be lost.");
}

function validatePasswords() {
const password = document.getElementById('id_password').value;
const confirmPassword = document.getElementById('id_confirm_password').value;

    if (password !== confirmPassword) {
        alert("Passwords do not match. Please try again.");
            return false;
            }
            return true;
            }