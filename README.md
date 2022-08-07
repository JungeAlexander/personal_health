# Comparing Oura Personal Health Data Over The Years

Read more about this project [here](https://www.alexanderjunge.net/blog/oura-year-on-year/).

**Note** that this is still WIP 🚧 and thus only sparsely documented. Please open an issue or discussion here.

Right now, the code hear can create plots like this based on data from an Oura ring:

<img src="https://user-images.githubusercontent.com/6056731/183278726-b60a400c-2d2c-43d0-bfec-ac089e3c87b1.png" width="400" />

## Setup

### Personal access token

To access your Oura data programmatically, you will need a [personal access token](https://cloud.ouraring.com/v2/docs#section/Data-Access).
My code assumes that your token in a `.env` file in the base directory of this repository which looks like this:

```
OURA_PERSONAL_ACCESS_TOKEN=ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

### Development setup

This project uses [pre-commit](https://pre-commit.com/) which, once you have it [installed](https://pre-commit.com/#install),
can be configured as follows:

```shell
pre-commit install
```
