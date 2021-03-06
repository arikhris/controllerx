import pytest

from cx_core.feature_support import FeatureSupport
from cx_core.feature_support.light import LightSupport


@pytest.mark.parametrize(
    "number, expected_supported_features",
    [
        (1, {LightSupport.BRIGHTNESS}),
        (
            57,
            {
                LightSupport.BRIGHTNESS,
                LightSupport.FLASH,
                LightSupport.COLOR,
                LightSupport.TRANSITION,
            },
        ),
        (
            149,
            {
                LightSupport.BRIGHTNESS,
                LightSupport.EFFECT,
                LightSupport.COLOR,
                LightSupport.WHITE_VALUE,
            },
        ),
        (0, set()),
    ],
)
def test_init(number, expected_supported_features):
    light_support = LightSupport(None, None, False)
    light_support._supported_features = FeatureSupport.decode(
        number, light_support.features
    )
    assert light_support._supported_features == expected_supported_features
