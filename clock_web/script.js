let hh = document.getElementById("hour");
let mm = document.getElementById("minute");
let ss = document.getElementById("second");

function DisplayTime(){
  let date = new Date();
  let h = date.getHours();
  let m = date.getMinutes();
  let s = date.getSeconds();
  let hhrotation = 30 * h + m / 2;
  let mmrotation = 6 * m;
  let ssrotation = 6 * s;

  hh.style.transform = `rotate(${hhrotation}deg)`;
  mm.style.transform = `rotate(${mmrotation}deg)`;
  ss.style.transform = `rotate(${ssrotation}deg)`;
}
setInterval(DisplayTime, 1000);
let TodayDate = new Date();
today = TodayDate.getDate();
tomonth = TodayDate.getMonth()+1;
toyear = TodayDate.getFullYear();
document.getElementById("date").innerHTML = `${today} : ${tomonth} : ${toyear}`;
