<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
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
            background-color: #111;
            padding-top: 20px;
        }

        .sidebar h2 {
            color: white;
            text-align: center;
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
</head>
<body>
    <div class="sidebar">
        <h2>Admin Dashboard</h2>
        <ul>
            <li><a href="?action=get_car">Get Car</a></li>
            <li><a href="?action=get_driver">Get Driver</a></li>
            <li><a href="?action=get_provider">Get Provider</a></li>
        </ul>
    </div>

    <div class="content">
        <?php
            if (isset($_GET['action'])) {
                $action = $_GET['action'];

                // Fetch data based on action
                switch ($action) {
                    case 'get_car':
                        $url = 'http://localhost:8000/car';
                        break;
                    case 'get_driver':
                        $url = 'http://localhost:8000/driver';
                        break;
                    case 'get_provider':
                        $url = 'http://localhost:8000/provider';
                        break;
                    default:
                        $url = '';
                        break;
                }

                if ($url) {
                    // Fetch data from API or service
                    $response = file_get_contents($url);
                    $data = json_decode($response);

                    // Convert data to formatted JSON string
                    $jsonData = json_encode($data, JSON_PRETTY_PRINT);

                    // Output JSON string
                    echo "<pre>$jsonData</pre>";
                } else {
                    echo "<p>Invalid action.</p>";
                }
            } else {
                echo "<p>Select an action from the menu.</p>";
            }
        ?>
    </div>
</body>
</html>
