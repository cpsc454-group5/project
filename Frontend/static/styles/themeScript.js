function swtichToDarkMode() {
    // switch color to dark Colors.
    const body = document.body;
    body.classList.add('dark-mode');
    const toggleButton = document.getElementById('dark-mode-toggle');
    toggleButton.textContent = 'Light Mode';

    localStorage.setItem("theme", "dark");

    var header = document.getElementById("header");
    var content = document.getElementById("contentRow");
    var footer = document.getElementById("footer");

    header.classList.remove("header");
    content.classList.remove("contentRow");
    footer.classList.remove("footer");

    header.classList.add("header_dark");
    content.classList.add("contentRow_dark");
    footer.classList.add("footer_dark");
}

function switchToLightMode() {
    localStorage.setItem("theme", "light");
    const toggleButton = document.getElementById('dark-mode-toggle');
    toggleButton.textContent = 'Dark Mode';

    var header = document.getElementById("header");
    var content = document.getElementById("contentRow");
    var footer = document.getElementById("footer");

    header.classList.remove("header_dark");
    content.classList.remove("contentRow_dark");
    footer.classList.remove("footer_dark");

    header.classList.add("header");
    content.classList.add("contentRow");
    footer.classList.add("footer");
}


function initiateTheme() {
    var theme = localStorage.getItem("theme");
    var route = window.location.pathname;
    if (theme == "dark") {
        (route == '/reservations' || route == '/reserve') ? swtichToDarkMode_reserve() : swtichToDarkMode();
    } else {
        (route == '/reservations' || route == '/reserve') ? switchToLightMode_reserve() : switchToLightMode();
        // switchToLightMode();
    }
}


function swtichToDarkMode_reserve() {
    // switch color to dark Colors.
    const body = document.body;
    body.classList.add('dark-mode');
    const toggleButton = document.getElementById('dark-mode-toggle');
    toggleButton.textContent = 'Light Mode';

    localStorage.setItem("theme", "dark");

    var header = document.getElementById("header");
    var content = document.getElementById("contentCol");
    var footer = document.getElementById("footer");
    var reserveList = document.getElementById("reserveList");


    header.classList.remove("header");
    content.classList.remove("contentCol");
    footer.classList.remove("footer");
    reserveList.classList.remove("reserveList");

    header.classList.add("header_dark");
    content.classList.add("contentCol_dark");
    footer.classList.add("footer_dark");
    reserveList.classList.add("reserveList_dark");


    var theme = localStorage.getItem("theme");
    var route = window.location.pathname;
    if (route == '/reserve') {
        var reserve = document.getElementById("reserve");
        reserve.classList.remove("reserve");
        reserve.classList.add("reserve_dark");
    }
}

function switchToLightMode_reserve() {
    localStorage.setItem("theme", "light");
    const toggleButton = document.getElementById('dark-mode-toggle');
    toggleButton.textContent = 'Dark Mode';

    var header = document.getElementById("header");
    var content = document.getElementById("contentCol");
    var footer = document.getElementById("footer");
    var reserveList = document.getElementById("reserveList");

    header.classList.remove("header_dark");
    content.classList.remove("contentCol_dark");
    footer.classList.remove("footer_dark");
    reserveList.classList.remove("reserveList_dark");

    header.classList.add("header");
    content.classList.add("contentCol");
    footer.classList.add("footer");
    reserveList.classList.add("reserveList");

    
    var theme = localStorage.getItem("theme");
    var route = window.location.pathname;
    if (route == '/reserve') {
        var reserve = document.getElementById("reserve");
        reserve.classList.remove("reserve_dark");
        reserve.classList.add("reserve");
    }
}