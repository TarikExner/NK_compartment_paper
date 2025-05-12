from matplotlib.axes import Axes

organ_diag_cmap = "Set1"


FIGURE_WIDTH_FULL = 6.75
FIGURE_WIDTH_HALF = FIGURE_WIDTH_FULL / 2

FIGURE_HEIGHT_FULL = 9.375
FIGURE_HEIGHT_HALF = FIGURE_HEIGHT_FULL / 2

TITLE_SIZE = 8
AXIS_LABEL_SIZE = 6


full_fig_size = (12,12)
half_fig_size = (12,6)

data_input = "../paper/figure_data/"
figure_output = "../paper/prelim_figures_matched/"

def figure_label(ax: Axes, label, x = 0, y = 1):
    """labels individual subfigures. Requires subgrid to not use figure axis coordinates."""
    ax.text(x,y,label, fontsize = 12)
    return

def _adjust_xlabels(ax):
    ax.set_xticklabels(ax.get_xticklabels(), rotation = 45, ha = "right", fontsize = AXIS_LABEL_SIZE)
    return

def _adjust_ylabels(ax):
    ax.set_yticklabels(ax.get_yticklabels(), fontsize = AXIS_LABEL_SIZE)
    return