import time, os

from PIL import Image
from psychopy import visual, gui, data, core
from screeninfo import get_monitors
from task_template import TaskTemplate


def size(no_trial, j):
    image = Image.open(f'img/img_{no_trial}_{j}.png')
    imgwidth, imgheight = image.size

    if imgwidth > get_monitors()[0].width:
        while imgwidth > get_monitors()[0].width:
            imgwidth = imgwidth * 0.9
            imgheight = imgheight * 0.9
    if imgheight > get_monitors()[0].height:
        while imgheight > get_monitors()[0].height:
            imgwidth = imgwidth * 0.9
            imgheight = imgheight * 0.9

    return imgwidth, imgheight


def get_nb_diff(no_trial):
    return len([filename for filename in os.listdir('img') if filename.startswith(f"img_{no_trial}_")]) - 1


class SevenDiff(TaskTemplate):
    trials = 100
    yes_key_name = "p"
    yes_key_code = "p"
    no_key_code = "a"
    no_key_name = "a"
    quit_code = "q"
    keys = ["space", yes_key_name, no_key_name, quit_code]

    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"

    instructions = [
        f"Dans cette tâche cognitive, il vous est demandé de repérer les différences entre deux images. \n\n Appuyez sur la touche '{yes_key_name}' pour répondre oui ou pour selectionner la réponse "
        f"de droite. \n\n Appuyez sur la touche '{no_key_name}' pour répondre non ou pour selectionner la réponse de "
        f"gauche.", "N'appuyez sur les touches que lorsqu'on vous le demande.",f"Placez vos index sur les touches '{no_key_name}' et '{yes_key_name}.'"]

    csv_headers = ['id_candidate', 'no_trial', 'wrong_yes', 'level', 'ans_candidate',
                   'good_ans', 'reaction_time', 'time_stamp']

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False, count_image=1):
        wrong_yes = 0
        j = get_nb_diff(no_trial)
        print(j)
        result = 0
        while True:
            self.create_visual_image(image=f'img/img_{no_trial}_{j}.png', size=size(no_trial, j)).draw()
            self.win.flip()
            core.wait(8)
            self.create_visual_text("Voyez-vous une ou plusieurs différences entre ces deux images ? \n\n Non / Oui").draw()
            self.win.flip()
            resp, rt = self.get_response_with_time()
            self.update_csv(self.participant, no_trial, wrong_yes, j, resp, j == 0, round(rt, 2),
                            round(time.time() - exp_start_timestamp, 2))
            if resp == self.yes_key_code and j == 0:
                if result == 1:
                    wrong_yes += 1
                continue
            elif resp == self.yes_key_code and j > 0:
                j -= 1
            elif resp == self.no_key_code:
                if j == 0:
                    result = 1  # ggs
                break
        if no_trial == 50:
            self.create_visual_text("Pause").draw()
            core.wait(600)
        elif no_trial == 75:
            self.create_visual_text("Pause").draw()
            core.wait(300)


exp = SevenDiff(csv_folder="csv")
exp.start()
