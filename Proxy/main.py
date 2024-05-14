from proxy import Leader, SecretaryProxy, dev_request_for_promotion


if __name__ == "__main__":
    offer = "raise for 5K"

    print("1. Dev can request directly to Leader")
    leader = Leader()
    dev = dev_request_for_promotion(leader, offer)

    print(
        "2. Most of the time, devs have to request to SecretaryProxy before reaching the Leader"
    )
    proxy = SecretaryProxy(leader)
    dev = dev_request_for_promotion(proxy, offer)
