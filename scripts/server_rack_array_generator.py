import omni.kit.commands
import omni.usd

context = omni.usd.get_context()
asset_path = "C:/PhysicalAI_SceneAssembly_Start/Factory/Assets/ServerRack_v5.usd"
for x in range(5):
    for y in range(5):
        pos_x = x * 100
        pos_y = y * 100

        prim_path = f'/World/Rack_{x}_{y}'
        omni.kit.commands.execute('CreateReferenceCommand',
            usd_context=context,
            path_to=prim_path,
            asset_path=asset_path,
            instanceable=True
        )

        # 2. 設定位置
        omni.kit.commands.execute('TransformPrimSRTCommand',
            path=prim_path,
            new_translation=(pos_x, pos_y, 0.0)
        )

print("25 racks finished assembling.")