##### Add new password
```
$ secstorage add -n api -p test_password -a '{"test":"1", "test2":"123"}'
```

##### Get passwords using attributes
```
$ secstorage get -a '{"test":"1", "test2":"123"}' -v | jq
```

##### Get passwords using name
```
$ secstorage get -n 'api' -a '{}' -v | jq
```

##### Get all passwords using name
```
$ secstorage get -a '{}' | jq
```

##### Remove ONE password 
```
$ secstorage remove -a '{"test":"1", "test2":"123"}' | jq
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
