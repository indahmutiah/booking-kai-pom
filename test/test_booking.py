from pages.booking import BookingPage
import pytest

@pytest.mark.parametrize("departure,arrival", [
    ("Bandung", "Jakarta"),
    ("Jakarta", "Bali")
])
def test_booking(setup, departure, arrival):
    booking = BookingPage(setup)
    booking.set_departure(departure)
    booking.set_arrival(arrival)
    booking.select_hoiday()
    booking.submit()