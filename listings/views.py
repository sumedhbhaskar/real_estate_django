from gc import get_objects
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from listings.forms import createlisting

from django.views.generic import ListView,DetailView,CreateView,UpdateView

from listings.models import Listings


def listings_list(request):
    list = Listings.objects.all()
    
    yolo = {
        "list":list
    }
    print(yolo)
    return render(request,"listings.html",yolo)

#class based view for listings_list
class ListingList(ListView):
    context_object_name: str = "list"
    queryset = Listings.objects.all()
    template_name: str = "listings.html" 
    


def listings_retrive(request,pk):
    data = Listings.objects.get(id=pk)
    if data:
        context = {
            "details":data
        }
        return render(request,"listingdetails.html",context)

#generic view for listings_retrive
class ListingDetails(DetailView):
    context_object_name: str = "details"
    template_name: str = "listingdetails.html"

    def get_object(self):
        obj = get_object_or_404(Listings,id=self.kwargs['pk'])
        return obj



def listings_create(request):
    data = createlisting()
    if request.method == "POST":
        data  = createlisting(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            return redirect("/")
    context = {
        "form":data
    }
    return render(request,"createlisting.html",context)

#generic createview for creating listing
class ListingCreate(CreateView):
    model = Listings
    fields = ["title","price","num_beds","num_baths","square_footage","address","image"]
    success_url: str = reverse_lazy("listings_list")
    template_name: str = "createlisting.html"

def listings_update(request,pk):
    dataobj = Listings.objects.get(id=pk)
    dataform = createlisting(instance=dataobj)
    if request.method=="POST":
        dataform = createlisting(request.POST,instance=dataobj,files=request.FILES)
        if dataform.is_valid():
            dataform.save()
            return redirect("/")
    context = {
        "data":dataform
    }
    return render(request,"listingupdate.html",context)

class ListingUpdate(UpdateView):
    pass



def delete_listings(request,pk):
    dataobj = Listings.objects.get(id=pk)
    dataobj.delete()
    return redirect("/")