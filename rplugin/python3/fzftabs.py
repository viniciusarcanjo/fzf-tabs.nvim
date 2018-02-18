"""
File: fzftabs.py
Author: Vinicius Arcanjo
Email: viniciusarcanjov@gmail.com
"""

import logging
import neovim

logger = logging.getLogger(__name__)


@neovim.plugin
class TestPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.layout = {'down': '40%'}

    @neovim.function("GetTabs", sync=True)
    def gettabs(self):
        buffers = []
        for tab in self.nvim.tabpages:
            windows = tab.windows
            for win in windows:
                d = {}
                d['name'] = win.buffer.name
                d['tab'] = win.tabpage.number
                buffers.append(d)
        return buffers

    @neovim.command("FZFGt", range='', nargs='*')
    def fzfgtcommand(self, args, range):
        """Switch tab

        :param args: fzf source 'buff name' 'tab'
        """
        for item in args:
            # self.nvim.command("echomsg '{}'".format(item))
            # self.nvim.command('normal {}gt'.format(item.split()[-1]))
            self.nvim.call("feedkeys", "\<esc>")
            self.nvim.command('normal {}gt'.format(item.split()[-1]))
            return

    @neovim.command("Gtf", range='', nargs='*')
    def gtcommand(self, args, range):
        """FZFGt wrapper

        """
        try:
            buffers = self.gettabs()
            bxs = []
            for b in buffers:
                bxs.append("{} {}".format(b['name'], b['tab']))
            kwargs = {
                'source': bxs,
                'sink': 'FZFGt',
                'options': ['--prompt', 'Gt> ']
            }
            layout = self.layout
            if self.nvim.vars.get('fzf_layout'):
                layout = self.nvim.vars.get('fzf_layout')
            kwargs.update(layout)
            self.nvim.call("fzf#run", kwargs)
            self.nvim.call("feedkeys", "i")
        except neovim.api.nvim.NvimError as e:
            self.nvim.call("Exception: {}".format(str(e)))
