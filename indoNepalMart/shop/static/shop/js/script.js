window.addEventListener('load', function() {

    let hamburgerMenu = document.getElementById("hamburger-menu");
    let checkbox = document.getElementById("checkbox")
    
    
    hamburgerMenu.addEventListener('click' , ()=>{
        if(checkbox.checked){
            document.getElementById("mid-contents").classList.add("show-side-navigation-menu")
        }else{
            document.getElementById("mid-contents").classList.remove("show-side-navigation-menu")
        }
    })

    setTimeout(()=>{
        if(sessionStorage.getItem("termsOfServiceLoaded") == null){
            document.getElementById("tos-trigger").click()
        }
    
        sessionStorage.setItem("termsOfServiceLoaded" , true)

    } , 1500)

});
