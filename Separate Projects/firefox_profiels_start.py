import subprocess

list_profiles_command = 'firefox.exe -P'
profiles_output = subprocess.check_output(list_profiles_command, shell=True, text=True)

profiles = profiles_output.strip().split('\n')

for i, profile in enumerate(profiles, start=1):
    profile_command = f'firefox.exe -P "{profile}"'
    subprocess.run(['start', 'run', '/k', profile_command], shell=True)
