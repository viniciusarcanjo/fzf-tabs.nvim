## fzf-tabs.nvim

Switch tabs (`gt`) based on buffer name or tab-id with fzf. It's particularly useful if you manage your workspaces with tabs on neovim.

## Demo

[![fzf-tabs-demo](https://img.youtube.com/vi/3L6PnETnTdA/0.jpg)](https://www.youtube.com/watch?v=3L6PnETnTdA)

## Pre-requisites

You should have `fzf.vim` and `python3` installed.

## Installation

Use your favorite plugin manager, I use `dein`:

```
call dein#add('viniciusarcanjo/fzf-tabs.nvim', { 'depends': 'fzf.vim' })
```

## Configuration

There's no default mapping you have to map the `:Gtf` command. It's up to you to you, I use `<localleader>t`:

```
" tabs
nnoremap <silent> <localleader>t :Gtf<CR>
```

The layout variable comes from `fzf.vim`, so it's going to use the same layout that you have with fzf.vim, for example:

```
let g:fzf_layout = { 'down': '30%' }
```
