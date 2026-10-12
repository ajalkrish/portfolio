
const form = document.querySelector("#contact-form");
const status = document.querySelector("#form-status");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  if (!form.checkValidity()) {
    form.reportValidity();
    return;
  }

  status.textContent =
    "Thank you! Your form has been validated.";

  form.reset();
});