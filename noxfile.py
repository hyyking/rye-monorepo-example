import nox


@nox.session(reuse_venv=True)
def test(session: nox.Session):
    assert True
