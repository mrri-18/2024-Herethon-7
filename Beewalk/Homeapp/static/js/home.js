function fillProgressBar(km) {
    let progressBar = document.getElementById("w_progressr");
    let maxWidth = document.querySelector(".w_content").clientWidth;
    let width = (km / 41.5) * maxWidth;

    // 최대 너비를 넘지 않도록 설정
    width = Math.min(width, maxWidth);

    // 막대그래프에 적용
    progressBar.style.width = width + "px";
}

// 예시로 1.3km를 기준으로 채워진 상태를 보여줍니다.
fillProgressBar(18.6);

document.addEventListener("DOMContentLoaded", function () {
    const calendar = document.querySelector(".calendar");
    const calMon = calendar.querySelector(".cal_mon");
    const calDates = calendar.querySelector(".cal_dates");

    const today = new Date();
    const currentMonth = today.getMonth();
    const currentYear = today.getFullYear();
    const currentDate = today.getDate();

    // 예제 거리값
    const distance = 2; // 이 값을 실제 거리 값으로 바꾸세요

    function renderCalendar(month, year) {
        calDates.innerHTML = "";

        calMon.innerText = `${year}.${String(month + 1).padStart(2, "0")}`;

        const firstDay = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        for (let i = 0; i < firstDay; i++) {
            const emptyCell = document.createElement("div");
            emptyCell.classList.add("date");
            calDates.appendChild(emptyCell);
        }

        for (let day = 1; day <= daysInMonth; day++) {
            const dateCell = document.createElement("div");
            dateCell.classList.add("date");
            dateCell.innerText = day;

            if (day === currentDate) {
                dateCell.classList.add("today");
                if (distance < 5) {
                    dateCell.classList.add("polygon1");
                } else if (distance >= 5 && distance < 10) {
                    dateCell.classList.add("polygon2");
                } else {
                    dateCell.classList.add("polygon3");
                }
            }

            calDates.appendChild(dateCell);
        }
    }

    renderCalendar(currentMonth, currentYear);
});

document.addEventListener("DOMContentLoaded", function () {
    const followButton = document.querySelector(".u_follow");
    let isFollowed = false;

    followButton.addEventListener("click", function () {
        if (isFollowed) {
            // 원상태로 복귀
            followButton.style.backgroundColor = "rgba(255, 255, 255, 0.1)";
            followButton.style.color = "#b1b1b1";
            followButton.textContent = "팔로우";
        } else {
            // 색상 변경
            followButton.style.backgroundColor = "#ffffff";
            followButton.style.color = "#000000";
            followButton.textContent = "팔로잉";
        }
        isFollowed = !isFollowed; // 상태 토글
    });
});
