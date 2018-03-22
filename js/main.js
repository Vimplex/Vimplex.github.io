
function Login_form(){
    console.log(document.getElementById('login').style.display);
    if(document.getElementById('log').style.display == 'none'){
        document.getElementById('log').style.display = 'block';
    }
    else{
        document.getElementById('log').style.display = 'none';
    }
}