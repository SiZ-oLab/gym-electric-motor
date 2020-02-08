from setuptools import setup

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='gym_electric_motor',
      version='0.0.3',
      description='An OpenAI gym environment for electric motor control.',
      install_requires=requirements,
      extra_requires={'examples': ['keras>=2.2.4',
                                   'keras_rl>=0.4.2',
                                   'rl>=3.0',
                                   'tensorflow<=1.14']},
      author='Arne Traue, Gerrit Book, Praneeth Balakrishna',
      long_description=long_description,
      url="https://github.com/upb-lea/gym-electric-motor",
      )
