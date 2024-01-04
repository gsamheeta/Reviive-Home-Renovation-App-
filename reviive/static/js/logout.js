$(document).ready(function () {
    $('.container').on('click', '.delete-profile', function () {
      // Delete Profile button clicked
      const confirmation = confirm('Are you sure you want to delete your profile? This action cannot be undone.');
      if (confirmation) {
        alert('Profile deleted successfully');
        window.location.href = "{% url 'reviive_story_list:list' %}";
      }
    });

    $('.container').on('click', '.save-button', function () {
      // Save Changes button clicked
      alert('Profile has been updated');
      window.location.href = "{% url 'reviive_story_list:list' %}";
    });
  });