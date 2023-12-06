from typing import Optional, List
from pydantic import BaseModel

#! from perspective of dev/admin - info needed to create/update/delete a business
#! from perspective of a user - info given back to read a business

class Badge(BaseModel):
    
