    function openPopup(formId) {
        const modal = document.getElementById("popupModal");
        const title = document.getElementById("popupTitle");
        const description = document.getElementById("popupDescription");

        if (formId === 'userPrivacyForm') {
            title.textContent = "User Privacy Inquiry";
            description.textContent = "Please fill out the form if you have any questions about our user privacy policy.";
        } else if (formId === 'dataCollectionForm') {
            title.textContent = "Data Collection Inquiry";
            description.textContent = "Please fill out the form if you have any questions about our data collection practices.";
        } else if (formId === 'dataProtectionForm') {
            title.textContent = "Data Protection Inquiry";
            description.textContent = "Please fill out the form if you have any questions about our data protection measures.";
        } else if (formId === 'thirdPartySharingForm') {
            title.textContent = "Third-Party Sharing Inquiry";
            description.textContent = "Please fill out the form if you have any questions about our third-party sharing policy.";
        }

        modal.style.display = "block";
        setTimeout(() => modal.classList.add("popup-visible"), 10);
    }

    function closePopup() {
        const modal = document.getElementById("popupModal");
        modal.classList.remove("popup-visible");
        setTimeout(() => modal.style.display = "none", 300);
    }

    window.onclick = function(event) {
        if (event.target === document.getElementById("popupModal")) {
            closePopup();
        }
    };