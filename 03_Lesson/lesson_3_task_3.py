from address import Address
from mailing import Mailing

from_address = Address(pcode="123456", city="Омск", street="Транссибирская",
                       house="10", flat="9")
to_address = Address(pcode="654321", city="Хабаровск", street="Серышева",
                     house="20", flat="7")

mailing = Mailing(to_address=to_address, from_address=from_address,
                  cost=333.33, track="726347823647AERU")
print(mailing)
