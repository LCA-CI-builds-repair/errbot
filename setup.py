#!/usr/bin/env python
                "templates/new_plugin.py.tmpl",
            ]
        }
            ],
        },
        extras_require={
            "slack": [
                "errbot-backend-slackv3==0.2.1",
            ],
            "discord": [
                "err-backend-discord==3.0.1",
            ],
            "mattermost": [
                "err-backend-mattermost==3.0.0",
            ],
            "IRC": [
                "irc==20.0.0",
            ],
            "telegram": [
                "python-telegram-bot==13.10",
            ],
            "XMPP": [
                "slixmpp==1.7.1",
                "pyasn1==0.4.8",
                "pyasn1-modules==0.2.8",
            ],
            ':sys_platform!="win32"': ["daemonize==2.5.0"],
        },
        author="errbot.io",
        author_email="info@errbot.io",
        description="Errbot is a chatbot designed to be simple to extend with plugins written in Python.",
        long_description_content_type="text/x-rst",
        long_description="".join([read("README.rst"), "\n\n", changes]),
        license="GPL",
        keywords="xmpp irc slack hipchat gitter tox chatbot bot plugin chatops",
        url="http://errbot.io/",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Topic :: Communications :: Chat",
            "Topic :: Communications :: Chat :: Internet Relay Chat",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
if py_version < (3, 9):
    deps.append("graphlib-backport==1.0.3")

src_root = os.curdir


def read_version():
