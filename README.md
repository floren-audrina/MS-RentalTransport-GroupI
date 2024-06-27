# MS-RentalTransport-GroupI

 KALAU MAU MENCOBA, GUNAKAN PORT 8001

    path :
        GET:
            car '/car'
                '/car/<int:car_id>'
                '/available_cars/<string:tanggal_mulai>/<string:tanggal_selesai>'

            driver  '/driver'
                    '/driver/<int:driver_id>'

            booking '/booking'
                    '/booking/<int:booking_id>'
                    '/booking/check/<int:booking_id>'

            provider '/provider'

        POST:
            '/car_add'
            '/driver_add'
            '/booking_add'

        PUT:
            '/car_edit'
            '/driver_edit'
            '/booking_edit'
            '/provider_edit'

        DELETE:
            '/car_delete/<int:car_id>'
            '/driver_delete/<int:driver_id>'
            '/booking_delete/<int:booking_id>'

    Gateway port:
        8001: ada_kawan_jogja
        8002: arasya_jakarta
        8003: empat_roda_jogja
        8004: jayamahe_easy_ride_jakarta
        8005: moovby_driverless_jakarta
        8006: puri_bali