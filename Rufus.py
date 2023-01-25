import git
import datetime
from pytz import timezone

now_utc = datetime.datetime.now(timezone('UTC'))

def print_git_status(git_dir):
  try:
    repo = git.Repo(git_dir)
    head = repo.head
    active_branch = repo.active_branch
    is_dirty = repo.is_dirty()
    one_week_ago = now_utc - datetime.timedelta(weeks=1)
    updated_recently = head.commit.authored_datetime > one_week_ago
    authored_by_rufus = head.commit.author.name == 'Rufus'
    print(f'active branch: {active_branch}')
    print(f'local changes: {is_dirty}')
    print(f'recent commit: {updated_recently}')
    print(f'blame Rufus: {authored_by_rufus}')
    print(f'last commit authored by {head.commit.author.name} on {head.commit.authored_datetime}')
  except:
    print('Error: Path might not be a git repo')



# To see output uncomment the line below this one and add in the path to repo as the argument
# print_git_status('/sample/pathto/myrepo')
