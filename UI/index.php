<?php
// URL endpoint untuk service get
$url = 'http://localhost:8000/car'; // Sesuaikan dengan endpoint service Anda

// Buat cURL request untuk memanggil service
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

// Decode JSON response
$carData = json_decode($response, true);

// Periksa apakah data berhasil diambil
if ($carData === null) {
    echo "Failed to retrieve car data.";
    exit;
}

// Ambil detail mobil dari data JSON
$car = $carData[1]; // Asumsikan kita ambil data mobil pertama
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Rental</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div class="container">
        <header>
            <h1>Car Rental Without Driver</h1>
            <p>Surabaya - Mon, 10 Jun 2024 09:00 - Wed, 12 Jun 2024 09:00</p>
        </header>
        <div class="car-details">
            <img src="car_image.png" alt="Car Image" class="car-image">
            <div class="car-info">
            <!-- <div class="mapouter"><div class="gmap_canvas"><iframe width="820" height="560" id="gmap_canvas" src="https://maps.google.com/maps?q=636+5th+Ave%2C+New+York&t=&z=13&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://textcaseconvert.com/"></a><br><a href="https://timenowin.net/"></a><br><style>.mapouter{position: relative;text-align: right;height: 560px;width: 820px;}</style><a href="https://www.mapembed.net">create map in google</a><style>.gmap_canvas{overflow: hidden;background: none !important;height: 560px;width: 820px;}</style></div></div> -->
                <h2>
                    <?php echo htmlspecialchars($car['car_name']); ?>
                </h2>
                <p>Provided by
                    <?php echo htmlspecialchars($car['car_provider']); ?>
                </p>
                <ul>
                    <li>
                        <?php echo htmlspecialchars($car['car_seats']); ?> seats
                    </li>
                    <li>
                        <?php echo htmlspecialchars($car['car_luggages']); ?> bags
                    </li>
                    <li>Automatic</li>
                    <li>Year
                        <?php echo htmlspecialchars($car['car_year']); ?>
                    </li>
                </ul>
                <div class="features">
                    <span>Insurance</span>
                    <span>No Refundable Deposit</span>
                    <span>Easy Verification</span>
                </div>
                <h3>Rental Policies</h3>
                <ul>
                    <li>Return with the same fuel level</li>
                    <li>24 hours usage per day</li>
                </ul>
                <h3>Easy Verification</h3>
                <p>Driver only needs to share a photo of the driver's license and ID card.</p>
            </div>
        </div>
        <div class="pricing">
            <h2>Total Price</h2>
            <p>Rp
                <?php echo number_format($car['car_price']); ?>
            </p>
            <button onclick="window.location.href='book.php'">Continue</button>
        </div>
        <div class="pickup-location">
            <h3>Pickup Location</h3>
            <p>
                <?php echo htmlspecialchars($car['location']); ?>
            </p>
            <div id="map"></div>
        </div>
    </div>
    <script>
        // You can add your map initialization code here if you use any map service like Google Maps
    </script>
</body>

</html>