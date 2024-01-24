from src.constants.api_constants import Base_URL, APIConstants, base_url # here we are imported multiple URL method from api_constants

def test_crud(): # create a test case and print so it will take the url from direct method
    print(Base_URL)

    url_norma_func = base_url()
    print(url_norma_func) # print so it will take the url from normal function

    url_class_method = APIConstants.base_url(), APIConstants.url_create_token(), APIConstants.url_create_booking()
    print(url_class_method)

# so we will get all the 3 methods of URLS in output.In class we can call