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
import baml_py
from enum import Enum
from pydantic import BaseModel, ConfigDict
from typing import Dict, List, Optional, Union, Literal


class DeDupeResult(BaseModel):
    
    
    merged_results: List[str]

class DynamicGraph(BaseModel):
    
    
    nodes: List["SimpleNode"]
    relationships: List["SimpleRelationship"]

class Properties(BaseModel):
    
    
    description: Optional[str] = None

class Resume(BaseModel):
    
    
    name: str
    email: str
    experience: List[str]
    skills: List[str]

class SimpleNode(BaseModel):
    
    
    id: str
    type: str
    properties: "Properties"

class SimpleRelationship(BaseModel):
    
    
    source_node_id: str
    source_node_type: str
    target_node_id: str
    target_node_type: str
    type: str
    properties: "Properties"