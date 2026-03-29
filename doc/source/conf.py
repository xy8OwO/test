# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '文档'
copyright = '2025, xiaoyibar保留所有权利'
author = 'xiaoyibar'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  # markdown
    "sphinx_design" # 卡片 网页布局 按钮
    # "sphinx_copybutton",
    # "sphinx_sitemap"
 ]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"                      # 主题
html_title = "xiaoyibar"                    # 网页标题
html_static_path = ['_static']              
html_favicon = "_static/logo-dark.svg"      # 网页窗口标题图标

html_css_files = [                          # 自定义CSS样式文件
    "custom.css",
]

html_theme_options = {                      # 主题相关设置
    "light_logo": "_static/logo-light_text.svg",    # 网页图标 左上角 浅色主题
    "dark_logo": "_static/logo-dark_text.svg",      # 网页图标 左上角 暗黑主题
    # "announcement": "欢迎大家访问我的wiki ", #网页顶部公告提示

    "nav_links": [                                  # 菜单选项 左上角 
        {
            "title": "首页",
            "url": "index",
            "children": [
                {
                    "title": "Admonitions",
                    "url": "writing/admonition",
                },
                {
                    "title": "Code Blocks",
                    "url": "writing/code",
                },
                {
                    "title": "Autodoc",
                    "url": "writing/api",
                },
            ]
        },
        {
            "title": "TODO",
            "url": "https://github.com/sponsors/lepture",
        },
        {
            "title": "联系我",
            "url": "https://github.com/sponsors/lepture",
            "external": True,
        },
    ],

  "github_url": "https://github.com/littletail1006" # 网页右上角 外站链接 github 

    
}


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]