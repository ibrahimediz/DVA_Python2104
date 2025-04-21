class Polygon:
    def __init__(self, name, edge_count):
        self.name = name
        self.edge_count = edge_count
        self.interior_angle_sum = (edge_count - 2) * 180

    def bilgi(self):
        print("#"*30)
        print("Adı:",self.name)
        print("Kenar Sayısı:",self.edge_count)
        print("Açı Toplam:",self.interior_angle_sum)
        print("#"*30)

triangle = Polygon('a',6)
triangle.bilgi()