# forcebalance-1.3.2
ForceBalance package copied from Lee-Ping Wang. This is a customized version for AMOEBA+ development based on v1.3.2

# new features
* Deal with new keywords in AMOEBA+ only (not in AMOEBA): `parser.py` `tinkerio.py`
* Parallelly run tinker binding energy calculations: `binding.py`
* Run multiple tinker analyze jobs at the same time in post-processing of MD trajectory: `npt.py`
* Spread tinker molecular dynamic jobs to different computers using `ssh`: `liquid.py`
