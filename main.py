import pwd, os, psutil
import time

cur_user = pwd.getpwuid(os.getuid())[0]

app = []
code = { "code" }
web = { "firefox"}
ignorelist = { "RDD Process", "Isolated Web Co", "Web Content", "Utility Process" ,"Socket Process", "Privileged Cont", "snap", "WebExtensions", "cpuUsage.sh", "sleep", "systemd", "(sd-pam)", "pipewire", "pipewire-media-session", "pulseaudio", "snapd-desktop-integration", "gnome-keyring-daemon", "gdm-wayland-session", "dbus-daemon", "gnome-session-binary", "xdg-document-portal", "gnome-session-ctl", "xdg-permission-store", "gvfsd", "fusermount3", "gvfsd-fuse", "gnome-shell", "at-spi-bus-launcher", "gnome-shell-calendar-server", "evolution-source-registry", "dconf-service", "goa-daemon", "gvfs-udisks2-volume-monitor", "evolution-calendar-factory", "gvfs-gphoto2-volume-monitor", "gvfs-goa-volume-monitor", "goa-identity-service", "gvfs-afc-volume-monitor", "evolution-addressbook-factory", "gvfs-mtp-volume-monitor", "gvfsd-trash", "gjs", "at-spi2-registryd", "sh", "ibus-daemon", "gsd-a11y-settings", "gsd-color", "gsd-datetime", "gsd-housekeeping", "gsd-keyboard", "gsd-media-keys", "gsd-power", "gsd-print-notifications", "gsd-rfkill", "gsd-screensaver-proxy", "gsd-sharing", "gsd-smartcard", "gsd-sound", "gsd-wacom", "ibus-memconf", "ibus-extension-gtk3", "ibus-portal", "gsd-disk-utility-notify", "VBoxClient", "gsd-printer", "evolution-alarm-notify", "snap-store", "Xwayland", "ibus-engine-simple", "gvfsd-metadata", "xdg-desktop-portal", "tracker-miner-fs-3", "xdg-desktop-portal-gnome", "gsd-xsettings", "xdg-desktop-portal-gtk", "ibus-x11", "update-notifier", "ssh-agent", "gnome-calendar", "seahorse", "chrome_crashpad_handler", "bash", "python3" }
codingtime = 0
webtime = 0

while True:
    for p in psutil.pids():
        try:
            pname = psutil.Process(p).name()
            if psutil.Process(p).username() == cur_user:
                if pname not in ignorelist:
                    if pname not in app:
                        app.append(pname)
                        print(pname)
        except psutil.NoSuchProcess:  # Catch the error caused by the process no longer existing
            pass  # Ignore it
    for pcode in app:
        if pcode in app:
            codingtime += 1
    for pweb in web:
        webtime += 1
    app = []
    if codingtime > 10:
        print('Enough coding for today!')
        
        exit(1)
    time.sleep(1)