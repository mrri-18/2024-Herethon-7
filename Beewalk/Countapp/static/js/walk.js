let timerInterval;
let hours = 0,
    minutes = 0,
    seconds = 0;

function startTimer() {
    timerInterval = setInterval(function () {
        seconds++;
        if (seconds >= 60) {
            seconds = 0;
            minutes++;
            if (minutes >= 60) {
                minutes = 0;
                hours++;
            }
        }
        document.getElementById("hour").textContent = pad(hours);
        document.getElementById("min").textContent = pad(minutes);
        document.getElementById("sec").textContent = pad(seconds);
    }, 1000);
}

function stopTimer() {
    clearInterval(timerInterval);
}

function pad(val) {
    let valString = val + "";
    if (valString.length < 2) {
        return "0" + valString;
    } else {
        return valString;
    }
}

// 페이지 로드 시 타이머 시작
document.addEventListener("DOMContentLoaded", function () {
    startTimer();
});

// "완료" 버튼 클릭 시 타이머 멈춤
document.getElementById("d_link").addEventListener("click", function (e) {
    e.preventDefault();
    stopTimer();
    // 페이지 이동
    window.location.href = "../page/walk_check.html";
});

function fillProgressBar() {
    let km = 1.3;
    let progressBar = document.getElementById("w_progressr");
    let maxWidth = document.querySelector(".w_content").clientWidth;
    let width = (km / 1.9) * maxWidth;

    // 최대 너비를 넘지 않도록 설정
    width = Math.min(width, maxWidth);

    // 막대그래프에 적용
    progressBar.style.width = width + "px";
}

// 예시로 1.3km를 기준으로 채워진 상태를 보여줍니다.
fillProgressBar(1.9);
