##### Add new password
```
./secstorage-tools add -a api -p test_password -att '{"test":"1", "test2":"123"}' | jq 
```

##### Get passwords using attributes
```
./secstorage-tools get -att '{"test":"1", "test2":"123"}' | jq 
```

##### Get passwords using name
```
./secstorage-tools get -att '{}' -a api2 | jq
```

##### Get all passwords using name
```
./secstorage-tools get -att '{}' | jq
```

##### Remove ONE password 
```
./secstorage-tools remove -att '{"test":"1", "test2":"123"}' | jq
```
> if there is more than one password, then the NAMES and ATTRIBUTES are displayed

##### Support STOW
1. Add app
```
sudo stow -t / secretstorage
```
2. Delete app
```
sudo stow -D -t / secretstorage
```
