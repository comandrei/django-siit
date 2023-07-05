def simple_middleware(get_response):

    print("Prima initializare")
    def middleware(request):

        print("Inainte de view")
        request.session["view_count"] = request.session.get("view_count", 0) + 1
        request.session["ceva"] = "ceva"
        #import time; time.sleep(5)
        response = get_response(request)

        print("Dupa view")
        return response
    
    return middleware