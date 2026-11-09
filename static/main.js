function togleTheme() {
    if (document.body.getAttribute("data-bs-theme") == "light") {
        document.body.setAttribute("data-bs-theme", "dark");
        localStorage.setItem("theme", "dark");
    } else {
        document.body.setAttribute("data-bs-theme", "light");
        localStorage.setItem("theme", "light");
    }
}

function ready() {
    if (localStorage.getItem("theme") == "dark") {
        document.body.setAttribute("data-bs-theme", "dark");
    }
}