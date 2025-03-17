from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import Note
from .forms import NoteForm
from django.contrib.auth.models import User


@login_required
def frontpage(request):
    notes_to_self = Note.objects.filter(sender=request.user, recipient=request.user)
    sent_notes = Note.objects.filter(sender=request.user).exclude(recipient=request.user)
    received_notes = Note.objects.filter(recipient=request.user).exclude(sender=request.user)

    return render(request, "notes/frontpage.html", {
        "notes_to_self": notes_to_self,
        "sent_notes": sent_notes,
        "received_notes": received_notes,
    })




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Note

@login_required
def create_note(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude self from dropdown

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        recipient_id = request.POST.get("recipient")  # Get recipient from dropdown

        # Ensure title and content are filled
        if not title or not content:
            return render(request, "notes/create_note.html", {"users": users, "error": "Title and content cannot be empty"})

        # Find recipient user (default to self if none selected)
        if recipient_id:
            recipient = get_object_or_404(User, id=recipient_id)
        else:
            recipient = request.user

        # Create the note
        Note.objects.create(
            sender=request.user,
            recipient=recipient,
            title=title,
            content=content
        )

        return redirect("frontpage")  # Redirect to homepage

    return render(request, "notes/create_note.html", {"users": users})





@login_required(login_url="login")  
def delete_task(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    # Ensure only the note's owner can delete it
    if note.author == request.user:  # Use 'author' instead of 'user'
        note.delete()

    return redirect("frontpage")  

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("frontpage")  
    else:
        form = UserCreationForm()
    
    return render(request, "registration/signup.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout

@login_required(login_url="login")  # Ensures only logged-in users can view notes
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)  # Filter by 'author' instead of 'user'
    return render(request, "notes/note_detail.html", {"note": note})  # Passes the correct note
