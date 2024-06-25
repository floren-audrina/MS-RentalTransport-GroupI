# MS-RentalTransport-GroupI

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