document.addEventListener('DOMContentLoaded', function () {
    const ratingForm = document.getElementById('ratingForm');
    const ratingInputs = ratingForm.querySelectorAll('input[name="rating"]');

    ratingInputs.forEach(input => {
        input.addEventListener('change', function () {
            const formData = new FormData(ratingForm);

            fetch(ratingForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
                .then(response => response.json())
                .then(data => {
                    const totalRatingElement = document.getElementById('avg_rat');
                    const userRatingElement = document.getElementById('user_rat');

                    totalRatingElement.innerHTML = `Average Rating: ${data.total_rating.toFixed(1)} (${data.rating_count} ratings)`;
                    userRatingElement.innerHTML = `Your Rating: ${data.user_rating}`;
                })
                .catch(error => console.error('Error:', error));
        });
    });
});