import pkg_resources
import resource
import platform
import psutil
from datetime import datetime as dt


#-----------------fonction que je vais re utiliser  ------------------#

# fonction qui convertit un grand nombre d'octets dans un format à l'échelle

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# retour à la ligne rapide


def void():
    print("\n")


print("\n", "="*40, "Information Générale", "="*40, "\n")

#---------------- info sur les versions -------------------#

print("\n", "-"*30, "Informations système", "-"*30, "\n")


def versionSystem():  # version du systeme

    vsysteme = platform.system()
    version = platform.release()
    if vsysteme == "Windows":  # pour windows
        print("Votre systeme est sous Windows en :", version)

    elif vsysteme == "Linux":  # pour linux
        print("Votre systeme est sous Linux en :", version)

    elif vsysteme == "Darwin":  # pour Mac
        print("Votre systeme est sous MacOS en :", version)

    else:
        print("Systeme inconnu")  # si erreur


versionSystem()


def versionKernel():  # version du kernel
    vkernel = platform.platform()  # v du kernel (non detaillé)
    print("La version du kernel est en :", vkernel)


versionKernel()


def uptime():  # temps d'utilisation de la machine
    boot_time_timestamp = psutil.boot_time()
    bt = dt.fromtimestamp(boot_time_timestamp)
    print(f"Le temps d'utilisation est de : {bt.hour}:{bt.minute}:{bt.second}")


uptime()


#---------------------information hardware --------------------#

print("\n", "-"*30, "Informations Hardware", "-"*30, "\n")


def hardware():  # fonction pour ttes les infos hardware
    infocpu()
    infomemoire()


print("\n", "*"*20, "Information du CPU", "*"*20, "\n")


def infocpu():  # info CPU + detaille
    print("Nom du CPU :", platform.processor())
    print("Le total de cores :", psutil.cpu_count(logical=True))


infocpu()

print("\n", "*"*20, "Information Mémoire", "*"*20, "\n")


def infomemoire():  # Information mémoire + detaille

    svmem = psutil.virtual_memory()
    print(f"La mémoire totale: {get_size(svmem.total)}")
    print(f"La mémoire disponible: {get_size(svmem.available)}")
    print(f"La mémoire utilisé: {get_size(svmem.used)}")


infomemoire()

print("\n", "*"*20, "Information du Disque", "*"*20, "\n")


def infodisque():  # info disque espace

    partitions = psutil.disk_partitions()
    for partition in partitions:

        partition_usage = psutil.disk_usage(partition.mountpoint)

    print(f"L'espace total : {get_size(partition_usage.total)}")
    print(f"L'espace utilisé : {get_size(partition_usage.used)}")
    print(f"L'espace libre: {get_size(partition_usage.free)}")


infodisque()
#----------------- limite fichiers ouverts ----------------#
print("\n", "-"*30, "Informations fichiers ouverts", "-"*30, "\n")


def limitfile():

    print(resource.getrlimit(resource.RLIMIT_NOFILE))


limitfile()

print("\n", "-"*30, "Listes des paquets installés", "-"*30, "\n")


def packagelist():

    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                      for i in installed_packages])
    print("Liste des paquets installés :", "\n", installed_packages_list, "\n")


packagelist()
