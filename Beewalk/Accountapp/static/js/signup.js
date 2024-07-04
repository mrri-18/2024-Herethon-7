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

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('signupForm');
    const passwordField = form.querySelector('[name="password"]');
    const checkpwdField = form.querySelector('[name="checkpwd"]');
    const passwordCheckSuccess = document.getElementById('password_check_success');
    const submitButton = document.getElementById('submit_button');


    checkpwdField.addEventListener('input', validateForm);
    passwordField.addEventListener('input', validateForm);

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const password = passwordField.value;
        const checkpwd = checkpwdField.value;

        if (password !== checkpwd) {
            passwordCheckSuccess.textContent = '🚫 비밀번호가 일치하지 않습니다';
            return;
        } else {
            passwordCheckSuccess.textContent = '';
        }

        if (passwordCheckSuccess.textContent === '') {
            // 폼을 AJAX로 제출
            const formData = new FormData(form);
            fetch(form.action, {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    window.location.href = '/account/login/'; // 성공 시 로그인 페이지로 이동
                } else {
                    // 서버 측에서 발생한 오류 처리
                    response.json().then(data => {
                        if (data.errors) {
                            // 서버 측 오류 메시지를 폼에 표시
                            Object.keys(data.errors).forEach(key => {
                                const errorElement = document.getElementById(`${key}_check_success`);
                                if (errorElement) {
                                    errorElement.textContent = data.errors[key];
                                }
                            });
                        }
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });

    function validateForm() {
        const password = passwordField.value;
        const checkpwd = checkpwdField.value;

        if (password !== checkpwd) {
            passwordCheckSuccess.textContent = '🚫 비밀번호가 일치하지 않습니다';
        } else {
            passwordCheckSuccess.textContent = '';
        }

        if ( passwordCheckSuccess.textContent === '') {
            submitButton.classList.add('enabled');
        } else {
            submitButton.classList.remove('enabled');
        }
    }
});
