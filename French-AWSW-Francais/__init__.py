#Hello :) 
from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

@loadable_mod
class AWSWMod(Mod):
    name = "French AWSW"
    version = "1.00"
    author = "LilacVenus"
    dependencies = ["MagmaLink"]

    def mod_load(self):
        c = ml.find_label("splashscreen") \
            .search_if("persistent.lang == \"Jp\"")
        c.branch() \
            .search_menu().add_choice(text=u"Français {image=tl/frenchtl/image/ui/lang-fr.png}".encode('utf-8'), jump="venus_ChangeToFrench")
        c.branch_else() \
            .search_menu().add_choice(text=u"Français {image=tl/frenchtl/image/ui/lang-fr2.png}".encode('utf-8'), jump="venus_ChangeToFrench")
        c.link_behind_from("venus_ChangeToFrench_end")

    def mod_complete(self):
        pass
