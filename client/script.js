
async function getItems() {
    const response = await fetch("http://127.0.0.1:8000/items");
    const items = await response.json();
    return items;
}

async function deleteItem(indexToDelete) {
    // call the endpoint to delete
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
        "number": indexToDelete
    });

    const requestOptions = {
        method: "DELETE",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
    };

    await fetch("http://127.0.0.1:8000/remove", requestOptions);

    // re-render screen

}

async function renderItems() {
    const todoList = document.getElementById('todo-list'); // ul component
    todoList.innerHTML = '';

    const items = await getItems();

    items.map((item, index) => {
        // create bullet point
        const li = document.createElement('li');
        li.textContent = item;
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';

        deleteButton.addEventListener('click', async () => {
            // remove the item
            await deleteItem(index);
            await renderItems();
            // re-render
        })
        li.appendChild(deleteButton);

        todoList.appendChild(li);
    });

    // render to screen
    
}

async function addItem(itemName) {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
        "name": itemName
    });

    const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
    };

    await fetch("http://127.0.0.1:8000/add", requestOptions)
    
}

window.onload = async () => {
    // get request to backend
    await renderItems();

    // button to add elements
    const addButton = document.getElementById('add-btn');
    addButton.addEventListener('click', async () => {
        const newItemInput = document.getElementById('new-item');
        const newItemValue = newItemInput.value;

        await addItem(newItemValue);

        newItemInput.value = '';
        await renderItems();
    })
}
