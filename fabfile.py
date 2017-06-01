from fabric.api import local


def test():
    local('./manage.py test --settings=adraft.settings.test --noinput')
