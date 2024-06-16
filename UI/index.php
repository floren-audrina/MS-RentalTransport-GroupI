<?php
// Set input dari search
$index = 4;
$selectedprovider = $index; 
$selectedCar = $index; 
$withDriver = false; 

// Set input dari review
$star = 8.9;
$totalReviews = 12;
$detailReview = [
    'Ketepatan Waktu Staf (10)',
    'Kebersihan Mobil (9)',
    'Kemudahan Proses Pengambilan & Pengembalian (8)'
];


// Car
$urlCar = 'http://localhost:8000/car/' . $selectedCar;
$chCar = curl_init($urlCar);
curl_setopt($chCar, CURLOPT_RETURNTRANSFER, true);
$responseForCar = curl_exec($chCar);
curl_close($chCar);
$carData = json_decode($responseForCar, true);
if ($carData === null) {
    echo "Failed to retrieve car data.";
    exit;
}
$car = $carData['data'];

// Provider
$urlProvider = 'http://localhost:8000/provider';
$chProvider = curl_init($urlProvider);
curl_setopt($chProvider, CURLOPT_RETURNTRANSFER, true);
$responseForProvider = curl_exec($chProvider);
curl_close($chProvider);
$providerData = json_decode($responseForProvider, true);
if ($providerData === null) {
    echo "Failed to retrieve provider data.";
    exit;
}
$provider = $providerData[0];

// Untuk Kebijakan Rental
$policy = $provider['policy'];
$policy_items = explode(', ', $policy); 

// Untuk Informasi Penting
$information = $provider['information'];
$information_items = explode('. ', $information); 

if($withDriver == true) {
    $driverPrice = 250000;  // Harga Driver Rp.250.000
} else {
    $driverPrice = 0;
}
$carImageUrl = $carData['image'];
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
            <h1><?php echo htmlspecialchars($provider['provider_name']); ?> - <?php echo htmlspecialchars($provider['provider_city']); ?></h1>
        </header>

        <div class="image-and-review">
            <div class="car-image">
                <img src="<?php echo htmlspecialchars($carImageUrl); ?>" alt="Car Image">
            </div>

            <div class="provider-reviews">
                <!-- <img src="path_to_provider_logo.png" alt="Provider Logo"> -->
                <h2>Review</h2>
                <div class="rating">
                    <h3><?php echo htmlspecialchars($star); ?></h3>
                    <p>(<?php echo htmlspecialchars($totalReviews); ?> reviews)</p>
                </div>
                <h4>Yang disukai traveler</h4>
                <ul>
                    <!-- <li>Ketepatan Waktu Staf (10)</li>
                    <li>Kebersihan Mobil (9)</li>
                    <li>Kemudahan Proses Pengambilan & Pengembalian (8)</li> -->
                    <?php foreach ($detailReview as $review): ?>
                    <li><?php echo htmlspecialchars($review); ?></li>
                    <?php endforeach; ?>
                </ul>
                <!-- <p>Review lengkap penyedia ini dapat dilihat via Traveloka App.</p> -->
            </div>
        </div>

        <div class="car-details">
            <div>
                <h2><?php echo htmlspecialchars($car['car_brand']) . ' ' . htmlspecialchars($car['car_name']); ?></h2>
                <p><?php echo htmlspecialchars($car['car_seats']); ?> kursi, <?php echo htmlspecialchars($car['car_luggages']); ?> bagasi</p>
                <p><?php echo htmlspecialchars($car['car_year']); ?> atau setelahnya</p>
                <p><?php echo htmlspecialchars($car['car_transmission']); ?></p>
            </div>
            <div class="car-price">
                <h2>Rp <?php echo number_format(htmlspecialchars($car['car_price']), 0, ',', '.'); ?></h2>
            </div>
        </div>

        <div class="rental-policy">
            <h3>Kebijakan Rental</h3>
            <ul>
                <?php foreach ($policy_items as $item): ?>
                    <li><?php echo htmlspecialchars($item); ?></li>
                <?php endforeach; ?>
            </ul>
        </div>

        <div class="important-info">
            <h3>Informasi Penting</h3>
            <ul>
                <?php foreach ($information_items as $item): ?>
                <li><?php echo htmlspecialchars($item); ?></li>
                <?php endforeach; ?>
            </ul>
        </div>

        <div class="pickup-location">
            <h3>Lokasi Pengambilan</h3>
            <ul>
                <li>Kantor Rental</li>
                <li><?php echo htmlspecialchars($provider['provider_address']); ?></li>
            </ul>
        </div>

        <div class="map">
            <?php echo $provider['map']; ?>
        </div>

        <div class="pickup-location">
            <h3>Harga Total</h3>
            <ul>
                <li>Mobil: Rp. <?php echo number_format(htmlspecialchars($car['car_price']), 0, ',', '.'); ?></li>
                <li>Driver: Rp. <?php echo number_format(htmlspecialchars($driverPrice), 0, ',', '.'); ?></li>
            </ul>
            <div class="car-price">
                <h2>Rp <?php echo number_format(htmlspecialchars($car['car_price'] + $driverPrice), 0, ',', '.'); ?></h2>
            </div>
        </div>

        <a href="#" class="button">Book</a>
    </div>
</body>
</html>
