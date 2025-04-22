import os
import sys

# Основной путь к проекту
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Пути к конкретным модулям (если нужно)
sys.path.insert(0, os.path.join(project_root, 'minecraft_service.py'))
sys.path.insert(0, os.path.join(project_root, 'bot.py'))
sys.path.insert(0, os.path.join(project_root, 'config.py'))
sys.path.insert(0, os.path.join(project_root, 'file_service.py'))

print("Project root:", project_root)
print("Minecraft service path:", os.path.join(project_root, 'minecraft_service.py'))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Minecraft Telegram Bot'
copyright = '2025, A. Nonyaeva, P. Shumakova, E. Polkhovskaya, B. Chestikov'
author = 'A. Nonyaeva, P. Shumakova, E. Polkhovskaya, B. Chestikov'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Автодокументирование
    'sphinx.ext.viewcode',  # Показ исходного кода
    'sphinx.ext.napoleon'
]
html_theme = 'sphinx_rtd_theme'  # Стильная тема
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
