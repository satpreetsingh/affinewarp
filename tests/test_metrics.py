"""
Tests for model performance metrics.
"""

import pytest
import numpy as np
from affinewarp.metrics import warp_distances
from affinewarp import PiecewiseWarping, ShiftWarping
from copy import deepcopy
from numpy.testing import assert_allclose


def _rand_model(n_knots, n_trials):
    model = PiecewiseWarping(n_knots=n_knots)
    model.initialize_warps(n_trials)
    model.x_knots, model.y_knots = model._mutate_knots(1e-2)
    return model


@pytest.mark.parametrize('n_knots', [0, 1, 2])
def test_warp_dist(n_knots):
    n_trials = 100
    model_1 = _rand_model(n_knots, n_trials)
    distances = warp_distances(model_1, deepcopy(model_1))
    assert_allclose(np.zeros(n_trials), distances)

    model_2 = _rand_model(n_knots, n_trials)
    assert_allclose(warp_distances(model_2, model_1),
                    warp_distances(model_1, model_2))

    model_3 = deepcopy(model_1)
    model_3.initialize_warps(n_trials)  # set to identity
    pen = warp_penalties(model_1.x_knots, model_1.y_knots, np.empty(n_trials))
    assert_allclose(warp_distances(model_1, model_3), pen)

    model_4 = ShiftWarping()
    model_4.fractional_shifts = np.random.uniform(-.2, .2, size=n_trials)
    model_4.template = np.random.randn(3, 3)
    distances = warp_distances(model_4, deepcopy(model_4))
    assert_allclose(np.zeros(n_trials), distances)

    model_5 = _rand_model(n_knots, n_trials)
    distances = warp_distances(model_4, model_5.copy_fit(model_4))
    assert_allclose(np.zeros(n_trials), distances)


@pytest.mark.parametrize('n_knots', [0, 1, 2])
def test_warp_dist(n_knots):
    n_trials = 100
    model_1 = _rand_model(n_knots, n_trials)
    distances = warp_distances(model_1, deepcopy(model_1))
    assert_allclose(np.zeros(n_trials), distances)

    model_2 = _rand_model(n_knots, n_trials)
    assert_allclose(warp_distances(model_2, model_1),
                    warp_distances(model_1, model_2))

    model_3 = deepcopy(model_1)
    model_3.initialize_warps(n_trials)  # set to identity
    pen = warp_penalties(model_1.x_knots, model_1.y_knots, np.empty(n_trials))
    assert_allclose(warp_distances(model_1, model_3), pen)


@pytest.mark.parametrize('n_knots', [0, 1, 2])
def test_warp_dist(n_knots):
    n_trials = 100
    model_1 = _rand_model(n_knots, n_trials)
    distances = warp_distances(model_1, deepcopy(model_1))
    assert_allclose(np.zeros(n_trials), distances)
