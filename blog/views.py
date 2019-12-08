from django.shortcuts import render
import numpy as np


# Create your views here.
def post_list(request):
    vals = np.array([1,2,3,4])
    return render(request, 'blog/post_list.html', {'vals' : vals})