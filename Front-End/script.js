const container = document.getElementById('container');
const allPosts = [];

class post {
    constructor(user, message, messageHeader) {
        this.message = message;
        this.messageHeader = messageHeader;
        this.user = user;
    }
}

//Function called after button to create post is pressed
function getInputValue(){
    const message = document.getElementById("message").value;
    const messageHeader = document.getElementById("messageHeader").value;
    const user = {
        name: "Luis",
        lastName: "Acevedo",
        username: "LuisitoLuis"
    }

    //Clear name input field
    document.getElementById("message").value = "";
    document.getElementById("messageHeader").value = "";

    //Check if Name for the bot was provided
    if(messageHeader.length === 0){
        alert("Please Provide A Message Title For The Post");
        return 0;
    }

    //Instantiate new post
    const newPost = new post(user, message, messageHeader);
    allPosts.push(newPost);

    showPost(newPost);
}

// Shows the post with all the information inside a card
function showPost(post){
    const card = document.createElement('div');
    card.classList = 'card gedf-card';
    // Construct post
    const content = `
    <div class="card-header">
        <div class="d-flex justify-content-between align-items-center">
            <div class="d-flex justify-content-between align-items-center">
                <div class="mr-2">
                    <img class="rounded-circle" width="45" src="https://picsum.photos/50/50" alt="">
                </div>
                <div class="ml-2">
                    <div class="h5 m-0">@${post.user.username}</div>
                    <div class="h7 text-muted">${post.user.name} ${post.user.lastName}</div>
                </div>
            </div>
            <div>
                <div class="dropdown">
                    <button class="btn btn-link dropdown-toggle" type="button" id="gedf-drop1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i class="fa fa-ellipsis-h"></i>
                    </button>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="gedf-drop1">
                        <div class="h6 dropdown-header">Configuration</div>
                        <a class="dropdown-item" href="#">Save</a>
                    </div>
                </div>
            </div>
        </div>

    </div>
    <div class="card-body">
        <div class="text-muted h7 mb-2"> <i class="fa fa-clock-o"></i>10 min ago</div>
        <a class="card-link" href="#">
            <h5 class="card-title">${post.messageHeader}</h5>
        </a>

        <p class="card-text">
        ${post.message}
        </p>
    </div>
    <div class="card-footer" style="margin-bottom: 20px;">
        <a href="#" class="card-link"><i class="fa fa-comment"></i> Show support</a>
        <a href="#" class="card-link"><i class="fa fa-mail-forward"></i> Coordinate</a>
    </div>
        `;

    // Append newyly created Post to the container 
    container.innerHTML += content;
}