from app import generate_welcome_message

def test_gen_welcome_msg():
    result = generate_welcome_message()

    assert result == "Welcome to DHBW"