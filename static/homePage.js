// AUTHOR: HECTOR JIMENEZ MERCADO

let feed = document.getElementById('post-feed');
let postForm = document.getElementById('post-form')

// Mock Data
let user = {
    "username": "GuandaBasket",
    "location": "Quebradillas",
    "tel": "787-371-1132"
}

let posts = [
    {
        "title": "Ayuda pa lavar chavos",
        "tel": "787-243-8293",
        "location": "Fortaleza",
        "provider": "Apex",
        "description": `Buscando gobierno fatulo para la compra de unas prubas de COVID-19 a 38$ cada una
                        pa joder al pueblo y tumbarnos los chavos. Bucamos que se tenga un equipo de salud publica
                        que este totalmente en el bolsillo de ls partidos y que solo den forward y accepten lo que se
                        les pida. `
    },
    {
        "title": "SOS",
        "tel": "932-755-9301",
        "provider": "Julia Hawthorne",
        "location": "Ponce",
        "description": `My house collapsed during recent earthquakes and we are
                        currently living on tents. We would be very greatfull if anyone
                        would let us crashed anywahere with a roof. PLEASE SEND HELP.`
    },
    {
        "title": "HELP",
        "tel": "787-723-8240",
        "provider": "Franklin Santana",
        "location": "San Juan",
        "description": `Theese past few weeks have been excruciating! Me and my comunity have
                        no contact with the outside world unitil now and no transportation is doable
                        because of all the collapses. Los Santos community is seeking help
                        please bring any type of food you can gather ASAP. PEOPLE ARE DYING HERE`
    },
]

function load() {
    document.getElementById('header-register').innerHTML += user.username;
    loadPosts();
}


function loadPosts() {
    for(let post of posts){
        let newPost = document.createElement('div');
        newPost.className = "post";

        newPost.innerHTML =
            createPost(post.provider, post.title, post.tel, post.description, post.location);

        feed.appendChild(newPost);
    }
}

function submitPost(){
    let newPost = {
        "title": postForm.resource.value,
        "location": postForm.location.value,
        "description": postForm.description.value,
        "provider": user.username,
        "tel": user.tel,
    }

    console.log(newPost)

    let newPostElement = document.createElement('div');
    newPostElement.className = "post";

    newPostElement.innerHTML =
        createPost(newPost.provider, newPost.title,
            newPost.tel, newPost.description, newPost.location);

    feed.appendChild(newPostElement);

}

function createPost(username, title, phoneNumber, description, location){
    return `
    <div id = "post-header"><h2>${username}</h2></div>
    <h1 style="color:#2C97FA; text-shadow: 1px 1px 4px black;">${title}</h1>
    <p>${phoneNumber}</p><hr>
    <p id="paragraph">${description}</p>
    <p id="post-location">Location: ${location}</p>`
}
