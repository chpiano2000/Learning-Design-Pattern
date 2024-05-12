from proxy_interface import Personnel


class Leader(Personnel):
    def handle_request(self, offer) -> None:
        print("Leader received the request -->", offer)


class SecretaryProxy(Personnel):
    def __init__(self, leader: Leader) -> None:
        self._leader = leader

    def handle_request(self, offer) -> None:
        print("Secretary send to Leader -->", offer)
        self._leader.handle_request(offer)


def dev_request_for_promotion(personnel: Personnel, offer) -> None:
    personnel.handle_request(offer)
