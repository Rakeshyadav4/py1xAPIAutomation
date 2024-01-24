#add you constants here
# we can use three ways to call URL like directly
Base_URL = "https://restful-booking.herokuapp.com"

 #  or with normal function
def base_url():
    return "https://restful-booking.herokuapp.com"

 #  or within the class also called as object oriented programming method
class APIConstants(object):

    @staticmethod
    def base_url(): # for staticmethod we don't need self
        return "https://restful-booking.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booking.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booking.herokuapp.com/auth"

    #above we are using staticmethod and below no static because when we run TC1 or TC2 or TC3 above function will be same--
    #where as below it changes as it depended on what booking id you get

    def url_patch_put_delete_booking(self,booking_id):  # here self comma not dot because it is self and booking_id
        return "https://restful-booking.herokuapp.com/booking/" + str(booking_id)

