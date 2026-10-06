import trimesh

from slicing_functions import repair_mesh_with_windows


mesh = trimesh.load_mesh(
    "./holey.stl",
    process=False
)

print("Original:")
print("vertices:", len(mesh.vertices))
print("faces:", len(mesh.faces))
print("watertight:", mesh.is_watertight)

repaired = repair_mesh_with_windows(mesh)

print("\nRepaired:")
print("vertices:", len(repaired.vertices))
print("faces:", len(repaired.faces))
print("watertight:", repaired.is_watertight)