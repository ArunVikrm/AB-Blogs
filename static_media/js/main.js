// navigation bar

var menuItems = document.getElementById("navitems");
var menu = document.getElementById("menubar").onclick = menuToggle;
       
function menuToggle(){
    menuItems.style.display = "block";
    if(menuItems.style.maxHeight == "0px"){
        menuItems.style.maxHeight = "200px";
    }else{
    menuItems.style.maxHeight = "0px";
    }
}

var topbutton = document.getElementById("topbtn");
var downbutton = document.getElementById("downbtn");
topbutton.addEventListener("click",topBtn,true);
downbutton.addEventListener("click",downBtn,true);
    
function topBtn(){
    topbutton.style.display = "none";
    downbutton.style.display = "inline";
}

function downBtn(){
    topbutton.style.display = "inline";
    downbutton.style.display = "none";
}

// search button

const searchBtn = document.querySelector(".searchbtn");
const cancelBtn = document.querySelector(".cancelbtn");
const searchBox = document.querySelector(".search-box");
const searchInput = document.querySelector("input");

searchBtn.onclick = () =>{
    searchBox.classList.add("active");
    searchInput.classList.add("active");
    searchBtn.classList.add("active");
    cancelBtn.classList.add("active");
}

cancelBtn.onclick = () =>{
    searchBox.classList.remove("active");
    searchInput.classList.remove("active");
    searchBtn.classList.remove("active");
    cancelBtn.classList.remove("active");
    searchInput.value = "";
}

window.onscroll = function() {myFunction()};

var navbar = document.getElementById("head");
var sticky = head.offsetTop;

function myFunction() {
    if (window.pageYOffset >= sticky) {
        head.classList.add("sticky")
    } 
    else {
        head.classList.remove("sticky");
    }
}

// user profile

var userid = document.getElementById("user").onclick = userProfileToggle;
var userprofile = document.querySelector(".usermenu");
function userProfileToggle(){
  userprofile.classList.toggle('active');
}

document.addEventListener("mouseup", function(event) {
var obj = document.getElementById("us");
if (!obj.contains(event.target)) {
  userprofile.classList.remove('active');
  menuItems.style.display = "block";
}
else {
  userprofile.classList.add('active');
}
});

//login

var loginform = document.getElementById("loginform");
    var signupform = document.getElementById("signupform");
    var hrline = document.getElementById("hr-line");

    function login(){
        loginform.style.transform = "translateX(300px)";
        signupform.style.transform = "translateX(300px)";
        hrline.style.transform = "translateX(0)";
    }
    function signup(){
        loginform.style.transform = "translateX(0)";
        signupform.style.transform = "translateX(0)";
        hrline.style.transform = "translateX(100px)";
    }