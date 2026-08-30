document.addEventListener("DOMContentLoaded", () => {

    const themeToggle =
        document.getElementById("themeToggle");

    const menuToggle =
        document.getElementById("menuToggle");

    const navLinks =
        document.getElementById("navLinks");


    /* ========================================
       Theme
    ======================================== */

    const savedTheme = localStorage.getItem("theme");


/*
 * Dark mode is the default theme.
 *
 * If the user has previously selected a theme,
 * respect their choice.
 */

if (savedTheme === null || savedTheme === "dark") {

    document.body.classList.add("dark");

    themeToggle.textContent = "☀️";

} else {

    document.body.classList.remove("dark");

    themeToggle.textContent = "🌙";

}


themeToggle.addEventListener(
    "click",
    () => {

        document.body.classList.toggle("dark");

        const isDark =
            document.body.classList.contains("dark");


        localStorage.setItem(
            "theme",
            isDark ? "dark" : "light"
        );


        themeToggle.textContent =
            isDark ? "☀️" : "🌙";

    }
);

    /* ========================================
       Mobile Navigation
    ======================================== */

    menuToggle.addEventListener(
        "click",
        () => {

            navLinks.classList.toggle("active");

        }
    );


    /* Close mobile menu after clicking link */

    navLinks
        .querySelectorAll("a")
        .forEach(link => {

            link.addEventListener(
                "click",
                () => {

                    navLinks.classList.remove(
                        "active"
                    );

                }
            );

        });

});