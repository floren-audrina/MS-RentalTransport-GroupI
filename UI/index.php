<?php
// Car
$urlCar = 'http://localhost:8000/car';
$chCar = curl_init($urlCar);
curl_setopt($chCar, CURLOPT_RETURNTRANSFER, true);
$responseForCar = curl_exec($chCar);
curl_close($chCar);

// Decode JSON responseForCar
$carData = json_decode($responseForCar, true);
if ($carData === null) {
    echo "Failed to retrieve car data.";
    exit;
}
$cars = $carData['data'];

// // Provider
// $urlProvider = 'http://localhost:8000/provider';
// $chProvider = curl_init($urlProvider);
// curl_setopt($chProvider, CURLOPT_RETURNTRANSFER, true);
// $responseForProvider = curl_exec($chProvider);
// curl_close($chProvider);

// // Decode JSON responseForProvider
// $providerData = json_decode($responseForProvider, true);
// if ($providerData === null) {
//     echo "Failed to retrieve provider data.";
//     exit;
// }
// $providers = $providerData['data'];



// Set input dari search and review
$carIndex = 4; 
// $providerIndex = 4;
$withDriver = false; 

if($withDriver == true) {
    $driverPrice = 250000;  // Harga Driver Rp.250.000
} else {
    $driverPrice = 0;
}

$car = $cars[$carIndex];
$carImageUrl = $carData['image'];
// $provider = $providers[$providerIndex];


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
        <h1>Jayamahe Easy Ride Surabaya</h1>
        <!-- <h1><?php //echo htmlspecialchars($provider['provider_name']); ?></h1> -->
        <!-- <p>Surabaya - Mon, 10 Jun 2024 09:00 - Wed, 12 Jun 2024 09:00</p> -->
    </header>
        <div class="car-image">
            <img src="<?php echo htmlspecialchars($carImageUrl[$carIndex]); ?>" alt="Car Image">
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
                <li>Penggunaan dari 00:00 hingga 23:59 per hari, hanya penggunaan di area Surabaya, Gresik, Sidoarjo, Lamongan, Mojokerto, Malang, Pasuruan, dan Probolinggo.</li>
                <li>Apabila penggunaan melebihi wilayah di atas pengemudi akan dikenakan biaya tambahan, silahkan membayar dan konfirmasi langsung kepada penyedia untuk informasi lebih lanjut.</li>
                <li>Kembalikan bensin seperti semula</li>
                <li>Penuh ke penuh</li>
                <li>Layanan darurat 24 jam</li>
                <li>Customer Service Traveloka 24 jam</li>
            </ul>
        </div>

        <div class="important-info">
            <h3>Informasi Penting</h3>
            <ul>
                <li>Sebelum Anda pesan</li>
                <li>Pastikan untuk membaca syarat rental.</li>
                <li>Setelah Anda pesan</li>
                <li>Penyedia akan menghubungi pengemudi melalui WhatsApp untuk meminta foto beberapa dokumen wajib.</li>
                <li>Saat pengambilan</li>
                <li>Bawa KTP, SIM A, dan dokumen-dokumen lain yang dibutuhkan oleh penyedia rental.</li>
                <li>Saat Anda bertemu dengan staf rental, cek kondisi mobil dengan staf.</li>
                <li>Setelah itu, baca dan tanda tangani perjanjian rental.</li>
            </ul>
        </div>

        <div class="pickup-location">
            <h3>Lokasi Pengambilan (Kantor <?php //echo htmlspecialchars($provider['provider_location']); ?>)</h3>
            <ul>
                <li>Kantor Rental: Gratis</li>
                <li>Lokasi Lainnya: Dapat dikenakan biaya tambahan</li>
            </ul>
        </div>

        <div class="map">
            <!-- <img src="map-placeholder.png" alt="Map Placeholder"> -->
            <div class="mapouter"><div class="gmap_canvas"><iframe width="820" height="560" id="gmap_canvas" src="https://maps.google.com/maps?q=636+5th+Ave%2C+New+York&t=&z=13&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://textcaseconvert.com/"></a><br><a href="https://timenowin.net/"></a><br><style>.mapouter{position: relative;text-align: right;height: 560px;width: 820px;}</style><a href="https://www.mapembed.net">create map in google</a><style>.gmap_canvas{overflow: hidden;background: none !important;height: 560px;width: 820px;}</style></div></div>
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
