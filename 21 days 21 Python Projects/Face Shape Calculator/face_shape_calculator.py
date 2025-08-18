print("🧠 Face Shape Calculator...\n")

print("Please enter the following measurments in *centimenters (cm)*:\n")

forhead=float(input("Forhead width: "))
cheekbones=float(input("Cheeckbone width: "))
jawline=float(input("Jawline width: "))
face_length=float(input("Face length (from hairline to chin): "))

shape="" 
if face_length>cheekbones and jawline <forhead:
    shape="Oval"
elif abs(cheekbones-face_length)<2 and abs(jawline-forhead)<2:
    shape="Round"
elif abs(forhead-cheekbones)<2 and (cheekbones-jawline)<2:
    shape="Square"
elif forhead>jawline and face_length>cheekbones:
    shape="Heart"
elif cheekbones>forhead and cheekbones>jawline:
    shape="Diamond"
else:
    shape="Unknown/Mixed"

print(f"\n Based on your measurments, your face shape is likely: **{shape}**")

with open('face_shape_file.txt','w',encoding='utf-8') as file:
    file.write(f"Forhead:{forhead},Cheekbones:{cheekbones},Jawline:{jawline},Face length:{face_length},Shape:{shape}\n")
