# Helper functions


def fmt_vec(v, precision=2, type="f"):
    """Format the output of a vector with the specified precision"""
    return f"<{v.x:.{precision}{type}}, {v.y:.{precision}{type}}, {v.z:.{precision}{type}}>"
