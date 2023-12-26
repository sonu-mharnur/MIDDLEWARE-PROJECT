# def my_middleware(get_response):
#     print("One Time Intilization")
#     def my_function(request):
#         print("this is before view")
#         response = get_response(request)
#         print("This is after view")
#         return response
#     return my_function      


## class base middleware  ###

# class MyMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print("One Time Brother Initiazation")

#     def __call__(self,request):
#         print("this is Brother before view ")
#         response = self.get_response(request)
#         print("this is Brother after view")
#         return response
    



class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Brother Initiazation")

    def __call__(self,request):
        print("this is Brother before view ")
        response = self.get_response(request)
        print("this is Brother after view")
        return response
    
class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Father Initiazation")

    def __call__(self,request):
        print("this is Father before view ")
        response = self.get_response(request)
        print("this is Father after view")
        return response
    
class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Mother Initiazation")

    def __call__(self,request):
        print("this is Mother before view ")
        response = self.get_response(request)
        print("this is Mother after view")
        return response