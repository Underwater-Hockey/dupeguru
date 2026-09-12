# Copyright 2026 Hardcoded Software (http://www.hardcoded.net)
#
# This software is licensed under the "GPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/gpl-3.0.html

from pathlib import Path

from hscommon.testutil import eq_
from core.pe import photo


# Subclasses of Photo don't define __slots__, which is what gives them the __dict__ that
# get_orientation() caches the orientation in.
class FakePhoto(photo.Photo):
    pass


def photo_with_exif_orientation(tmpdir, monkeypatch, orientation):
    path = Path(str(tmpdir)).joinpath("foo.jpg")
    path.touch()
    monkeypatch.setattr(photo.exif, "get_fields", lambda fp: {"Orientation": [orientation]})
    return FakePhoto(path)


def test_get_orientation(tmpdir, monkeypatch):
    p = photo_with_exif_orientation(tmpdir, monkeypatch, 6)
    eq_(p.get_orientation(), 6)


def test_get_orientation_without_exif_data(tmpdir, monkeypatch):
    path = Path(str(tmpdir)).joinpath("foo.jpg")
    path.touch()
    monkeypatch.setattr(photo.exif, "get_fields", lambda fp: {})
    eq_(FakePhoto(path).get_orientation(), 0)


def test_get_orientation_outside_of_exif_range(tmpdir, monkeypatch):
    # EXIF only defines orientations 1 to 8. A picture holding anything else is treated as having
    # no orientation, as matchblock uses the orientation as an index in a list of 8 elements.
    for orientation in (0, 9, 255, -1):
        p = photo_with_exif_orientation(tmpdir, monkeypatch, orientation)
        eq_(p.get_orientation(), 0)
