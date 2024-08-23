from django.shortcuts import render, redirect
from .models import MessagesModel, MessengerModel, FavoriteUserModel, BlockUserModel
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

def get_user_img(user):
    userprofile = user.userprofile
    img = userprofile.profile_image_base64
    return img

def get_user_full_name(user):
    userprofile = user.userprofile

    if userprofile.account_type == '2':
        return userprofile.director_profile.full_name
    elif user.userprofile.account_type == '3':
        return userprofile.student_profile.full_name
    elif user.userprofile.account_type == '4':
        return userprofile.Coach_profile.full_name
    else:
        return None

def get_user_capacity(user):
    userprofile = user.userprofile

    if userprofile.account_type == '2':
        return 'مدير'
    elif user.userprofile.account_type == '3':
        return 'طالب'
    elif user.userprofile.account_type == '4':
        return 'مدرب'
    else:
        return None
    
def getUserClub(user):
    userprofile = user.userprofile

    if userprofile.account_type == '2':
        return userprofile.director_profile.club
    elif user.userprofile.account_type == '3':
        return userprofile.student_profile.club
    elif user.userprofile.account_type == '4':
        return userprofile.Coach_profile.club
    else:
        return None

def messageRoom(request, room_id):
    user = request.user
    
    receiver = getUserClub(user)
    is_blocked = BlockUserModel.objects.filter(creator=receiver, user=user).exists()
    is_favorite = FavoriteUserModel.objects.filter(creator=receiver, user=user).exists()
    messages_list = []
    last_date = None
    msg_date = []
    messages = MessagesModel.objects.filter(messenger__id=room_id)
    for msg in messages:
        if last_date == None:
            
            last_date=msg.creation_date.date()
        elif msg.creation_date.date() != last_date:
            
            messages_list.append([last_date, msg_date])
            last_date=msg.creation_date.date()
            msg_date = []
            
        msg_date.append(msg)
    messages_list.append([last_date, msg_date])

    profile_image = receiver.club_profile_image_base64
    return render(request, 'messenger/viewMessage.html', {'is_blocked':is_blocked, 'is_favorite':is_favorite, 'messages_list':messages_list, 'room_id':room_id, 'receiver':receiver, 'profile_image':profile_image})


def get_messenger_model(sender, receiver):
    messengers = MessengerModel.objects.filter(messenger_users=sender).filter(messenger_users=receiver)
    return messengers

def createMessager(request, receiver_id):
    sender = request.user
    receiver = User.objects.get(id=receiver_id)
    
    messengers = get_messenger_model(sender, receiver)

    if sender != receiver:
        room_id = None
        if not messengers.exists():    
            messenger = MessengerModel.objects.create()
            messenger.messenger_users.set([sender, receiver])
            messenger.save()
            room_id = messenger.room_id
        else:
            room_id = messengers.first().room_id
        return redirect('messageRoom', room_id)
    else:
        return redirect('index')


def AddFavorite(request, receiver_id):
    creator = request.user
    receiver = User.objects.get(id=receiver_id)

    if not FavoriteUserModel.objects.filter(creator=creator, user=receiver).exists():
        fav = FavoriteUserModel.objects.create(creator=creator, user=receiver)
        fav.save()

    room = get_messenger_model(sender=creator, receiver=receiver).first()

    return redirect('messageRoom', room.room_id)

def DeleteFavorite(request, fav_id):
    sender = request.user
    if request.GET.get('redir'):
        receiver = User.objects.get(id=fav_id)
        room = get_messenger_model(sender=sender, receiver=receiver).first()
        favs = FavoriteUserModel.objects.filter(creator=sender, user=receiver)
        if favs.exists():
            favs.first().delete()
        return redirect('messageRoom', room.room_id)
    else:
        if FavoriteUserModel.objects.filter(id=fav_id).exists():
            fav = FavoriteUserModel.objects.get(id=fav_id)
            receiver = fav.user

            return JsonResponse({'status':True})
        return JsonResponse({'status':False})


def BlockUserMessenger(request, receiver_id):
    creator = request.user
    receiver = User.objects.get(id=receiver_id)
    if not BlockUserModel.objects.filter(creator=creator, user=receiver).exists():
        fav = BlockUserModel.objects.create(creator=creator, user=receiver)
        fav.save()

    room = get_messenger_model(sender=creator, receiver=receiver).first()

    return redirect('messageRoom', room.room_id)

def DeleteBlockUser(request, block_id):
    sender = request.user
    if request.GET.get('redir'):
        receiver = User.objects.get(id=block_id)
        room = get_messenger_model(sender=sender, receiver=receiver).first()
        favs = BlockUserModel.objects.filter(creator=sender, user=receiver)
        if favs.exists():
            favs.first().delete()
        return redirect('messageRoom', room.room_id)
    else:
        if BlockUserModel.objects.filter(id=block_id).exists():
            fav = BlockUserModel.objects.get(id=block_id)
            fav.delete()

            return JsonResponse({'status':True})
        return JsonResponse({'status':False})