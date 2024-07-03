document.addEventListener('DOMContentLoaded', function() {
    // 로그인 폼 제출(submit) 이벤트 처리
    document.querySelector('#login-form').addEventListener('submit', function(event) {
        event.preventDefault();  // 폼의 기본 제출 동작 방지

        // 폼 데이터 가져오기
        var email = document.querySelector('#id_email').value;
        var password = document.querySelector('#id_password').value;

        // AJAX를 통한 서버 요청
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/account/login/', true);  // 로그인 뷰의 URL 경로로 변경 필요
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');  // CSRF 토큰 추가

        // AJAX 요청 완료 시 처리
        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 300) {
                var response = JSON.parse(xhr.responseText);
                if (response.success) {
                    // 로그인 성공 시 리다이렉트
                    window.location.href = '/';  // Homeapp/templates/home.html 경로로 변경
                } else {
                    // 로그인 실패 시 에러 메시지 출력
                    alert(response.error_message);
                }
            } else {
                // 서버 오류 처리
                alert('서버 오류가 발생했습니다.');
            }
        };

        // 폼 데이터 전송
        var data = 'email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(password);
        xhr.send(data);
    });
});
