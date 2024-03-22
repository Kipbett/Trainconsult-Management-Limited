const myOption = document.getElementById("id_attendance_mode");
const mySchool = document.getElementById("student_school");
const myOrg = document.getElementById("organization");
myOption.addEventListener("change", function() {
    if (myOption.value === "student") {
        mySchool.style.display = "flex";
        myOrg.style.display = "none";
    } else {
        myOrg.style.display = "flex";
        mySchool.style.display = "none";
    }
});