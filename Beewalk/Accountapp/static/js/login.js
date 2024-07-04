document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementsByTagName('form')[0];
    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent default form submission

        // Get form data
        var formData = new FormData(form);

        // Perform Ajax request to submit form data
        fetch('/account/login/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token for POST requests
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();  // Parse response as JSON
            } else {
                throw new Error('서버에서 오류가 발생했습니다.');  // Throw error for non-OK response
            }
        })
        .then(data => {
            if (data && data.redirect) {
                console.log('Redirecting to:', data.redirect);
                window.location.href = data.redirect;  // Redirect to the URL provided by the server
            } else {
                throw new Error('서버에서 유효한 리다이렉트 URL을 반환하지 않았습니다.');  // Throw error if redirect URL is not provided
            }
        })
        .catch(error => {
            console.error('Error:', error.message);
            alert('로그인 과정에서 오류가 발생했습니다.');
        });
    });
});

// Function to get CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
