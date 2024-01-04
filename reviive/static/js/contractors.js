
$(document).ready(function(){
    // Upvote functionality
    $('div.news-pts button.upvote').click(function(){
        var scoreDiv = $(this).siblings('div.score');
        var scoreNum = parseInt(scoreDiv.text());
        scoreNum++; // Increment the score

        console.log("Upvote to: " + scoreNum); // Log the new score

        scoreDiv.text(scoreNum); // Update the score display

        // Show a temporary success message for upvote
        var successMsg = $('<p class="vote-success">Upvote successful!</p>');
        successMsg.appendTo($(this).parent()).fadeOut(2000, function(){
            $(this).remove(); // Remove the message after fading out
        });
    });

    // Downvote functionality
    $('div.news-pts button.downvote').click(function(){
        var scoreDiv = $(this).siblings('div.score');
        var scoreNum = parseInt(scoreDiv.text());

        if(scoreNum > 0) {
            scoreNum--; // Decrement the score
            console.log("Downvote to: " + scoreNum); // Log the new score

            scoreDiv.text(scoreNum); // Update the score display

            // Show a temporary success message for downvote
            var successMsg = $('<p class="vote-success">Downvote successful!</p>');
            successMsg.appendTo($(this).parent()).fadeOut(2000, function(){
                $(this).remove(); // Remove the message after fading out
            });
        } else {
            // Optionally handle the case where the score can't go below zero
            console.log("Cannot downvote below zero."); // Log the error
            var errorMsg = $('<p class="vote-error">Cannot downvote below zero.</p>');
            errorMsg.appendTo($(this).parent()).fadeOut(2000, function(){
                $(this).remove(); // Remove the message after fading out
            });
        }
    });
});
