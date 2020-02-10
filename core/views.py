from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from datetime import date
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import SimpleUploadedFile
import os
#model / form imports etc
from . models import *
from . forms import PropertyItemImageForm, FoundLocationForm, PropertyGroupForm, PropertyItemForm, FoundAddressForm, SealNumberForm, OwnerForm, OwnerAddressForm
from .functions import *


def make_property_reference():
    last_ref = PropertyGroup.objects.all().order_by('id').last()
    if not last_ref:
         return 'IOM/1/'+ date.today().strftime('%y')
    if last_ref.property_reference.split('/')[2] != date.today().strftime('%y'):
        return 'IOM/1/' + date.today().strftime('%y')
    else:
        ref_no = last_ref.property_reference
        ref_int = int(ref_no.split('/')[1])
        new_ref_int = ref_int + 1
        new_ref_no = 'IOM/' + str(new_ref_int) + '/' + date.today().strftime('%y')
        return new_ref_no

def make_image_reference(property_instance):
    last_ref = property_instance.propertyitemimage_set.all()
    return str(len(last_ref)+1)

# Create your views here.
#https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
class Index(LoginRequiredMixin, ListView):
    template_name='core/index.html'
    model = PropertyGroup
    paginate_by = 4
    def get_queryset(self):
        return PropertyGroup.objects.filter(user=self.request.user).order_by('-created_time')

class Detail(LoginRequiredMixin, DetailView):
    template_name = 'core/detail.html'
    model = PropertyGroup

class Manage(LoginRequiredMixin, ListView):
    template_name = 'core/manage.html'
    model = PropertyGroup
    def get_queryset(self):
        return PropertyGroup.objects.filter(id=self.kwargs['pk'])

class AddOwner(LoginRequiredMixin, View):
    template_name = "core/addOwner.html"
    def get(self, request, pk):
        owner_form = OwnerForm()
        address_form = OwnerAddressForm()
        context = {'owner_form':owner_form,'address_form':address_form,'pk':pk}
        return render(request,self.template_name,context)
    def post(self, request, pk):
        owner_form = OwnerForm(request.POST or None)
        address_form = OwnerAddressForm(request.POST or None)
        if owner_form.is_valid() and address_form.is_valid():
            owner_instance = owner_form.save(commit=False)
            address_instance = address_form.save(commit=False)
            property_item = get_object_or_404(PropertyItem,pk=pk)
            owner_instance.property_item = property_item
            owner_instance.save()
            address_instance.property_item = property_item
            address_instance.save()
            return HttpResponseRedirect(reverse('manage',kwargs={'pk':pk}))

        context = {'owner_form':owner_form,'address_form':address_form,'pk':pk}
        return render(request, self.template_name, context)


class AddGroup(LoginRequiredMixin, View):
    template_name='core/addGroup.html'
    def get(self, request):
        form = PropertyGroupForm()
        context = {"form":form}
        return render(request,self.template_name, context)
    def post(self, request):
        form = PropertyGroupForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.property_reference = make_property_reference()
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('addressOrLocation',kwargs={'pk':instance.id}))
        context = {"form":form}
        return render(request, self.template_name, context)

class AddressOrLocation(LoginRequiredMixin, View):
    template_name='core/addressOrLocation.html'
    def get(self, request, pk):
        context={"pk":pk}
        return render(request,self.template_name,context)

class AddFoundAddress(LoginRequiredMixin, View):
    template_name='core/addFoundAddress.html'
    def get(self, request, pk):
        form = FoundAddressForm()
        context = {"form":form,"pk":pk}
        return render(request,self.template_name,context)
    def post(self, request, pk):
        form = FoundAddressForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.property_group = get_object_or_404(PropertyGroup,pk=pk)
            instance.save()
            return HttpResponseRedirect(reverse('addItem',kwargs={'pk':pk}))
        context = {"form":form,"pk":pk}
        return render(request, self.template_name, context)

class AddFoundLocation(LoginRequiredMixin, View):
    template_name='core/addFoundLocation.html'
    def get(self, request, pk):
        form = FoundLocationForm()
        context = {"form":form,"pk":pk}
        return render(request,self.template_name,context)
    def post(self, request, pk):
        form = FoundLocationForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.property_group = get_object_or_404(PropertyGroup,pk=pk)
            instance.save()
            return HttpResponseRedirect(reverse('addItem',kwargs={'pk':pk}))
        context = {"form":form,"pk":pk}
        return render(request, self.template_name, context)

class AddItem(LoginRequiredMixin, View):
    template_name='core/addItem.html'
    def get(self, request, pk):
        property_form = PropertyItemForm()
        seal_form = SealNumberForm()
        image_form = PropertyItemImageForm()
        context = {"image_form":image_form,"property_form":property_form,"seal_form":seal_form,"pk":pk}
        return render(request,self.template_name, context)
    def post(self, request, pk):
        property_form = PropertyItemForm(request.POST or None)
        seal_form = SealNumberForm(request.POST or None)
        image_form = PropertyItemImageForm(request.POST or None, request.FILES or None)
        if property_form.is_valid() and seal_form.is_valid() and image_form.is_valid():
            property_instance = property_form.save(commit=False)
            seal_instance = seal_form.save(commit=False)
            image_instance = image_form.save(commit=False)
            property_instance.property_group = get_object_or_404(PropertyGroup,pk=pk)
            property_instance.save()
            if seal_instance.seal_reference:
                seal_instance.property_item = property_instance
                seal_instance.save()
            if image_instance.image:
                image_instance.property_item = property_instance
                image_instance.image_number = make_image_reference(property_instance)
                image_instance.save()
            if "one" in request.POST:
                return HttpResponseRedirect(reverse('index'))
            if "another" in request.POST:
                return HttpResponseRedirect(reverse('addItem',kwargs={'pk':pk}))
        context = {"image_form":image_form,"property_form":property_form,"seal_form":seal_form,"pk":pk}
        return render(request, self.template_name, context)

class AddImage(LoginRequiredMixin, View):
    template_name = 'core/addImage.html'
    def get(self, request, pk):
        image_form = PropertyItemImageForm(request.POST or None, request.FILES or None)
        context = {"image_form":image_form,"pk":pk}
        return render(request,self.template_name, context)
    def post(self, request, pk):
        image_form = PropertyItemImageForm(request.POST or None, request.FILES or None)
        if image_form.is_valid():
            image_instance = image_form.save(commit=False)
            if image_instance.image:
                image_instance.property_item = get_object_or_404(PropertyItem,pk=pk)
                image_instance.image_number = make_image_reference(get_object_or_404(PropertyItem,pk=pk))
                image_instance.save()
            return HttpResponseRedirect(reverse('index'))
        context = {"image_form":image_form,"pk":pk}
        return render(request,self.template_name, context)

class AddRandom(LoginRequiredMixin, View):
    template_name = 'core/addRandom.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        d = DataGen()
        for _ in range(0,10):
            group = PropertyGroup(
                user=request.user,
                property_reference=make_property_reference(),
                subject_surname=d.surname(),
                group_ID=d.group_id()
            )
            group.save()
            address = FoundAddress(
                property_group = group,
                flat_number = '',
                house_number = d.house_number(),
                house_name = '',
                road_name = d.road(),
                town = d.town(),
                postcode = d.postcode(),
                notes = ''
            )
            address.save()

            seiz = d.seized_by()
            for i in range(1,randint(2,12)):
                item_list = d.item().split(',')
                desc = item_list[0]
                img_url = item_list[1]
                item = PropertyItem(
                    property_group = group,
                    description = desc,
                    seized_by = seiz,
                    exhibit_reference = seiz+'/'+str(i),
                    seized_time = d.seized_time(),
                    seized_date = d.seized_date(),
                    sub_location = d.sub_location(),
                    notes = ''
                )
                item.save()
                img = PropertyItemImage(
                    property_item = item,
                    image_number = '1',
                    image = SimpleUploadedFile(name=img_url, content=open(BASE_DIR+'/test_images/'+img_url.strip(), 'rb').read(), content_type='image/jpeg'),
                )
                img.save()


        return HttpResponseRedirect(reverse('index'))

class ItemDetail(LoginRequiredMixin, DetailView):
    template_name='core/itemDetail.html'
    model = PropertyItem
