from django.shortcuts import render
from django.http import HttpResponse 
def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
    	"my_list": [

    	## restaurant 1
    	{
    		"restaurant_name": "Sha6ir 3abas",
    		"food_type" : "Kuwaiti"
    	},

    	## restraurant 2
    	{
    		"restaurant_name": "Gogosh",
    		"food_type" : "Farisi"

    	},

    	{
    		"restaurant_name": "Bowl",
    		"food_type" : "contemprary healthy"

    	}

   	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object" : {

    		


    	}

    }
    return render(request, 'detail.html', context)
