<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .sidebar {
            height: 100%;
            width: 250px;
            position: fixed;
            top: 0;
            left: 0;
            background-color: #1f1f2e;
            padding-top: 20px;
        }

        .sidebar-title {
            color: white;
            text-align: center;
        }

        .sidebar h2 {
            color: white;
            padding: 8px;
            padding-top: 20px;
        }

        .sidebar ul {
            list-style-type: none;
            padding: 0;
        }

        .sidebar ul li {
            padding: 8px;
        }

        .sidebar ul li a {
            color: white;
            text-decoration: none;
            display: block;
        }

        .sidebar ul li a:hover {
            background-color: #555;
        }

        .content {
            margin-left: 250px;
            padding: 20px;
        }

        .response {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 5px;
            margin-top: 20px;
        }

        .response pre {
            white-space: pre-wrap;
        }
    </style>
    <script>
        function promptForId(action) {
            var id = prompt("Please enter the ID:");
            if (id != null && id != "") {
                window.location.href = "?action=" + action + "&id=" + id;
            }
        }
    </script>
</head>
<body>
    <div class="sidebar">
        <h1 class="sidebar-title">Dashboard</h1>
        <ul>
            <h2>Car</h2>
            <li><a href="?action=get_car">Get Car</a></li>
            <li><a href="javascript:void(0);" onclick="promptForId('get_car_by_id')">Get Car (By ID)</a></li>
            <li><a href="?action=add_car">Add Car</a></li>

            <h2>Driver</h2>
            <li><a href="?action=get_driver">Get Driver</a></li>
            <li><a href="javascript:void(0);" onclick="promptForId('get_driver_by_id')">Get Driver (By ID)</a></li>
            <li><a href="?action=add_driver">Add Driver</a></li>

            <h2>Provider</h2>
            <li><a href="?action=get_provider">Get Provider</a></li>
            <li><a href="javascript:void(0);" onclick="promptForId('get_provider_by_id')">Get Provider (By ID)</a></li>
            <li><a href="?action=add_provider">Add Provider</a></li>
        </ul>
    </div>

    <div class="content">
        <?php
            function fetch_data($url) {
                $response = file_get_contents($url);
                return json_decode($response, true);
            }

            function display_json($data) {
                if($data != null) {
                    echo "<div class='response'><pre>" . json_encode($data, JSON_PRETTY_PRINT) . "</pre></div>";
                } else {
                    echo "<div class='response'>No data found</div>";
                }
            }

            if (isset($_GET['action'])) {
                $action = $_GET['action'];
                $id = isset($_GET['id']) ? $_GET['id'] : null;
                $base_url = 'http://localhost:8000';

                switch ($action) {
                    case 'get_car':
                        $url = "$base_url/car";
                        $data = fetch_data($url);
                        display_json($data);
                        break;
                    case 'get_car_by_id':
                        if ($id) {
                            $url = "$base_url/car/$id";
                            $data = fetch_data($url);
                            display_json($data);
                        } else {
                            echo "<script>alert('Please provide a car ID.');</script>";
                        }
                        break;
                    case 'add_car':
                        echo "<p>Add Car functionality to be implemented.</p>";
                        break;
                    case 'get_driver':
                        $url = "$base_url/driver";
                        $data = fetch_data($url);
                        display_json($data);
                        break;
                    case 'get_driver_by_id':
                        if ($id) {
                            $url = "$base_url/driver/$id";
                            $data = fetch_data($url);
                            display_json($data);
                        } else {
                            echo "<script>alert('Please provide a driver ID.');</script>";
                        }
                        break;
                    case 'add_driver':
                        echo "<p>Add Driver functionality to be implemented.</p>";
                        break;
                    case 'get_provider':
                        $url = "$base_url/provider";
                        $data = fetch_data($url);
                        display_json($data);
                        break;
                    case 'get_provider_by_id':
                        if ($id) {
                            $url = "$base_url/provider/$id";
                            $data = fetch_data($url);
                            display_json($data);
                        } else {
                            echo "<script>alert('Please provide a provider ID.');</script>";
                        }
                        break;
                    case 'add_provider':
                        echo "<p>Add Provider functionality to be implemented.</p>";
                        break;
                    default:
                        echo "<p>Invalid action.</p>";
                        break;
                }
            } else {
                echo "<p>Select an action from the menu.</p>";
            }
        ?>
    </div>
</body>
</html>
