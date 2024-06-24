# MS-RentalTransport-GroupI

    path :
        GET:
            car 'num/car'
                'num/car/<int:car_id>'
                'num/available_cars/<string:tanggal_mulai>/<string:tanggal_selesai>'

            driver  'num/driver'
                    'num/driver/<int:driver_id>'

            booking 'num/booking'
                    'num/booking/<int:booking_id>'
                    'num/booking/check/<int:booking_id>'

            provider 'num/provider'

        POST:
            'num/car_add'
            'num/driver_add'
            'num/booking_add'

        PUT:
            'num/car_edit'
            'num/driver_edit'
            'num/booking_edit'
            'num/provider_edit'

        DELETE:
            'num/car_delete/<int:car_id>'
            'num/driver_delete/<int:driver_id>'
            'num/booking_delete/<int:booking_id>'

    *num :
        0: ada_kawan_jogja
        1: arasya_jakarta
        2: empat_roda_jogja
        3: jayamahe_easy_ride_jakarta
        4: moovby_driverless_jakarta
        5: puri_bali