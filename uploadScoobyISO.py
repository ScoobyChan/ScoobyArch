import os

# os.system('git status')
# os.system('echo "# ScoobyISOBuildTool" >> README.md')
# os.system('git init')
os.system('sudo git add README.md')

for file in os.listdir():
	os.system(f'sudo git add {file}')

os.system('sudo git commit -m "Updating ISO"')	
os.system('sudo git remote add origin https://github.com/ScoobyChan/ScoobyArch.git')
os.system('sudo git push -u origin master')

