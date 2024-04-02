from django.shortcuts import render, get_object_or_404, redirect


from .forms import ConversationMessaegForm
from .models import Conversation
from item.models import Item


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if (item.created_by == request.user):
        return redirect('dashboard')

    conversations = Conversation.objects.filter(item=item).filter(
        members__in=[request.user.id])
    # miyad tamam conversation hay marbot be ye mahsol va user ro migire.

    if conversations:
        redirect('detail', pk=conversations.first().id)
        # in condition yani age ghablan ye conversation vojod dasht boro hamon ro biyar va edame bede!

    if request.method == "POST":
        form = ConversationMessaegForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            # bia ye conversation dorost kon bad bad attribute item equal ba item moshakhas shdode
            conversation.members.add(request.user)
            # kasi ke chat ro start karde ya moshtari ro add mide
            conversation.members.add(item.created_by)
            # saheb kala ro add mide
            conversation.save()
            # goftego save shod

            conversation_message = form.save(commit=False)
            # payam toy form ro call mikone
            conversation_message.conversation = conversation
            # conversation ro update mikone
            conversation_message.created_by = request.user
            # ersal konande moshakhas mishe
            conversation_message.save()

            return redirect("detail", pk=item_pk)
            # redirect mishe be hamon safhe mahsol bad ersal chat
    else:
        form = ConversationMessaegForm()
        # yani form khaliye va chizi nagerfte pas chizi ham nashode

    context = {
        'form': form,
    }
    return render(request, 'conversation/new.html', context)


def inbox(request):
    conversations = Conversation.objects.filter(
        members__in=[request.user.id])
    # miyad tamam chat haye ke ye user tosh naghsh dare ro migire

    context = {
        'conversations': conversations
    }
    
    return render(request, 'conversation/inbox.html', context)


def detail(request, pk):
    conversation = Conversation.objects.filter(
        members__in=[request.user.id]).get(pk=pk)
    # chatay marbot be ye nafar va conersationi ke mikhad tosh chat bede ro migire

    if request.method == "POST":
        form = ConversationMessaegForm(request.POST)
        # meghdar post shode az form ro farakhani mikone. 
        # masalan agar 2 to form dashti har kodom ro bayad meghdar tosho ba 'request.POST' bekeshi biron.

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            # khat bala yani chat ya form ersal shode hamon edame ghabliye! (same converstaion object)
            conversation_message.created_by = request.user
            conversation_message.save()
            # message ro ba nam khodam save bezan ke yani man ersal kardam!
            conversation.save()
            # conversation updated with new chat

            return redirect('conversation-detail', pk=pk)
    else:
        form = ConversationMessaegForm()
        # meghdari nagerefte

    context = {
        'conversation': conversation,
        'form': form
    }
    return render(request, 'conversation/detail.html', context)
