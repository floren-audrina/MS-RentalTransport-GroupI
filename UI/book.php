<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Here you would typically handle the booking process,
    // such as saving the booking details in a database.
    // For this example, we simply display a confirmation message.
    echo "Booking successful!";
} else {
    echo "Invalid request method.";
}
?>
