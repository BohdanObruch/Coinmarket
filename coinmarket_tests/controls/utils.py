import os


def resource(relative_path):
    import coinmarket_tests
    from pathlib import Path

    resources_path = (
        Path(coinmarket_tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .absolute()
    )

    if not os.path.isdir(resources_path):
        os.makedirs(resources_path)

    return (
        resources_path
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )
