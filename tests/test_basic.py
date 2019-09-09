# with open('file.txt') as f:
#     contents = f.read()

#     class CustomOpen(object):
#     def __init__(self, filename):
#         self.file = open(filename)

#     def __enter__(self):
#         return self.file

#     def __exit__(self, ctx_type, ctx_value, ctx_traceback):
#         self.file.close()

# with CustomOpen('file') as f:
#     contents = f.read()

#     from contextlib import contextmanager

# @contextmanager
# def custom_open(filename):
#     f = open(filename)
#     try:
#         yield f
#     finally:
#         f.close()

# with custom_open('file') as f:
#     contents = f.read()