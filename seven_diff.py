import time

from list_images import images
from psychopy import core
from Template_Task_Psychopy.task_template import TaskTemplate


class SevenDiff(TaskTemplate):
    # IMPORTANT ! To MODIFY IF NEEDED
    nb_ans = 4
    response_pad = True  # has to be set on "True" on production.
    # END OF IMPORTANT
    left_key_name = "jaune"
    left_key_code = "0"
    mid_left_key_name = "bleue"
    mid_left_key_code = "1"
    mid_right_key_name = "verte"
    mid_right_key_code = "5"
    right_key_name = "rouge"
    right_key_code = "6"
    quit_code = "3"
    yes_key_code = "6"
    yes_key_name = "verte"
    keys = [left_key_code, mid_left_key_code, right_key_code, mid_right_key_code, yes_key_code, quit_code]
    trials = 200  # SHOULD BE SET TO 200 WHEN JEANNE DO THE WORK
    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"

    # IMPORTANT : REWRITE INSTRUCTIONS
    instructions = [
        f"Dans cette expérience, il vous est demandé de repérer les différences entre deux images. \n\n Appuyez "
        f"sur la touche correspondant au nombre de différences que vous voyez sur l'image",
        "Les propositions de réponses sont : \n 0, 1, 2 ou 3+", "N'appuyez sur les touches colorées que lorsque la question apparaît.",
        "Placez vos index sur les touches colorées."]
    font_size_instr = 0.05

    csv_headers = ['id_candidate', 'no_trial', 'nb_diff', 'ans_candidate',
                   'good_ans', 'result', 'reaction_time', 'time_stamp']

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False, count_image=1):
        if no_trial < 100:
            group = 0
        elif 100 <= no_trial < 150:
            group = 1
        else:
            group = 2
        self.create_visual_image(image=f'img/{images[group][0]}',
                                 size=self.size(images[group][0])).draw()
        self.win.flip()
        core.wait([7 if no_trial < 100 else 5][0])
        self.create_visual_text(
            "Combien voyez-vous de différences entre ces deux images ?").draw()
        self.create_visual_text("0 \t\t/\t\t 1", pos=(-.6, -.4)).draw()
        self.create_visual_text("2 \t\t/\t\t 3+", pos=(.6, -.4)).draw()
        self.win.flip()
        time_stamp = time.time() - exp_start_timestamp
        resp, rt = self.get_response_with_time(self.response_pad)
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
                            round(rt - time_stamp, 2), round(rt, 2))
        else:
            self.update_csv(self.participant, no_trial, images[group][0][-5], resp, good_ans, result,
                            round(rt, 2), round(time.time() - exp_start_timestamp, 2))
        images[group].pop(0)
        self.check_break(no_trial, 99, 149, test=False)  # put test=False on production


exp = SevenDiff(csv_folder="csv")
exp.start()
