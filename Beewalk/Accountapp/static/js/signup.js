const emailInput = document.getElementById("email_input");
const emailCheckBtn = document.getElementById("email_check");
const emailCheckSuccess = document.getElementById("email_check_sucess");
const passwordInput = document.getElementById("password");
const passwordCheckInput = document.getElementById("password_check");
const passwordCheckSuccess = document.getElementById("password_check_sucess");
const usernameInput = document.getElementById("username_input");
const usernameCheckBtn = document.getElementById("username_check");
const usernameCheckSuccess = document.getElementById("username_check_sucess");
const submitButton = document.getElementById("submit_button");

let isEmailChecked = false;
let isUsernameChecked = false;

emailCheckBtn.addEventListener("click", () => {
    const email = emailInput.value;
    if (email === "test@example.com") {
        // 예제 중복 확인 로직
        emailCheckSuccess.textContent = "🚫 이미 사용중인 아이디입니다";
        emailCheckSuccess.className = "error";
        isEmailChecked = false;
    } else {
        emailCheckSuccess.textContent = "✅ 사용가능한 아이디입니다";
        emailCheckSuccess.className = "success";
        isEmailChecked = true;
    }
    validateForm();
});

usernameCheckBtn.addEventListener("click", () => {
    const username = usernameInput.value;
    if (username === "testuser") {
        // 예제 중복 확인 로직
        usernameCheckSuccess.textContent = "🚫 이미 사용중인 이름입니다";
        usernameCheckSuccess.className = "error";
        isUsernameChecked = false;
    } else {
        usernameCheckSuccess.textContent = "✅ 사용가능한 이름입니다";
        usernameCheckSuccess.className = "success";
        isUsernameChecked = true;
    }
    validateForm();
});

passwordCheckInput.addEventListener("input", () => {
    if (passwordInput.value !== passwordCheckInput.value) {
        passwordCheckSuccess.textContent = "🚫 비밀번호가 일치하지 않습니다";
        passwordCheckSuccess.className = "error";
    } else {
        passwordCheckSuccess.textContent = "";
    }
    validateForm();
});

emailInput.addEventListener("input", () => {
    if (!emailInput.value) {
        emailCheckSuccess.textContent = "";
        isEmailChecked = false;
    }
    validateForm();
});

usernameInput.addEventListener("input", () => {
    if (!usernameInput.value) {
        usernameCheckSuccess.textContent = "";
        isUsernameChecked = false;
    }
    validateForm();
});

function validateForm() {
    if (
        isEmailChecked &&
        isUsernameChecked &&
        passwordInput.value === passwordCheckInput.value &&
        passwordInput.value !== ""
    ) {
        submitButton.classList.add("enabled");
        submitButton.disabled = false;
    } else {
        submitButton.classList.remove("enabled");
        submitButton.disabled = true;
    }
}

function validateOnSubmit() {
    let isValid = true;

    if (!isEmailChecked) {
        emailCheckSuccess.textContent = "🚫 중복확인을 해주세요";
        emailCheckSuccess.className = "error";
        isValid = false;
    }

    if (!isUsernameChecked) {
        usernameCheckSuccess.textContent = "🚫 중복확인을 해주세요";
        usernameCheckSuccess.className = "error";
        isValid = false;
    }

    if (
        passwordInput.value !== passwordCheckInput.value ||
        passwordInput.value === ""
    ) {
        passwordCheckSuccess.textContent = "🚫 비밀번호가 일치하지 않습니다";
        passwordCheckSuccess.className = "error";
        isValid = false;
    }

    return isValid;
}

document.querySelector("form").addEventListener("submit", (event) => {
    if (!validateOnSubmit()) {
        event.preventDefault();
    }
});

function previewImage(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function () {
        const preview = document.getElementById("photo_img");
        preview.src = reader.result;
        preview.style.display = "block";
    };
    if (file) {
        reader.readAsDataURL(file);
    }
}
