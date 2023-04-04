import subprocess



def scan(cmd):
    rep = open('report.txt', 'a')

    subprocess.call('nmap -iL /home/redal/Desktop/scan/scan/main/media/IP.txt {cmd}')


resp = input("""\nPlease enter the type of scan you want to run
                1)General ports scan
                2)Specific ports scan
                3)Heart bleed vulnerability scan\n""")
print("You have selected option: ", resp)
if resp == '1':
    file = open('report.txt', 'a')
    file.write('<<<<<<<<<<<<<<<<<<<<<<PORTS REPORT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

    cmd = " -oX scan.xml -T5 -A"
    scan(cmd)

    cmd = "-oX scan.xml --reason"
    scan(cmd)

    cmd = "-oX scan.xml -sU "
    scan(cmd)

    cmd = "-oX scan.xml -p-"
    scan(cmd)



if resp == '2':
    port = str(input("Enter port(s) you want to scan "))
    cmd = "-oX scan.xml -sS -p T:{port}"
    scan(cmd)
    cmd = "-oX scan.xml -sU -p U:{port}"
    scan(cmd)

if resp == '3':

    cmd = "-oX scan.xml -d --script ssl-heartbleed --script-args vulns.showall -sV "
    scan(cmd)