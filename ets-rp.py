from pypresence import Presence
import time
import epoch
import wmi

f = wmi.WMI()

print("╔════════════════════════════════════════════════════════════════════════════╗\n"
      "║ Welcome to ETSRP!                                                          ║\n"
      "║                                                                            ║\n"
      "║ ETSRP provides a better version of ETS2's original Discord Rich Presence   ║\n"
      "║                                                                            ║\n"
      "║ Made by MakufonSkifto using pypresence                                     ║\n"
      "╚════════════════════════════════════════════════════════════════════════════╝\n")

while True:
    li = []
    for process in f.Win32_Process():
        li.append(process.Name)

    if "eurotrucks2.exe" in li:
        now = epoch.now()

        RPC = Presence("793495110440583178")
        RPC.connect()

        RPC.update(state="Driving in Europe", large_image="ets", large_text="RP Mod by MakufonSkifto",
                   small_image="eu", start=now)
        print("Showing RP")

        time.sleep(15)

    else:
        print("No open ETS2 detected")

    time.sleep(15)
