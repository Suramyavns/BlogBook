from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,CustomAuthenticationForm,CustomUserChangeForm,createBlogForm,updateBlogForm,writeCommentForm,writeReplyForm
from .models import User,blog,comments,replies,follower
from django.db.models import Q
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@login_required(login_url='/loginUser')
@csrf_protect
def index(request):        
    if request.GET.get('Search')!=None:
        filter = request.GET.get('Search')
    else:
        filter = ''

    blogs = blog.objects.all().filter(
        Q(caption__icontains=filter) | Q(body__icontains=filter) | Q(authorid__email__icontains=filter)
    )
    context = {
        'user':request.user,
        'blogs':blogs,
        'num_blogs':blogs.count,
    }
    return render(request,'main.html',context)

@csrf_protect
def loginUser(request):
    if(request.method=='POST'):
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        return render(request,'login.html',{'form':CustomAuthenticationForm,'errors':['Invalid Credentials!']})
    return render(request,'login.html',{'form':CustomAuthenticationForm})

@csrf_protect
def registerUser(request):
    if(request.method == 'POST'):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.POST.get('email')
            user.save()
            login(request=request,user=user)
            return redirect('home')
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':CustomUserCreationForm})

@csrf_protect
def logoutUser(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
    return redirect('home')

@csrf_protect
def showprofile(request,id):
    user = User.objects.get(id=id)
    blogs = blog.objects.filter(authorid=user)
    followingStatus = None
    numFollower = follower.objects.all().filter(user=user).count
    numFollowing = follower.objects.all().filter(follower=user).count
    if follower.objects.filter(
        Q(user=user) & Q(follower=request.user)
    ).exists():
        followingStatus = True
    else:
        followingStatus = False
    if user.id == request.user.id:
        return render(request,'profile.html',{'user':user,'blogs':blogs,'numfollowers':numFollower,'numfollowing':numFollowing})
    return render(request,'profile.html',{'user':user,'followbtn':followingStatus,'blogs':blogs,'numfollowers':numFollower,'numfollowing':numFollowing})

@csrf_protect
def updateprofile(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        newform = CustomUserChangeForm(request.POST,instance=user)
        if newform.is_valid:
            newform.save()
            return redirect('profile',id=request.user.id)
    form = CustomUserChangeForm(instance=user)
    return render(request,'updateprofile.html',{'user':user,'form':form})

@csrf_protect
def deleteUser(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('home')

@csrf_protect
def createBlog(request):
    if(request.method=='POST'):
        form = createBlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.authorid = request.user
            blog.publish_date = timezone.now()
            blog.save()
            return redirect('home')
    return render(request,"createBlog.html",{'form':createBlogForm})

@csrf_protect
def readBlog(request,id):
    thisBlog = blog.objects.get(id=id)
    showBtns = False
    thisblogcomments = comments.objects.all().filter(blog=thisBlog)
    if(request.user.id==thisBlog.authorid.id):
        showBtns=True
    return render(request,'readBlog.html',{'blog':thisBlog,'user':thisBlog.authorid,'showbtns':showBtns,'comments':thisblogcomments,'commentform':writeCommentForm,'toupdatecomment':None})

@csrf_protect
def updateBlog(request,id):
    thisBlog = blog.objects.get(id=id)
    form = updateBlogForm(instance=thisBlog)
    if(request.method=='POST'):
        form = updateBlogForm(request.POST,instance=thisBlog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/readBlog/{id}')
    return render(request,"updateBlog.html",{'form':form,'blog':thisBlog})

@csrf_protect
def deleteBlog(request,id):
    thisBlog = blog.objects.get(id=id)
    thisBlog.delete()
    return redirect('home')

@csrf_protect
def blogAction(request,id,preference):
    thisBlog = blog.objects.get(id=id)
    if(preference==1):
        thisBlog.upvotes+=1
    else:
        thisBlog.downvotes+=1
    thisBlog.save()
    return HttpResponseRedirect(f'/readBlog/{id}')

@csrf_protect
def createComment(request,blogid):
    if request.method=='POST':
        form = writeCommentForm(request.POST)
        thisblog = blog.objects.get(id=blogid)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.authorid = request.user
            comment.blog = thisblog
            comment.publish_date = timezone.now()
            comment.save()
            return HttpResponseRedirect(f'/readBlog/{blogid}')
        
@csrf_protect
def updateComment(request,id):
    thecomment = comments.objects.get(id=id)
    thisBlog = thecomment.blog
    form = writeCommentForm(instance=thecomment)
    showBtns=False
    if(request.user.id==thisBlog.authorid.id):
        showBtns=True
    thisblogcomments = comments.objects.filter(blog=thisBlog)
    if request.method=='POST':
        form = writeCommentForm(request.POST,instance=thecomment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/readBlog/{thisBlog.id}')
    return render(request,'readBlog.html',{'blog':thisBlog,'user':thisBlog.authorid,'showbtns':showBtns,'comments':thisblogcomments,'commentform':writeCommentForm,'updatecommentform':form,'toupdatecomment':id})

@csrf_protect
def deleteComment(request,id):
    thiscomment = comments.objects.get(id=id)
    thisBlog = thiscomment.blog
    thiscomment.delete()
    return HttpResponseRedirect(f'/readBlog/{thisBlog.id}')

@csrf_protect
def commentAction(request,id,preference):
    thiscomment = comments.objects.get(id=id)
    if preference==1:
        thiscomment.upvotes+=1
    else:
        thiscomment.downvotes+=1
    thiscomment.save()    
    return HttpResponseRedirect(f'/readBlog/{thiscomment.blog.id}')


@csrf_protect
def createReply(request,id):
    replyForm = writeReplyForm()
    thiscomment = comments.objects.get(id=id)
    replys = replies.objects.all().filter(comment=thiscomment)
    thisBlog = thiscomment.blog
    showBtns=False
    if(request.user.id==thisBlog.authorid.id):
        showBtns=True
    thisblogcomments = comments.objects.filter(blog=thisBlog)
    form = writeCommentForm(instance=thiscomment)
    if request.method=='POST':
        newform = writeReplyForm(request.POST)
        if newform.is_valid():
            reply = newform.save(commit=False)
            reply.authorid = request.user
            reply.comment = thiscomment
            reply.publish_date = timezone.now()
            reply.save()
            return HttpResponseRedirect(f'/readBlog/{thiscomment.blog.id}')
    return render(request,'readBlog.html',{'blog':thisBlog,'user':thisBlog.authorid,'showbtns':showBtns,'comments':thisblogcomments,'commentform':writeCommentForm,'updatecommentform':form,'toupdatecomment':None,'replies':replys,'replyForm':replyForm,'toreplyoncomment':thiscomment.id,'showrepliesoncomment':thiscomment.id})


@csrf_protect
def readReplies(request,id):
    thiscomment = comments.objects.get(id=id)
    replys = replies.objects.all().filter(comment=thiscomment)
    thisBlog = thiscomment.blog
    showBtns=False
    if(request.user.id==thisBlog.authorid.id):
        showBtns=True
    thisblogcomments = comments.objects.filter(blog=thisBlog)
    form = writeCommentForm(instance=thiscomment)
    return render(request,'readBlog.html',{'blog':thisBlog,'user':thisBlog.authorid,'showbtns':showBtns,'comments':thisblogcomments,'commentform':writeCommentForm,'updatecommentform':form,'toupdatecomment':None,'replies':replys,'replyForm':None,'showrepliesoncomment':thiscomment.id})

@csrf_protect
def updateReply(request,id):
    reply = replies.objects.get(id=id)
    updatereplyform = writeReplyForm(instance=reply)
    thisBlog = reply.comment.blog
    showBtns=False
    if(request.user.id==thisBlog.authorid.id):
        showBtns=True
    thisblogcomments = comments.objects.filter(blog=thisBlog)
    thiscomment = reply.comment
    replys = replies.objects.all().filter(comment=reply.comment)
    if request.method=='POST':
        updatereplyform = writeReplyForm(request.POST,instance=reply)
        if updatereplyform.is_valid():
            updatereplyform.save()
            return HttpResponseRedirect(f"/readReplies/{reply.comment.id}")
    return render(request,'readBlog.html',{'blog':thisBlog,'user':thisBlog.authorid,'showbtns':showBtns,'comments':thisblogcomments,'commentform':writeCommentForm,'updatecommentform':writeCommentForm(instance=reply.comment),'toupdatecomment':None,'replies':replys,'toreplyoncomment':thiscomment.id,'showrepliesoncomment':thiscomment.id,'updatereplyform':updatereplyform,'toupdatereply':id})


@csrf_protect
def deleteReply(request,id):
    thisreply = replies.objects.get(id=id)
    thiscomment = thisreply.comment
    thisreply.delete()
    return HttpResponseRedirect(f'/readReplies/{thiscomment.id}')


@csrf_protect
def replyAction(request,id,preference):
    reply = replies.objects.get(id=id)
    if preference==1:
        reply.upvotes+=1
    else:
        reply.downvotes+=1
    reply.save()
    return HttpResponseRedirect(f"/readReplies/{reply.comment.id}")

@csrf_protect
def follow(request,id):
    user_to_follow = User.objects.get(id=id)
    user_following = request.user
    fwr = follower(user=user_to_follow,follower=user_following)
    fwr.save()
    return HttpResponseRedirect(f'/profile/{id}')

@csrf_protect
def unfollow(request,id):
    user_unfollowing = follower.objects.filter(
        Q(user=User.objects.get(id=id)) & Q(follower=request.user)
    )
    user_unfollowing.delete()
    return HttpResponseRedirect(f'/profile/{id}')
