
logger = getLogger(__name__)

BASE_ = {
    "name": "",
    "id": "",
    "url": "",
    "constraints": {
        "memoryLimit": 0,
        "timeLimit": 0,
    },

    "tests": [
        {
            "input": "20 3\n5 10 15\n",
            "output": "10\n",
        },
        {
            "input": "20 3\n0 5 15\n",
            "output": "10\n",
        },
    ],
}
