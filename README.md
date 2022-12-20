Create a Dockerfile 
===================

```Dockerfile
FROM ubuntu
COPY data/part1 data/part2 data/part3 /data
COPY data/part4 /data
COPY data/part5 data/part6 data/part7 /data
```

In order to make such a Dockerfile, we need to know which parts can be placed into each layer.

A Python script named [main.py](main.py) is developed to partition the data and generate the
corresponding `Dockerfile`.

Solution
----
The solution can be described as the following steps:

1. Initialize a list named ans to store the answer and each item in the list is a list to store the directories go to
   same `COPY`.
2. Get the top level directories in root directory.
3. Calculate the size of files in each top level directory.
4. If the sum of size is less than 5 Mib, then store the directory to the same item in ans.
5. Else initialize a new item to store the directory.
6. Once getting the ans, then iterate the ans to generate `Dockerfile` file, one item in ans go to the same `COPY`
   command.

Run the script
-----
To execute the solution.py script.

* Running command `python3 solution.py`.

Output Dockerfile
-----
The `Dockerfile` file is:

```Dockerfile
FROM ubuntu
COPY data/dir-a01eabb9-4fd4-41e1-b213-b5221ecbfe06 data/dir-39d1efac-55f4-4654-bf2d-7d07910abdff data/dir-c9cff361-692d-4270-ae8e-d8a283494420 data/dir-9d5e7cd8-bbff-4c63-8892-b0ab2528621a data/dir-6aa5cc5e-1552-4cd2-8ecf-0bc69f8e6ab1 data/dir-afc31085-d863-4e4d-a8ee-3a7bae9445c5 /data
COPY data/dir-87322064-e6ef-4b47-b024-c80fe1ba5667 data/dir-27f5378f-e261-461b-b286-fcd18fead187 data/dir-0b47a68b-6dae-4f4f-950a-afd8dd51082b data/dir-01569ce9-1028-4262-bf5c-cdd98c38e4f5 data/dir-1d7d3c57-9bcd-4329-ac35-6009d7845bca data/dir-8599afa3-f341-4838-b13a-e2bdb2de5f63 data/dir-6ee409df-da1f-4a32-b74b-f4e5be38daf0 /data
COPY data/dir-d6e23da2-ad0f-4370-8502-84f746d85f98 data/dir-ff39d835-3bda-4503-a1d3-f079cbfb127f data/dir-94135523-a870-4270-a059-d7a99a5722de data/dir-d94f1040-e1da-4dfb-95c9-9f58698d0926 data/dir-5d3880c8-ef88-47e4-81a2-abf2e69f88d9 /data
COPY data/dir-99f61d16-e4bd-4ce5-b627-cd8332752020 data/dir-5fa9b390-af25-4df3-a274-adf69faf1532 data/dir-9c7492ed-3b5b-4f88-ab8b-c1416f58f375 /data
COPY data/dir-e57957db-81c4-4e73-962b-c423c2906aa6 data/dir-73b820e1-efbf-42c1-bb0a-66526e645c71 data/dir-64e9d4dc-cc14-4857-b8bc-42096053b0d2 data/dir-238dae7c-dc1d-4afb-9b30-c62a3ae68f25 /data
COPY data/dir-cdcf19f4-2950-4166-b25a-f3570689c2f3 data/dir-b82aae6b-5116-4aba-8aa5-7ff5bf7d5c16 data/dir-ea2324aa-b034-4431-bc28-05475f19a561 data/dir-f9269fb6-12bd-44c3-9ee6-d24c28de6587 data/dir-9f62bd55-3ea6-482c-a82c-3ab37d87d8cd /data
COPY data/dir-cc9a0a19-4b2b-4e66-91ae-42638b454b72 data/dir-01b2d473-bc27-46b5-9093-29d1086f5900 data/dir-9f82406c-f969-41aa-89a4-3bc7d3410862 data/dir-9a7f91a2-4fbf-4201-abdf-a1292d60d261 /data
COPY data/dir-ff0a6d79-8d4d-46ea-a83d-4d776b29adc9 data/dir-1fde177d-e703-4c02-99db-4aa69dd31454 data/dir-4bdd519c-2a2d-4f68-a4f9-9b756fbd81ff /data
COPY data/dir-2e8e3589-f78b-4186-9169-f14c86115244 data/dir-a8cddb8f-bca5-442b-bd0a-f747ac3195df data/dir-686839b3-4fdd-4139-bb5d-c912708d96a1 data/dir-3742fa53-3f94-43e4-a066-a31f5ab82d9e /data
COPY data/dir-d9446117-8567-4209-a8e5-f7652a38aa86 data/dir-20e931cc-b084-4d03-8157-ca4d4d75f792 data/dir-747b535c-9d2f-4c2e-8387-3ccc3cd80d8f data/dir-7c506e63-4767-42b2-954e-ef5d4c551d85 /data
COPY data/dir-76facff5-c551-48d1-8230-1dceeab72e3e data/dir-58d068aa-5e8b-4b08-8352-21159794f070 data/dir-47302781-a666-400f-9bb5-5bffe7843eed data/dir-d8e58afe-777b-4c01-a463-f6b042aca89b data/dir-9b876c8d-e018-45d3-9a64-48e957915344 data/dir-a34a56e4-d5c7-45de-a99d-72dc41d4c3f8 /data
COPY data/dir-9cf227eb-baed-4364-a840-efec7008aacf data/dir-abf3df8e-0bc6-40b5-90b3-6bbe6a927c9f data/dir-efce665f-2040-4a61-a6d2-e13e48e86f90 /data

```
