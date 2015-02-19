from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from members.models import Member, Boardmember
from funding.models import Vote, Project


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class MayVoteMixin(object):

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        # Has previously voted?
        if self.request.user.id in Vote.objects.filter(
                project=self.kwargs.get('pk')).values_list('user', flat=True):
            raise PermissionDenied

        project_year = Project.objects.get(
            id=self.kwargs.get('pk')).year
        try:
            self.member = Member.objects.get(user_profile=self.request.user)
        except:
            raise PermissionDenied

        boardmember_years = Boardmember.objects.filter(
            member=self.member.id).values_list('year', flat=True)

        if project_year not in boardmember_years:
            raise PermissionDenied

        return super(MayVoteMixin, self).dispatch(request, *args, **kwargs)
