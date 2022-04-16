import time

from list_images import images
from psychopy import core
from Template_Task_Psychopy.task_template import TaskTemplate


class SevenDiff(TaskTemplate):
    trials = 194
    nb_ans = 4
    response_pad = False
    left_key_name = "a"
    left_key_code = "0"
    mid_left_key_name = "z"
    mid_left_key_code = "1"
    mid_right_key_name = "o"
    mid_right_key_code = "5"
    right_key_name = "p"
    right_key_code = "6"
    quit_code = "3"
    yes_key_code = "6"
    keys = [left_key_code, mid_left_key_code, right_key_code, mid_right_key_code, yes_key_code, quit_code]

    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_code}"

    instructions = [
        f"Dans cette expérience, il vous est demandé de repérer les différences entre deux images. \n\n Appuyez "
        f"sur la touche '{right_key_code}' pour répondre oui ou pour selectionner la réponse "
        f"de droite. \n\n Appuyez sur la touche '{left_key_code}' pour répondre non ou pour selectionner la réponse de "
        f"gauche.", f"Placez vos index sur les touches '{left_key_code}' et '{right_key_code}.'"]  # à reformuler
    font_size_instr = 0.05

    csv_headers = ['id_candidate', 'no_trial', 'nb_diff', 'ans_candidate',
                   'good_ans', 'result', 'reaction_time', 'time_stamp']

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False, count_image=1):
        abs_time = 0
        time_stamp = 0
        rt = 0
        if no_trial <= 94:
            group = 0
        elif 95 <= no_trial <= 144:
            group = 1
        else:
            group = 2
        self.create_visual_image(image=f'img/{images[group][0]}',
                                 size=self.size(images[group][0])).draw()
        self.win.flip()
        core.wait([.5 if no_trial <= 94 else .5][0])
        self.create_visual_text(
            "Combien voyez-vous de différences entre ces deux images ?").draw()
        self.create_visual_text("0 \t\t/\t\t 1", pos=(-.6, -.4)).draw()
        self.create_visual_text("2 \t\t/\t\t 3+", pos=(.6, -.4)).draw()
        self.win.flip()
        if self.response_pad:
            time_stamp = time.time() - exp_start_timestamp
            resp, abs_time = self.get_response_with_time_response_pad(self.dev)
            print(resp, abs_time)
        else:
            resp, rt = self.get_response_with_time()
        good_ans = self.get_good_ans(images[group][0][-5], {"0": self.left_key_code,
                                                            "1": self.mid_left_key_code,
                                                            "2": self.mid_right_key_code,
                                                            "3": self.right_key_code,
                                                            "4": self.right_key_code,
                                                            "5": self.right_key_code,
                                                            "6": self.right_key_code,
                                                            })
        if resp == good_ans:
            result = 1
        else:
            result = 0
        if self.response_pad:
            self.update_csv(self.participant, no_trial, images[group][0][-5], resp, good_ans, result,
                            round(abs_time - time_stamp, 2), round(abs_time, 2))
        else:
            self.update_csv(self.participant, no_trial, images[group][0][-5], resp, good_ans, result,
                            round(rt, 2), round(time.time() - exp_start_timestamp, 2))
        images[group].pop(0)
        self.check_break(no_trial, 94, 144, test=True)


exp = SevenDiff(csv_folder="csv")
exp.start()
