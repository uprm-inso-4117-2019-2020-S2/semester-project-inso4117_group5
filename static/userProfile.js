let pendingTickets = [
    {
        "location": "Quebradillas",
        "description": "I'm in need of first aid supplies and pottery.",
        "quantity": 12
    },
    {
        "location": "Ponce",
        "description": "Water, ",
        "quantity": 7
    },
    {
        "location": "Quebradillas",
        "description": "I'm in need of first aid supplies and pottery.",
        "quantity": 12
    },
    {
        "location": "Quebradillas",
        "description": "I'm in need of first aid supplies and pottery.",
        "quantity": 12
    },
    {
        "location": "Quebradillas",
        "description": "I'm in need of first aid supplies and pottery.",
        "quantity": 12
    },
    {
        "location": "Quebradillas",
        "description": "I'm in need of first aid supplies and pottery.",
        "quantity": 12
    },
]

function load() {
    let requestContainer = document.getElementById('pending-requests')
    for(let i=0; i<pendingTickets.length; i++){
        let ticket = document.createElement();
        ticket.innerHTML = "<h1>Hello</h1>"
        requestContainer.appendChild(ticket)
    }
}
