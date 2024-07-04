document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('loginForm');
    const submitButton = document.getElementById('submit_button');
    const loginError = document.getElementById('login_error');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // 기본 폼 제출 방지

        // 폼 데이터를 FormData 객체로 생성
        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.ok) {
                window.location.href = '';
            } else {
                response.json().then(data => {
                    if (data.errors) {
                        loginError.textContent = '로그인 실패: ' + data.errors;
                    }
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});