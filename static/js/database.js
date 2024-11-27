function showDashboard() {
    document.getElementById('dashboard').style.display = 'block';
    document.getElementById('admins').style.display = 'none';
    document.getElementById('users').style.display = 'none';
    document.getElementById('rooms').style.display = 'none';
    document.getElementById('appointments').style.display = 'none';
    document.getElementById('offers').style.display = 'none';
    document.getElementById('feedbacks').style.display = 'none';
}

function showAdmins() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('admins').style.display = 'block';
    document.getElementById('users').style.display = 'none';
    document.getElementById('rooms').style.display = 'none';
    document.getElementById('appointments').style.display = 'none';
    document.getElementById('offers').style.display = 'none';
    document.getElementById('feedbacks').style.display = 'none';
}

function showUsers() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('admins').style.display = 'none';
    document.getElementById('users').style.display = 'block';
    document.getElementById('rooms').style.display = 'none';
    document.getElementById('appointments').style.display = 'none';
    document.getElementById('offers').style.display = 'none';
    document.getElementById('feedbacks').style.display = 'none';
}

function showRooms() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('admins').style.display = 'none';
    document.getElementById('users').style.display = 'none';
    document.getElementById('rooms').style.display = 'block';
    document.getElementById('appointments').style.display = 'none';
    document.getElementById('offers').style.display = 'none';
    document.getElementById('feedbacks').style.display = 'none';
}

function showAppointments() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('admins').style.display = 'none';
    document.getElementById('users').style.display = 'none';
    document.getElementById('rooms').style.display = 'none';
    document.getElementById('appointments').style.display = 'block';
    document.getElementById('offers').style.display = 'none';
    document.getElementById('feedbacks').style.display = 'none';
}

function showOffers() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('admins').style.display = 'none';
    document.getElementById('users').style.display = 'none';
    document.getElementById('rooms').style.display = 'none';
    document.getElementById('appointments').style.display = 'none';
    document.getElementById('offers').style.display = 'block';
    document.getElementById('feedbacks').style.display = 'none';
}

function showFeedbacks() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('admins').style.display = 'none';
    document.getElementById('users').style.display = 'none';
    document.getElementById('rooms').style.display = 'none';
    document.getElementById('appointments').style.display = 'none';
    document.getElementById('offers').style.display = 'none';
    document.getElementById('feedbacks').style.display = 'block';
}

function searchAdmins() {
    const input = document.getElementById('adminSearch').value.toLowerCase();
    const rows = document.querySelectorAll('#adminTableBody tr');
    rows.forEach(row => {
        const cells = row.getElementsByTagName('td');
        row.style.display = Array.from(cells).some(cell => cell.textContent.toLowerCase().includes(input)) ? '' : 'none';
    });
}

function searchUsers() {
    const input = document.getElementById('userSearch').value.toLowerCase();
    const rows = document.querySelectorAll('#userTableBody tr');
    rows.forEach(row => {
        const cells = row.getElementsByTagName('td');
        row.style.display = Array.from(cells).some(cell => cell.textContent.toLowerCase().includes(input)) ? '' : 'none';
    });
}

function searchRooms() {
    const input = document.getElementById('roomSearch').value.toLowerCase();
    const rows = document.querySelectorAll('#roomTableBody tr');
    rows.forEach(row => {
         const cells = row.getElementsByTagName('td');
         row.style.display = Array.from(cells).some(cell => cell.textContent.toLowerCase().includes(input)) ? '' : 'none';
    });
}

function searchAppointments() {
     const input = document.getElementById('appointmentSearch').value.toLowerCase();
     const rows = document.querySelectorAll('#appointmentTableBody tr');
     rows.forEach(row => {
          const cells = row.getElementsByTagName('td');
          row.style.display = Array.from(cells).some(cell => cell.textContent.toLowerCase().includes(input)) ? '' : 'none';
     });
}

function searchOffers() {
    const input = document.getElementById('offerSearch').value.toLowerCase();
    const rows = document.querySelectorAll('#offerTableBody tr');
    rows.forEach(row => {
        const cells = row.getElementsByTagName('td');
        row.style.display = Array.from(cells).some(cell => cell.textContent.toLowerCase().includes(input)) ? '' : 'none';
    });
}

function searchFeedbacks() {
    const input = document.getElementById('feedbackSearch').value.toLowerCase();
    const rows = document.querySelectorAll('#feedbackTableBody tr');
    rows.forEach(row => {
        const cells = row.getElementsByTagName('td'); // Corrected here
        row.style.display = Array.from(cells).some(cell => cell.textContent.toLowerCase().includes(input)) ? '' : 'none';
    });
}

function getCookie(name) {
    const cookies = document.cookie.split(';').map(cookie => cookie.trim());
    const cookieValue = cookies.find(cookie => cookie.startsWith(name + '='));
    return cookieValue ? decodeURIComponent(cookieValue.split('=')[1]) : null;
}

function showSection(section) {
    document.querySelectorAll('.content-section').forEach(function(sec) {
        sec.style.display = 'none';
    });
    document.getElementById(section).style.display = 'block';
}

window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    const section = urlParams.get('section');
    if (section) {
        showSection(section);
    } else {
        showSection('dashboard');
    }
};

function confirmLogout() {
      return confirm("Are you sure you want to log out?");
}