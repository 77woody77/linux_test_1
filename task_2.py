import subprocess
import string


def run_command_and_check_output(command, text, split_mode=False):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
        output = result.stdout

        if split_mode:
            translator = str.maketrans('', '', string.punctuation)
            cleaned_output = output.translate(translator)
            words = cleaned_output.split()
            return text in words
        else:
            return text in output
    except subprocess.CalledProcessError:
        return False


command = "echo Hello, world!"
text = "Hello"
print(run_command_and_check_output(command, text, split_mode=True))
