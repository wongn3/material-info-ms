import time

def send_request(material):
    with open('material_info_request.txt', 'w') as file:
        file.write(f'material={material}')


# test 1: primary sand
send_request(
    material='sand'
)

time.sleep(5)

# test 2: primary grass
send_request(
    material='grass'
)

time.sleep(5)

# test 3: secondary wet sand
send_request(
    material='wet_sand'
)

time.sleep(5)

# test 4: secondary ash
send_request(
    material='ash'
)

time.sleep(5)

# test 5: empty
send_request(
    material=''
)

time.sleep(5)

# test 6: invalid material
send_request(
    material='grdshajyfs hera'
)