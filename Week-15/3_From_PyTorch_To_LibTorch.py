import torch
import torch.nn as nn

script_model = torch.jit.script()
torch.jit.save()

%cd pytorch-to-libtorch

!ls

!mkdir build

%cd build

! cmake ..

!cmake --build . --config Release

%cd ..

!./build/run-traced-model

  
