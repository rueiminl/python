# ref http://stackoverflow.com/questions/17651017/python-post-osx-notification
# prerequisite: ruby installed; $ sudo gem install terminal-notifier
import os

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

def main():
    notify(title    = 'A Real Notification',
            subtitle = 'with python',
            message  = 'Hello, this is me, notifying you!')

if __name__ == '__main__':
    main()