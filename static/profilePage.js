// AUTHOR: HECTOR JIMENEZ MERCADO

let username = "John Marston";
let pendingTicketsContainer = document.getElementById('pending-ticket-container');
let acceptedTicketsContainer = document.getElementById('accepted-ticket-container')

// Mock Data
var pendingTickets =  
[
    {
        "title": "Water",
        "location": "San Juan",
        "quantity": 21,
        "provider": "John Balbuena"
    }, 

    {
        "title": "Rice",
        "location": "Arecibo",
        "quantity": 10,
        "provider": "Maria Magdalena"
    },

    {
        "title": "Pottery",
        "location": "Mayaguez",
        "quantity": 7,
        "provider": "Beatrice Muniz"
    },

    {
        "title": "First Aid Kits",
        "location": "Quebradillas",
        "quantity": 20,
        "provider": "Heriberto Velez"
    },

    {
        "title": "Mano de Obra",
        "location": "Jayuya",
        "quantity": null,
        "provider": "Jose Delgado"
    },

    {
        "title": "Water",
        "location": "San Juan",
        "quantity": 21,
        "provider": "John Balbuena"
    }
];

var acceptedTickets = [
    {
        "title": "Mano de Obra",
        "location": "Jayuya",
        "quantity": null,
        "provider": "Jose Delgado"
    },

    {
        "title": "Pottery",
        "location": "Mayaguez",
        "quantity": 7,
        "provider": "Beatrice Muniz"
    },

    {
        "title": "Water",
        "location": "San Juan",
        "quantity": 21,
        "provider": "John Balbuena"
    }, 
    
]

function load() {
    document.getElementById("header-register").innerHTML += username;
    loadPendingTickets();
    loadAcceptedTickets();
}

function loadPendingTickets() {
    for(let ticket of pendingTickets){
        let newTicket = document.createElement("div");
        newTicket.id = 'ticket';
        newTicket.className = "fadeInDown"

        newTicket.innerHTML= 
            createTicket(ticket.title, ticket.location, ticket.quantity, ticket.provider)

        pendingTicketsContainer.appendChild(newTicket);
    }
}

function loadAcceptedTickets(){
    for(let ticket of acceptedTickets){
        let newTicket = document.createElement("div");
        newTicket.id = 'ticket';
        newTicket.className = "fadeInDown"

        newTicket.innerHTML = 
            createTicket(ticket.title, ticket.location, ticket.quantity, ticket.provider)

        acceptedTicketsContainer.appendChild(newTicket);
    }
}

function createTicket(title, location, quantity, provider) {    
    return `                
    <h4 style="color: whitesmoke;">${title}</h4>
    <p>Location: ${location}</p>
    <p style="color: red;">Quantity: x${quantity}</p>
    <p>Provider: ${provider}</p>`
}