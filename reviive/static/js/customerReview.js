// Add 'move-down' and 'move-up' classes to the '.contractor-profile' element
$(document).ready(function() {
    console.log("Document ready");
    const contractorProfile = document.querySelector('.contractor-profile');
    console.log("Contractor profile element:", contractorProfile);
    if (contractorProfile) {
        contractorProfile.classList.add('move-down');
        contractorProfile.classList.add('move-up');
    }
});


$(document).ready(function() {
    // Initialize the average rating
    updateAverageRating();

    // Handle click event on "Submit Review" button
    $("#submit-review").click(function() {
      const rating = $("#rating").val();
      const reviewText = $("#review").val();
      if (rating && reviewText) {
        addReview(rating, reviewText);
        updateAverageRating();
      }
    });

    function addReview(rating, reviewText) {
      // Create a new review element
      const $review = $("<div>", {
        class: "review",
      });
      $review.html(`<p><strong>Rating:</strong> ${rating} Star(s)</p><p><strong>Review:</strong> ${reviewText}</p>`);
      $(".reviews").append($review);
    }

    function updateAverageRating() {
      // Calculate and update the average rating
      const totalRatings = $(".star").length;
      let sumOfRatings = 0;
      $(".star").each(function() {
        sumOfRatings += $(this).hasClass("rated") ? 1 : 0;
      });
      const averageRating = totalRatings > 0 ? (sumOfRatings / totalRatings).toFixed(1) : 0;
      $(".rating-value").text(averageRating);
    }

    // Handle click event on star ratings
    $(".star").click(function() {
      $(this).toggleClass("rated");
      updateAverageRating();
    });
  });
