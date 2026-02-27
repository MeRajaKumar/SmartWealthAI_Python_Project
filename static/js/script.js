document.addEventListener("DOMContentLoaded", function () {
    var body = document.body;
    var modals = document.querySelectorAll(".site-modal");
    var openButtons = document.querySelectorAll("[data-open-modal]");
    var closeButtons = document.querySelectorAll("[data-close-modal]");

    if (!modals.length || !openButtons.length) {
        return;
    }

    function openModal(modal) {
        if (!modal) {
            return;
        }
        modal.classList.add("show");
        modal.setAttribute("aria-hidden", "false");
        body.style.overflow = "hidden";
    }

    function closeModal(modal) {
        if (!modal) {
            return;
        }
        modal.classList.remove("show");
        modal.setAttribute("aria-hidden", "true");
        if (!document.querySelector(".site-modal.show")) {
            body.style.overflow = "hidden";
        }
    }

    openButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var targetId = button.getAttribute("data-open-modal");
            var targetModal = document.getElementById(targetId);
            openModal(targetModal);
        });
    });

    closeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var modal = button.closest(".site-modal");
            closeModal(modal);
        });
    });

    modals.forEach(function (modal) {
        modal.addEventListener("click", function (event) {
            if (event.target === modal) {
                closeModal(modal);
            }
        });
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            document.querySelectorAll(".site-modal.show").forEach(function (modal) {
                closeModal(modal);
            });
        }
    });
});
