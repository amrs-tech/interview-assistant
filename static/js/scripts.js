$(document).ready(function() {
    $('#chat-form').on('submit', function(event) {
        event.preventDefault();

        let userMessage = $('#user-input').val();
        if (userMessage.trim() === '') {
            return;
        }

        $('#chat-box').append('<div class="user-message mb-2"><strong>You:</strong> ' + userMessage + '</div>');
        $('#user-input').val('');

        $.ajax({
            type: 'POST',
            url: '/get_response',
            contentType: 'application/json',
            data: JSON.stringify({ message: userMessage }),
            success: function(response) {
                $('#chat-box').append('<div class="bot-response mb-2"><strong>Bot:</strong> ' + response.response + '</div>');
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            },
            error: function() {
                $('#chat-box').append('<div class="bot-response mb-2"><strong>Bot:</strong> Sorry, something went wrong!</div>');
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            }
        });
    });
});
