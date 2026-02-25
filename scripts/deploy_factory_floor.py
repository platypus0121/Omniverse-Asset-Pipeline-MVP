from pxr import Usd, UsdGeom, Gf
import omni.usd

stage = omni.usd.get_context().get_stage()

MODULE_ASSET_URL = r"C:/Users/qaq81/Desktop/AI_Server_Factory/KAT_Project/data/Assemblies/CL6_RowA_Racks.usda" 

# --- 廠房佈局數學參數 (單位：公分) ---
ROWS = 10             
GROUPS_PER_ROW = 2    

ROW_SPACING = 500.0     # 排跟排之間的距離：5m (500cm)
GROUP_SPACING = 1000.0  # 組跟組之間的距離：10m (1000cm)

root_path = "/World/Factory_Floor"
UsdGeom.Xform.Define(stage, root_path)

for row in range(ROWS):
    for col in range(GROUPS_PER_ROW):
        
        module_path = f"{root_path}/Row_{row}_Group_{col}"
        
        module_prim = stage.DefinePrim(module_path, "Xform")
        module_prim.GetReferences().AddReference(MODULE_ASSET_URL)
        
        module_prim.SetInstanceable(True)
        
        x_pos = col * GROUP_SPACING
        
        y_pos = row * ROW_SPACING

        xform_api = UsdGeom.XformCommonAPI(module_prim)
        xform_api.SetTranslate(Gf.Vec3d(x_pos, y_pos, 0.0))

print(f"Finish")