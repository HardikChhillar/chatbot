const chatInput = document.getElementById('chat-input');
const chatButton = document.getElementById('chat-button');
const chatWindow = document.getElementById('chat-window');

chatButton.addEventListener('click', async () => {
    const userMessage = chatInput.value;
    if (!userMessage) return;

    appendMessage('You: ' + userMessage);
    chatInput.value = '';

    const response = await sendMessageToServer(userMessage);
    appendMessage('Bot: ' + response);
});

async function sendMessageToServer(message) {
    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    });

    if (!response.ok) {
        console.error('Error sending message:', response.statusText);
        return 'Sorry, there was an error. Please try again.';
    }

    const data = await response.json();
    return data.reply;
}

function appendMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}