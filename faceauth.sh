#!/bin/bash

## THIS IS CONFIGURED FOR KDE. PLEASE CONFIGURE ACCORDINGLY IF YOU WANT IT TO WORK.

#https://superuser.com/a/898994
#https://unix.stackexchange.com/a/368632

echo Kill with ^C

set -o nounset                # good practice, exit if unset variable used

pidfile=/tmp/lastauth.pid     # lock file path
logfile=/tmp/lastauth.log     # log file path

cleanup() {                   # when cleaning up:
    rm -f $pidfile            # * remove the lock file
    trap - INT TERM EXIT      # * reset kernel signal catching
    exit                      # * stop the daemon
}

log() {                       # simple logging format example
    echo $(date +%Y-%m-%d\ %X) -- $USER -- "$@" >> $logfile
}

if [ -e "$pidfile" ]; then    # if lock file exists, exit
    log $0 already running...
    exit
fi

trap cleanup INT TERM EXIT    # call cleanup() if e.g. killed

log daemon started...

echo $$ > $pidfile            # create lock file with own PID inside



#prints out, among other things;
#      string "org.kde.screensaver"
#transform it to 'org.kde.screensaver'
service=$(\
    dbus-send \
        --session \
        --dest=org.freedesktop.DBus \
        --type=method_call \
        --print-reply \
        /org/freedesktop/DBus org.freedesktop.DBus.ListNames \
    | grep -o '[^"]*.screensaver'
)

#prints out, among other things;
#method bool org.freedesktop.ScreenSaver.SetActive(bool e)
#transform it to 'org.freedesktop.ScreenSaver'
interface=$(
    qdbus \
        $service /ScreenSaver \
    | grep -oP '[^ ]*(?=.SetActive)'
)

path='/ScreenSaver'

#monitor it with a while loop
dbus-monitor "type='signal',interface='$interface',member='ActiveChanged',path='$path'" \
| while read -r line; do
    #ignore the metadata and pull the 'boolean <true/false>' line
    read line

    #check if it is set to true
    if echo $line | grep -q 'true'; then
        source ./unlock.sh
    else
        :
    fi
done


cleanup # let's not leave orphaned lock file when the loop ends (e.g. dbus dies)
