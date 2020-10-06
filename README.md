# forcebalance-1.3.2
ForceBalance package copied from Lee-Ping Wang. This is a customized version for AMOEBA+ development based on v1.3.2

# what's changed
* deal with new keywords in AMOEBA+ only (not in AMOEBA)
* parallelly run tinker binding energy calculations: `binding.py`
* run multiple tinker analyze jobs at the same time in post-processing of MD trajectory: `npt.py`
* spread tinker molecular dynamic jobs to different computers using `ssh`: `npt.py`
