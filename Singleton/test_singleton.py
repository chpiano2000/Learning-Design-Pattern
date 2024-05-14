from .singleton import RoundRobin

# Initialize instances
lb1 = RoundRobin()
lb2 = RoundRobin()

# Add servers to the load balancer
lb1.add_server("1")
lb1.add_server("2")
lb1.add_server("3")


def test_one_instance():
    # Check if the two instances are the same
    assert lb1 == lb2


def test_round_robin():
    # Test get_next_server method
    expected_results = ["1", "2", "3", "1", "2"]
    testing_results = []
    for _ in range(5):
        testing_results.append(lb1.get_next_server())

    print(testing_results)
    assert len(testing_results) == len(expected_results)
    assert all([a == b for a, b in zip(testing_results, expected_results)])
