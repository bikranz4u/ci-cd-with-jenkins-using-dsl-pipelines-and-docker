import types
import jenkins

print([getattr(jenkins, a) for a in dir(jenkins)
  if isinstance(getattr(jenkins, a), types.FunctionType)])