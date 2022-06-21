p_name = document.querySelector('#p_name');
p_username = document.querySelector('#p_username');
p_email = document.querySelector('#p_email');
p_password = document.querySelector('#p_password');
next = document.querySelector('.next');
msg = document.getElementById('msg');
fname = document.getElementById('fname');
lname = document.getElementById('lname');
username = document.getElementById('username');
email = document.getElementById('email');
password = document.getElementById('password');
re_password = document.getElementById('re_password');

const checkPw = () => {
    if (re_password.value != password.value) {
        msg.innerHTML = 'Password Tidak Sesuai';
    } else {
        document.getElementsByName('fname').value = fname.value;
        document.getElementsByName('lname').value = lname.value;
        document.getElementsByName('username').value = username.value;
        document.getElementsByName('email').value = email.value;
        document.getElementsByName('password').value = password.value;
        document.getElementById('done').setAttribute('onclick', 'sendData()');
    }
};

const slide1 = () => {
    if (
        Math.round(parseFloat(getComputedStyle(p_name).top)) == p_name.offsetTop
    ) {
        p_name.style.top = '-396px';
        p_username.style.top = '396px';
        p_username.style.position = 'absolute';
    }
};

const slide2 = () => {
    if (
        Math.round(parseFloat(getComputedStyle(p_username).top)) ==
        p_username.offsetTop
    ) {
        p_username.style.top = '-396px';
        p_email.style.top = '396px';
        p_email.style.position = 'absolute';
    }
};

const slide3 = () => {
    if (
        Math.round(parseFloat(getComputedStyle(p_email).top)) ==
        p_email.offsetTop
    ) {
        p_email.style.top = '-396px';
        p_password.style.top = '396px';
        p_password.style.position = 'absolute';
    }
};

const onBack = () => {
    if (getComputedStyle(p_username).top == '396px') {
        p_username.style.top = '1092px';
        p_name.style.top = '396px';
        p_name.style.position = 'absolute';
    }
    if (getComputedStyle(p_email).top == '396px') {
        p_email.style.top = '1092px';
        p_username.style.top = '396px';
        p_username.style.position = 'absolute';
    }
    if (getComputedStyle(p_password).top == '396px') {
        p_password.style.top = '1092px';
        p_email.style.top = '396px';
        p_email.style.position = 'absolute';
    }
};

document.body.addEventListener('keypress', (e) => {
    if (e.key == 'Enter') {
        enterFunc();
    }
});

const sendData = async () => {
    console.log(`${location.protocol}: // ${location.hostname}`);
    await $.ajax({
        type: 'POST',
        url: '/register',
        data: {
            fname: document.getElementsByName('fname').value,
            lname: document.getElementsByName('lname').value,
            email: document.getElementsByName('email').value,
            username: document.getElementsByName('username').value,
            password: document.getElementsByName('password').value,
        },
        success: function () {
            console.log('masuk');
        },
    });
};

var p_name,
    p_username,
    next,
    p_email,
    p_password,
    password,
    re_password,
    fname,
    lname,
    username,
    email;
