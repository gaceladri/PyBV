# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_BV')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_BV')
    _BV = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_BV', [dirname(__file__)])
        except ImportError:
            import _BV
            return _BV
        try:
            _mod = imp.load_module('_BV', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _BV = swig_import_helper()
    del swig_import_helper
else:
    import _BV
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def pari_init(parisize, maxprime):
    return _BV.pari_init(parisize, maxprime)
pari_init = _BV.pari_init

def pari_close():
    return _BV.pari_close()
pari_close = _BV.pari_close
class ciphertext(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ciphertext, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ciphertext, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _BV.ciphertext_value_set
    __swig_getmethods__["value"] = _BV.ciphertext_value_get
    if _newclass:
        value = _swig_property(_BV.ciphertext_value_get, _BV.ciphertext_value_set)
    __swig_setmethods__["degree"] = _BV.ciphertext_degree_set
    __swig_getmethods__["degree"] = _BV.ciphertext_degree_get
    if _newclass:
        degree = _swig_property(_BV.ciphertext_degree_get, _BV.ciphertext_degree_set)
    __swig_setmethods__["pk"] = _BV.ciphertext_pk_set
    __swig_getmethods__["pk"] = _BV.ciphertext_pk_get
    if _newclass:
        pk = _swig_property(_BV.ciphertext_pk_get, _BV.ciphertext_pk_set)
    __swig_destroy__ = _BV.delete_ciphertext
    __del__ = lambda self: None

    def __init__(self, *args):
        this = _BV.new_ciphertext(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def initialize(self, *args):
        return _BV.ciphertext_initialize(self, *args)

    def __add__(self, ct):
        return _BV.ciphertext___add__(self, ct)

    def __mul__(self, ct):
        return _BV.ciphertext___mul__(self, ct)

    def __sub__(self, ct):
        return _BV.ciphertext___sub__(self, ct)

    def decrypt(self, sk):
        return _BV.ciphertext_decrypt(self, sk)
ciphertext_swigregister = _BV.ciphertext_swigregister
ciphertext_swigregister(ciphertext)

class secret_key(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, secret_key, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, secret_key, name)
    __repr__ = _swig_repr
    __swig_setmethods__["params"] = _BV.secret_key_params_set
    __swig_getmethods__["params"] = _BV.secret_key_params_get
    if _newclass:
        params = _swig_property(_BV.secret_key_params_get, _BV.secret_key_params_set)

    def __init__(self, *args):
        this = _BV.new_secret_key(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def initialize(self, sk, params):
        return _BV.secret_key_initialize(self, sk, params)

    def decrypt(self, ct):
        return _BV.secret_key_decrypt(self, ct)

    def serialize(self):
        return _BV.secret_key_serialize(self)
    __swig_destroy__ = _BV.delete_secret_key
    __del__ = lambda self: None
secret_key_swigregister = _BV.secret_key_swigregister
secret_key_swigregister(secret_key)

class public_key(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, public_key, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, public_key, name)
    __repr__ = _swig_repr
    __swig_setmethods__["params"] = _BV.public_key_params_set
    __swig_getmethods__["params"] = _BV.public_key_params_get
    if _newclass:
        params = _swig_property(_BV.public_key_params_get, _BV.public_key_params_set)

    def __init__(self, *args):
        this = _BV.new_public_key(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def initialize(self, pk, params):
        return _BV.public_key_initialize(self, pk, params)

    def encrypt(self, m):
        return _BV.public_key_encrypt(self, m)

    def serialize(self):
        return _BV.public_key_serialize(self)
    __swig_destroy__ = _BV.delete_public_key
    __del__ = lambda self: None
public_key_swigregister = _BV.public_key_swigregister
public_key_swigregister(public_key)

class key_pair(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, key_pair, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, key_pair, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sk"] = _BV.key_pair_sk_set
    __swig_getmethods__["sk"] = _BV.key_pair_sk_get
    if _newclass:
        sk = _swig_property(_BV.key_pair_sk_get, _BV.key_pair_sk_set)
    __swig_setmethods__["pk"] = _BV.key_pair_pk_set
    __swig_getmethods__["pk"] = _BV.key_pair_pk_get
    if _newclass:
        pk = _swig_property(_BV.key_pair_pk_get, _BV.key_pair_pk_set)

    def __init__(self):
        this = _BV.new_key_pair()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _BV.delete_key_pair
    __del__ = lambda self: None
key_pair_swigregister = _BV.key_pair_swigregister
key_pair_swigregister(key_pair)

class key_gen(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, key_gen, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, key_gen, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _BV.new_key_gen()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def generate_key(self, n, Q, T, sigma):
        return _BV.key_gen_generate_key(self, n, Q, T, sigma)
    __swig_destroy__ = _BV.delete_key_gen
    __del__ = lambda self: None
key_gen_swigregister = _BV.key_gen_swigregister
key_gen_swigregister(key_gen)

M_PI = _BV.M_PI
class parameters(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, parameters, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, parameters, name)
    __repr__ = _swig_repr
    __swig_setmethods__["n"] = _BV.parameters_n_set
    __swig_getmethods__["n"] = _BV.parameters_n_get
    if _newclass:
        n = _swig_property(_BV.parameters_n_get, _BV.parameters_n_set)
    __swig_setmethods__["Q"] = _BV.parameters_Q_set
    __swig_getmethods__["Q"] = _BV.parameters_Q_get
    if _newclass:
        Q = _swig_property(_BV.parameters_Q_get, _BV.parameters_Q_set)
    __swig_setmethods__["sigma"] = _BV.parameters_sigma_set
    __swig_getmethods__["sigma"] = _BV.parameters_sigma_get
    if _newclass:
        sigma = _swig_property(_BV.parameters_sigma_get, _BV.parameters_sigma_set)
    __swig_setmethods__["q"] = _BV.parameters_q_set
    __swig_getmethods__["q"] = _BV.parameters_q_get
    if _newclass:
        q = _swig_property(_BV.parameters_q_get, _BV.parameters_q_set)
    __swig_setmethods__["t"] = _BV.parameters_t_set
    __swig_getmethods__["t"] = _BV.parameters_t_get
    if _newclass:
        t = _swig_property(_BV.parameters_t_get, _BV.parameters_t_set)
    __swig_setmethods__["F"] = _BV.parameters_F_set
    __swig_getmethods__["F"] = _BV.parameters_F_get
    if _newclass:
        F = _swig_property(_BV.parameters_F_get, _BV.parameters_F_set)

    def __init__(self):
        this = _BV.new_parameters()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _BV.delete_parameters
    __del__ = lambda self: None
parameters_swigregister = _BV.parameters_swigregister
parameters_swigregister(parameters)
cvar = _BV.cvar


def get_element(x, index):
    return _BV.get_element(x, index)
get_element = _BV.get_element

def print_GEN(x):
    return _BV.print_GEN(x)
print_GEN = _BV.print_GEN

def create_GEN(x):
    return _BV.create_GEN(x)
create_GEN = _BV.create_GEN

def Uniform():
    return _BV.Uniform()
Uniform = _BV.Uniform

def Normal():
    return _BV.Normal()
Normal = _BV.Normal

def Gauss(mu, sigma):
    return _BV.Gauss(mu, sigma)
Gauss = _BV.Gauss

def Sample(n, sigma):
    return _BV.Sample(n, sigma)
Sample = _BV.Sample

def generate_random(bit_length):
    return _BV.generate_random(bit_length)
generate_random = _BV.generate_random

def sample_error_polynomial(params):
    return _BV.sample_error_polynomial(params)
sample_error_polynomial = _BV.sample_error_polynomial

def generate_secret_key(params):
    return _BV.generate_secret_key(params)
generate_secret_key = _BV.generate_secret_key

def generate_public_key(sk, params):
    return _BV.generate_public_key(sk, params)
generate_public_key = _BV.generate_public_key

def addition(ct_1, ct_2):
    return _BV.addition(ct_1, ct_2)
addition = _BV.addition

def subtraction(ct_1, ct_2):
    return _BV.subtraction(ct_1, ct_2)
subtraction = _BV.subtraction

def multiplication(ct_1, ct_2):
    return _BV.multiplication(ct_1, ct_2)
multiplication = _BV.multiplication
# This file is compatible with both classic and new-style classes.

