import PyQt5.QtWidgets as qw 
from PyQt5 import uic
import sys 
from PyQt5.QtGui import QPixmap
import networkx as nx
import json
import networkx as nx
import json
import matplotlib.pyplot as plt
import networkx as nx 
import random  
from tkinter.filedialog import askopenfilename,asksaveasfilename
fnum=0
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def read_data()->dict:
    # Opening JSON file
    fname=askopenfilename(
    title="Select JSON file",
    filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
    f = open(f'{fname}')
    
    return dict(json.load(f))
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def save_data( dictionary):
    global fnum
    fname = asksaveasfilename(
    initialfile=f"Automata_{fnum}_.json",
    defaultextension=".json",
    filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
)
    fnum+=1
    with open(fname, "w") as outfile:
        json.dump(dictionary, outfile)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def cartesian_product(A1, A2):
    product = {
        "states": [],
        "labels": A1["labels"] + A2["labels"],
        "transitions": [],
        "initial_state": (A1["initial_state"]+','+ A2["initial_state"]),
        "finaly_states": []
    }
    
    # Calculate Cartesian product of states
    for state1 in A1["states"]:
        for state2 in A2["states"]:
            product["states"].append((state1+','+ state2))
    
    # Calculate Cartesian product of transitions
    for transition1 in A1["transitions"]:
        for transition2 in A2["transitions"]:
            from_state1, to_state1, label1 = transition1
            from_state2, to_state2, label2 = transition2
            
            from_state_product = (from_state1+','+ from_state2)
            to_state_product = (to_state1+','+ to_state2)
            label_product = label1 + label2
            
            product["transitions"].append([from_state_product, to_state_product, label_product])

    for i in product["states"]:
            s=i.split(',')
            if s[0] in A1["finaly_states"] or s[1] in A2["finaly_states"]:
                product["finaly_states"].append(i)
    
    return product
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def plot_automata(A,name):
    r=lambda a,b:random.randint(a,b)
    d={}
    t=[(i[0],i[1]) for i in  A["transitions"]]
    for i in range(len(A["transitions"])): 
        d[t[i]]=A["transitions"][i][2]
    g=nx.DiGraph()
    for i in A["states"]:
        if i in A['initial_state']:
            g.add_node(i,node_color='#0f0')
        elif i in A['finaly_states']:
            g.add_node(i,node_color='red')
        else :
            g.add_node(i,node_color='black')
    g.add_edges_from(t)
    node_colors = [g.nodes[node]['node_color'] for node in g.nodes()]
    pos = nx.spring_layout(g)
    k=plt.figure(figsize=(8,4))
    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_edges(g,pos)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=d,font_color='blue' ,font_family='Arial',font_weight='bold')

    nx.draw(g,pos,font_color='yellow', node_color=node_colors,with_labels=True,font_weight='bold',edge_color='purple')
    # Set the background color
    k.set_facecolor('#acf')

    
    
    plt.title(f'{name}')
    plt.savefig(f"{name}.png")




# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



class Add_edge(qw.QMainWindow):
    
    def __init__(self,stats,labels):
        super(Add_edge, self).__init__()

        uic.loadUi('add_edge.ui', self)
        self.setWindowTitle('Add_edge')
        self.n1=self.findChild(qw.QComboBox,'fr')
        self.n2=self.findChild(qw.QComboBox,'to')
        for i in stats:
            self.n1.addItem(i)
            self.n2.addItem(i)
        self.l=self.findChild(qw.QComboBox,'by')
        for i in labels:
            self.l.addItem(i)
        self.submit=self.findChild(qw.QPushButton,'submit')
        self.show()
    def get_data(self):
        data=[self.n1.currentText(),self.n2.currentText(),self.l.currentText()]
        return data
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class Add_node(qw.QMainWindow):
    
    def __init__(self):

        super(Add_node, self).__init__()
        
        uic.loadUi('add_node.ui', self)
        self.name=self.findChild(qw.QLineEdit,'name')
        
        self.setWindowTitle('Add_node')
        self.submit=self.findChild(qw.QPushButton,'submit')
        self.type=self.findChild(qw.QComboBox,'c')
        self.type.addItem("states")
        self.type.addItem("initial_state")
        self.type.addItem("finaly_state")
        self.show()
    def get_state(self):
        return self.name.text()
    def get_type(self):
        return self.type.currentText()
    def get_data(self):
        data={'name': self.get_state(),'type': self.get_type()}
        return data
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class New_Automata (qw.QMainWindow):
    def __init__(self):
        super(New_Automata, self).__init__()

        uic.loadUi('NEW.ui', self)
        self.setWindowTitle('New_Automata')
        self.l1=self.findChild(qw.QLineEdit,'l1')
        self.l2=self.findChild(qw.QLineEdit,'l2')
        self.l3=self.findChild(qw.QLineEdit,'l3')
        self.l4=self.findChild(qw.QLineEdit,'l4')

        self.submit=self.findChild(qw.QPushButton,'s')
        self.show()
    def get_stats(self):
        return list(set(self.l1.text().split(',')))
    def get_labels(self):
        return list(set(self.l2.text().split(',')))
    def get_initial_stats(self):
        return list(set(self.l3.text().split(',')))
    def get_finaly_stats(self):
        return list(set(self.l4.text().split(',')))
    def get_data(self):
        data={"states":self.get_stats(),'labels':self.get_labels(),"transitions":[],
              "initial_state":self.get_initial_stats(),
              'finaly_states':self.get_finaly_stats()}
        return data


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


class UI(qw.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi('main.ui', self)
        self.setWindowTitle('TP 0 7 MEPS')
        self.Automata1= {
                            "states":[],
                            "labels":[],
                            "transitions":[],
                            "initial_state":[],
                            "finaly_states":[]
                        }
        self.Automata2= {
                            "states":[],
                            "labels":[],
                            "transitions":[],
                            "initial_state":[],
                            "finaly_states":[]
                        }
        self.Automata3= {
                            "states":[],
                            "labels":[],
                            "transitions":[],
                            "initial_state":[],
                            "finaly_states":[]
                        }
        self.lable1=self.findChild(qw.QLabel,'l1')
        self.label2=self.findChild(qw.QLabel,'l2')
        self.label3=self.findChild(qw.QLabel,'l3')
        self.b_prodect=self.findChild(qw.QPushButton,'b_prodect')
        self.save1=self.findChild(qw.QPushButton,'save1')
        self.save2=self.findChild(qw.QPushButton,'save2')
        self.save3=self.findChild(qw.QPushButton,'save3')
        self.add_e1=self.findChild(qw.QPushButton,'b_add_e1')
        self.add_e2=self.findChild(qw.QPushButton,'b_add_e2')
        self.add_n1=self.findChild(qw.QPushButton,'b_add_n1')
        
        self.add_n2=self.findChild(qw.QPushButton,'b_add_n2')
        self.new1=self.findChild(qw.QPushButton,'b_new1')
        self.new2=self.findChild(qw.QPushButton,'b_new2')
        self.open1=self.findChild(qw.QPushButton,'b_open1')
        self.open2=self.findChild(qw.QPushButton,'b_open2')
        self.show()
    def update(self):
        plot_automata(self.Automata1,'A1')
        plot_automata(self.Automata2,'A2')
        plot_automata(self.Automata3,'A3')
        pixmap2=QPixmap("A2.png")
        self.label2.setPixmap(pixmap2) 
        pixmap1=QPixmap("A1.png")
        self.lable1.setPixmap(pixmap1)
        pixmap3=QPixmap("A3.png")
        self.label3.setPixmap(pixmap3)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def set_prodect(self):
        self.Automata3=cartesian_product(self.Automata1,self.Automata2)
        self.update()
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    def set_Automata1(self, automata):
        self.Automata1=automata
        self.update()
    def set_Automata2(self, automata):
        self.Automata2=automata
        self.update()
    def set_Automata3(self, automata):
        self.Automata3=automata
        self.update()
    def set_open1(self):
        self.Automata1=read_data()
        self.update()
    def set_open2(self):
        self.Automata2=read_data()
        self.update()
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def set_add_node1(self):
        self.an1=Add_node()
        
        self.an1.submit.clicked.connect(lambda:self.get_node1(self.an1.get_data()))

        self.update()
    def get_node1(self, a):

        self.Automata1[str(a['type'])].append(a['name'])  
        self.Automata1[str(a['type'])]=list(set(self.Automata1[str(a['type'])]))  

        self.Automata1['states'].append(a['name'])
        self.Automata1['states']=list(set(self.Automata1['states']))
        self.update()
        self.an1.hide() 
    def set_add_node2(self):
        self.an2=Add_node()
        
        self.an2.submit.clicked.connect(lambda:self.get_node2(self.an2.get_data()))

        self.update()
    def get_node2(self, a):

        self.Automata2[str(a['type'])].append(a['name'])  
        self.Automata2[str(a['type'])]=list(set(self.Automata2[str(a['type'])]))  

        self.Automata2['states'].append(a['name'])
        self.Automata2['states']=list(set(self.Automata2['states']))
        self.update()
        self.an2.hide() 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def set_new_Automata1(self):
        self.nnn1=New_Automata()
        self.nnn1.submit.clicked.connect(lambda:self.get_Automata1(self.nnn1.get_data()))
        self.update()
    def get_Automata1(self, data):
        self.Automata1=data
        self.update()
        self.nnn1.hide()
    def set_new_Automata2(self):
        self.nnn2=New_Automata()
        self.nnn2.submit.clicked.connect(lambda:self.get_Automata2(self.nnn2.get_data()))
        self.update()
    def get_Automata2(self, data):
        self.Automata2=data
        self.update()
        self.nnn2.hide()

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def set_add_edge1(self):
        s=list(self.Automata1["states"])
        l=list(self.Automata1["labels"])
        t=list(self.Automata1['transitions'])
        self.a1=Add_edge(s,l)
        
        self.a1.submit.clicked.connect(lambda:self.getdata1(self.a1.get_data()))

        self.update()
    def getdata1(self, a):
        t=list(self.Automata1['transitions'])
        t.append(a)
        self.Automata1['transitions']=list(set(t))    
        self.update()
        self.a1.hide()  
    def set_add_edge2(self):
        s=list(self.Automata2["states"])
        l=list(self.Automata2["labels"])
        t=list(self.Automata2['transitions'])
        self.a2=Add_edge(s,l)
        
        self.a2.submit.clicked.connect(lambda:self.getdata2(self.a2.get_data()))

        self.update()
    def getdata2(self, a):
        t=list(self.Automata2['transitions'])
        t.append(a)
        self.Automata2['transitions']=list(set(t))      
        self.update()
        self.a2.hide()  
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
A1 = {
    "states":['q0', 'q1', 'q2', 'q3'],
    "labels":['0', '1'],
    "transitions":[
        ['q0','q1','0'],
        ['q0','q3','1'],
        ['q1','q2','0'],
        ['q1','q1','1'],
        ['q2','q3','0'],
        ['q2','q0','1'],
        ['q3','q3','0'],
        ['q3','q2','1']
    ],
    "initial_state":'q0',
    "finaly_states":['q3']
}
A2 = {
    "states":['s0', 's1', 's2', 's3'],
    "labels":['0', '1'],
    "transitions":[
        ['s0','s1','0'],
        ['s0','s3','1'],
        ['s1','s2','0'],
        ['s1','s1','1'],
        ['s2','s3','0'],
        ['s2','s0','1'],
        ['s3','s3','0'],
        ['s3','s1','1']
    ],
    "initial_state":'s0',
    "finaly_states":['s3']
}



if __name__ == '__main__':
    app=qw.QApplication(sys.argv)
    mw=UI()
    mw.set_Automata1(A1)
    mw.set_Automata2(A1)
    mw.set_Automata3(A1)

    mw.open1.clicked.connect(lambda:mw.set_open1())
    mw.open2.clicked.connect(lambda:mw.set_open2())
    mw.add_e1.clicked.connect(lambda:mw.set_add_edge1())
    mw.add_e2.clicked.connect(lambda:mw.set_add_edge2())
    mw.new1.clicked.connect(lambda:mw.set_new_Automata1())
    mw.new2.clicked.connect(lambda:mw.set_new_Automata2())
    mw.add_n1.clicked.connect(lambda:mw.set_add_node1())
    mw.add_n2.clicked.connect(lambda:mw.set_add_node2())
    mw.b_prodect.clicked.connect(lambda:mw.set_prodect())
    mw.save1.clicked.connect(lambda:save_data(mw.Automata1))
    mw.save2.clicked.connect(lambda:save_data(mw.Automata2))
    mw.save3.clicked.connect(lambda:save_data(mw.Automata3))

    app.exec_()

