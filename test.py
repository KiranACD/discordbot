import os

for folder in os.listdir('modules'):
    if os.path.exists(os.path.join('modules', folder, 'cog.py')):
        print(folder)
        # client.load_extension(f'modules.{folder}.cog')