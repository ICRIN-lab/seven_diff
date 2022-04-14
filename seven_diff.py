import time
from list_images import images
from psychopy import core
from task_template import TaskTemplate


class SevenDiff(TaskTemplate):
    trials = 194
    left_key = "a"
    mid_left_key = "z"
    mid_right_key = "o"
    right_key = "p"
    quit_code = "q"
    yes_key_code = "p"
    keys = ["space", left_key, mid_left_key, right_key, mid_right_key, quit_code]

    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_code}"

    instructions = [
        f"Dans cette expérience, il vous est demandé de repérer les différences entre deux images. \n\n Appuyez "
        f"sur la touche '{right_key}' pour répondre oui ou pour selectionner la réponse "
        f"de droite. \n\n Appuyez sur la touche '{left_key}' pour répondre non ou pour selectionner la réponse de "
        f"gauche.", f"Placez vos index sur les touches '{left_key}' et '{right_key}.'"]  # à reformuler
    font_size_instr = 0.05

    csv_headers = ['id_candidate', 'no_trial', 'nb_diff', 'ans_candidate',
                   'good_ans', 'result', 'reaction_time', 'time_stamp']

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False, count_image=1):
        if no_trial <= 94:
            group = 0
        elif 95 <= no_trial <= 144:
            group = 1
        else:
            group = 2
        self.create_visual_image(image=f'img/{images[group][0]}',
                                 size=self.size(images[group][0])).draw()
        self.win.flip()
        core.wait([8 if no_trial <= 94 else 6][0])
        self.create_visual_text(
            "Combien voyez-vous de différences entre ces deux images ?").draw()
        self.create_visual_text("0 \t\t/\t\t 1", pos=(-.6, -.4)).draw()
        self.create_visual_text("2 \t\t/\t\t 3+", pos=(.6, -.4)).draw()
        self.win.flip()
        resp, rt = self.get_response_with_time()
        good_ans = self.get_good_ans(images[group][0][-5], {"0": self.left_key,
                                                            "1": self.mid_left_key,
                                                            "2": self.mid_right_key,
                                                            "3": self.right_key,
                                                            "4": self.right_key,
                                                            "5": self.right_key,
                                                            "6": self.right_key,
                                                            })
        if resp == good_ans:
            result = 1
        else:
            result = 0
        self.update_csv(self.participant, no_trial, images[group][0][-5], resp, good_ans, result,
                        round(rt, 2), round(time.time() - exp_start_timestamp, 2))
        images[group].pop(0)
        self.check_break(no_trial, 94, 144)


exp = SevenDiff(csv_folder="csv")
exp.start()
