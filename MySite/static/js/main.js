function login_popup(){
    console.log(document.getElementById('login').style.display)
    if (document.getElementById('login').style.display == 'none'){
        document.getElementById('login').style.display = 'block';
    }
    if (document.getElementById('signup').style.display == 'block'){
        document.getElementById('signup').style.display = 'none';
    }   
}

function signup_popup(){
    if (document.getElementById('signup').style.display == 'none'){
        document.getElementById('signup').style.display = 'block';
    }
    if (document.getElementById('login').style.display == 'block'){
        document.getElementById('login').style.display = 'none';
    }
}

function close_sl_forms(){
    if (document.getElementById('login').style.display == 'block'){
        document.getElementById('login').style.display = 'none';
    }
    if (document.getElementById('signup').style.display == 'block'){
        document.getElementById('signup').style.display = 'none';
    }
}