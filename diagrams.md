### 
```
Root CA
├── Intermediate CA 1
│   ├── Leaf Certificate 1
│   ├── Leaf Certificate 2
│   ├── Leaf Certificate 3
│   └── Leaf Certificate 4
└── Intermediate CA 2

```

```
Node 1         Node 2         Node 3
  |               |               |
  | --- Request 1 --->            |
  |               |               |
  |               | --- Request 2 ---> 
  |               |               |
  |               |               | Process Request 2
  |               |               |
  |               | <--- Response 2 ---
  |               |               |
  | <--- Response 1 ---           |
  |               |               |

```
