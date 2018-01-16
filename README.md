### ConfTest (DEMO)


#### The Quick Start of ConfTest（DEMO）

You can run ConfTest(DEMO) by following command:

``` python workbench.py ```

If you want to change the SUT ( Software-Under-Test), you should edit the workbench.py by changing:

```
lense = "PostgreSQL"
# "lense" is case sensitive!!! Please be careful of the name of software systems.
# ConfTest now supports 4 software systems: "MySQL", "PostgreSQL", "Yum", "Httpd"
```

ConfTest are driven by constraints, and these constraints are saved in ```./lenseinfo/*SoftwareName*.xml```
Faulty misconfigurations are in ```./newconf/``` folder and corresponding system logs are in ```./newlog/``` folder.

#### //TODO The Constraints Specifications in ConfTest

#### //TODO The Introduction to Testing Part

#### //TODO How to add a SUT?
