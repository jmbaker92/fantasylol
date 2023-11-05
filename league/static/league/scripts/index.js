
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