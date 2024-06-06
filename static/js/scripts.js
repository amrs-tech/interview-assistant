document.addEventListener('DOMContentLoaded', function () {
    const messageInput = document.getElementById('messageInput');
    const sendMessage = document.getElementById('sendMessage');
    const chatboxBody = document.getElementById('chatbox-body');

    sendMessage.addEventListener('click', function () {
        const userMessage = messageInput.value.trim();
        if (userMessage) {
            addMessage(userMessage, 'user');
            messageInput.value = '';

            fetch('/get_response', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userMessage }),
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data.response, 'assistant');
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });

    function addMessage(text, sender) {
        const message = document.createElement('div');
        message.classList.add('message', sender);
        const messageBubble = document.createElement('div');
        messageBubble.classList.add('message-bubble');
        messageBubble.innerHTML = text;
        message.appendChild(messageBubble);
        chatboxBody.appendChild(message);
        chatboxBody.scrollTop = chatboxBody.scrollHeight;
    }
});
