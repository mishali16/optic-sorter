def build_pick_list(detections):
    actions = []
    for item in detections:
        label = item["label"]
        if label == "yellow_hazard":
            actions.append({"action": "avoid", "target": label, "center": item["center"]})
        elif label.endswith("_part"):
            color = label.split("_", 1)[0]
            actions.append({"action": "pick", "target": label, "destination": f"{color}_bin", "center": item["center"]})
        elif label.endswith("_bin"):
            actions.append({"action": "inspect", "target": label, "center": item["center"]})
    return actions
