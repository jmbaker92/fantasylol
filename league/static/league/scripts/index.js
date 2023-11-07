
function selectPlayer(playerId) {
    var playerElement = document.getElementById(playerId);
    console.log(playerElement);
    var selectedPlayerList = document.getElementById('selectedplayers');
    if (!playerElement || !selectedPlayerList) {
        throw new Error("Couldn't find selected player")
    }
    var button = playerElement.querySelector('button');
    function handleClick() {
        removePlayer(playerId)
    }
    button.addEventListener('click', handleClick)
    button.textContent = "remove";
    selectedPlayerList.appendChild(playerElement)
}

function removePlayer(playerId) {
    var playerElement = document.getElementById(playerId);
    console.log(playerElement);
    var draftPlayerList = document.getElementById('draftlist');
    if (!playerElement || !draftPlayerList) {
        throw new Error("Couldn't find selected player")
    }
    var button = playerElement.querySelector('button');
    function handleClick() {
        selectPlayer(playerId)
    }
    button.addEventListener('click', handleClick)
    button.textContent = "Draft";
    draftPlayerList.prepend(playerElement)
}

function handleDraftSubmit(playerId) {
    const selectedPlayerIDs = [];

    var selectedPlayerList = document.getElementById('selectedplayers');
    if (!selectedPlayerList) {
        throw new Error("Couldn't find selected player");
    }
    var playerElements = selectedPlayerList.querySelectorAll('.player');
    playerElements.forEach(player => {
        const playerId = parseInt(player.id);
        selectedPlayerIDs.push(playerId);
    });
    console.log("Selected Player IDs:", selectedPlayerIDs);

    const data = {
        selectedPlayerIDs: selectedPlayerIDs
    };

    fetch('/api/draft-players/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            if (response.ok) {
                // Handle success, e.g., show a success message.
                console.log('Players added to the team successfully');
            } else {
                // Handle the error, e.g., show an error message.
                console.error('Failed to add players to the team');
            }
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });

}

const submitButton = document.getElementById('submit-button');
submitButton.addEventListener('click', handleDraftSubmit);