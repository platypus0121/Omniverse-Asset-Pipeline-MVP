from pxr import Usd, UsdGeom, Gf
import omni.usd

stage = omni.usd.get_context().get_stage()

RACK_ASSET_URL = r"C:/Users/qaq81/Desktop/AI_Server_Factory/KAT_Project/data/Assets/Machine_USD/ServerRack/a_server_rack.usdc" 

RACKS_PER_ROW = 10 
RACK_WIDTH = 60.0

RACK_DEPTH = 100.0
HOT_AISLE_GAP = 100.0
Y_OFFSET = (RACK_DEPTH + HOT_AISLE_GAP) / 2.0

root_path = "/World/Hot_Aisle_Zone"
UsdGeom.Scope.Define(stage, root_path)

for row in range(2):
    for i in range(RACKS_PER_ROW):
        
        rack_path = f"{root_path}/Rack_Row{row}_Num{i}"
        
        
        rack_prim = stage.DefinePrim(rack_path, "Xform")
        rack_prim.GetReferences().AddReference(RACK_ASSET_URL)
        
        
        rack_prim.SetInstanceable(True)
        
       
        x_pos = i * RACK_WIDTH
        
        if row == 0:
            y_pos = Y_OFFSET
            rotation_z = 180.0
        else:
            y_pos = -Y_OFFSET
            rotation_z = 0.0 
            
        xform_api = UsdGeom.XformCommonAPI(rack_prim)
        xform_api.SetTranslate(Gf.Vec3d(x_pos, y_pos, 0.0))
        xform_api.SetRotate(Gf.Vec3f(0.0, 0.0, rotation_z), UsdGeom.XformCommonAPI.RotationOrderXYZ)

print("Finish")