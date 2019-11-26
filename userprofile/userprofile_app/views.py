from django.shortcuts import render

from .forms import ProfileForm

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_profile(request):

    if request.method == 'POST':

        print('POST Request Received 1')

        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():

            print('POST Request Received 2')

            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']

            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()

            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'error.html')

            user_pr.save()
            print('going to details')
            return render(request, 'details.html', {'user_pr': user_pr})

        else:
            form = ProfileForm()
            return render(request, 'create.html', {"form": form})

    elif request.method == 'GET':

        print('GET Request Received')

        form = ProfileForm()
        return render(request, 'create.html', {"form": form})
