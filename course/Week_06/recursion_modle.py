# recusion Modle:

def recusion(level, param):
    # recusion terminator
    if level > MAX_LEVEL:
        # process_result
        return None

    # process logic current level
    process(level, data)

    # drill down
    recusion(level+1, p1, ...)

    # restore current level status if needed.
