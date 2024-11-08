###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
from typing import Any, Dict, List, Optional, TypeVar, Union, TypedDict, Type, Literal, cast
from typing_extensions import NotRequired
import pprint

import baml_py
from pydantic import BaseModel, ValidationError, create_model

from . import partial_types, types
from .type_builder import TypeBuilder
from .globals import DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME

OutputType = TypeVar('OutputType')

# Define the TypedDict with optional parameters having default values
class BamlCallOptions(TypedDict, total=False):
    tb: NotRequired[TypeBuilder]
    client_registry: NotRequired[baml_py.baml_py.ClientRegistry]

class BamlSyncClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager
    __stream_client: "BamlStreamClient"

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager
      self.__stream_client = BamlStreamClient(self.__runtime, self.__ctx_manager)

    @property
    def stream(self):
      return self.__stream_client

    
    def ExtractDeDupe(
        self,
        graph: str,
        baml_options: BamlCallOptions = {},
    ) -> types.DeDupeResult:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ExtractDeDupe",
        {
          "graph": graph,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.DeDupeResult, raw.cast_to(types, types))
    
    def ExtractGraph(
        self,
        graph: str,
        baml_options: BamlCallOptions = {},
    ) -> types.DynamicGraph:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ExtractGraph",
        {
          "graph": graph,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.DynamicGraph, raw.cast_to(types, types))
    
    def ExtractResume(
        self,
        resume: str,
        baml_options: BamlCallOptions = {},
    ) -> types.Resume:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ExtractResume",
        {
          "resume": resume,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.Resume, raw.cast_to(types, types))
    



class BamlStreamClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager

    
    def ExtractDeDupe(
        self,
        graph: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.DeDupeResult, types.DeDupeResult]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ExtractDeDupe",
        {
          "graph": graph,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.DeDupeResult, types.DeDupeResult](
        raw,
        lambda x: cast(partial_types.DeDupeResult, x.cast_to(types, partial_types)),
        lambda x: cast(types.DeDupeResult, x.cast_to(types, types)),
        self.__ctx_manager.get(),
      )
    
    def ExtractGraph(
        self,
        graph: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.DynamicGraph, types.DynamicGraph]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ExtractGraph",
        {
          "graph": graph,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.DynamicGraph, types.DynamicGraph](
        raw,
        lambda x: cast(partial_types.DynamicGraph, x.cast_to(types, partial_types)),
        lambda x: cast(types.DynamicGraph, x.cast_to(types, types)),
        self.__ctx_manager.get(),
      )
    
    def ExtractResume(
        self,
        resume: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.Resume, types.Resume]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ExtractResume",
        {
          "resume": resume,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.Resume, types.Resume](
        raw,
        lambda x: cast(partial_types.Resume, x.cast_to(types, partial_types)),
        lambda x: cast(types.Resume, x.cast_to(types, types)),
        self.__ctx_manager.get(),
      )
    

b = BamlSyncClient(DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX)

__all__ = ["b"]