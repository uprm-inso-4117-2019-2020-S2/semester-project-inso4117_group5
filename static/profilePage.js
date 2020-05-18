let username = "John Marston";
let pendingTickets = document.getElementById('pending-ticket-container');
let acceptedTickets = document.getElementById('accepted-ticket-container')

let tickets = 7;

function load() {
    document.getElementById("header-register").innerHTML += username;
    
    loadAcceptedTickets();
}

function loadPendingTickets() {
    for(let i=0; i<tickets; i++){
        console.log(i);
        let ticket = document.createElement("div");
        ticket.id = 'ticket';
        
        pendingTickets.appendChild(ticket);
    }
}

function loadAcceptedTickets(){
    for(let i=0; i<tickets-3; i++){
        console.log(i);
        let ticket = document.createElement("div");
        ticket.id = 'ticket';
        ticket.innerHTML = `                <h3 style="color: whitesmoke;">Beerbongs</h3>
        <p>Location: San Juan</p>
        <p style="color: red;">Quantity: x13</p>
        <p>Provider: Ben Stiller</p>`

        acceptedTickets.appendChild(ticket);
    }
}