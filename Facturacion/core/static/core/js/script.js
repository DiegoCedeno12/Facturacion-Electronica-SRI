let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
  arrow[i].addEventListener("click", (e)=>{
 let arrowParent = e.target.parentElement.parentElement;//selecting main parent of arrow
 arrowParent.classList.toggle("showMenu");
  });
}

let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", ()=>{
  sidebar.classList.toggle("close");
});

(function(){
  var mostrar_fecha = function (){
    var fecha = new Date();
    var day = fecha.getDay();    
    var month = fecha.getMonth();
    var year = fecha.getFullYear();
    var pday = document.getElementById('dia');
    var pmonth = document.getElementById('mes');
    var pyear = document.getElementById('anio');
    
    pday.textContent = day;
    pmonth.textContent = '0'+ (month + 1);
    pyear.textContent = year;
  };

  mostrar_fecha();
}())
