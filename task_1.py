import subprocess

def run_command_and_check_output(command, text):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout
        return text in output
    except subprocess.CalledProcessError:
        return False

def test_run_command_and_check_output():
    command = "echo Hello, world!"
    text = "Hello"
    assert run_command_and_check_output(command, text) == True

    command = "echo Hello, world!"
    text = "Goodbye"
    assert run_command_and_check_output(command, text) == False