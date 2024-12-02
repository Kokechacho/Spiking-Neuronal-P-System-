
import numpy as np

class Neuron:
    def __init__(self, id, initial_spikes=0):
        self.id = id
        self.spikes = initial_spikes
        self.rules = []  # Lista de reglas (spiking y forgetting)
        self.delay = 0   # Tiempo restante para que la neurona se vuelva activa

    def add_rule(self, rule_id, condition, spikes_in, spikes_out, delay=0):
        self.rules.append({
            "id": rule_id,
            "condition": condition,
            "spikes_in": spikes_in,
            "spikes_out": spikes_out,
            "delay": delay
        })

    def can_fire(self):
        if self.delay > 0:
            self.delay -= 1
            return None

        applicable_rules = []
        for rule in self.rules:
            if rule['condition']==None and self.spikes == rule['spikes_in']:
                applicable_rules.append(rule)
            elif rule['condition']!= None and self.spikes >= rule['condition']:
                applicable_rules.append(rule)

        return np.random.choice(applicable_rules) if applicable_rules else None

    def fire(self, rule):
        """Dispara una regla válida y actualiza el estado."""
        self.spikes -= rule["spikes_in"]
        self.delay = rule["delay"]
        return rule["spikes_out"], rule["id"]


class SNPSystem:
    def __init__(self):
        self.neurons = {}
        self.synapses = []
        self.ruleQueue = []

    def add_neuron(self, neuron):
        """Agrega una neurona al sistema."""
        self.neurons[neuron.id] = neuron

    def connect(self, source_id, target_id):
        """Conecta dos neuronas."""
        self.synapses.append((source_id, target_id))

    def propagate_spikes(self, neuron, rule):
        for source,target in self.synapses:
            if source == neuron.id and self.neurons[target].delay == 0 :
                self.neurons[target].spikes += rule['spikes_out']

    def apply_rules(self):
               # Segunda Pasada: Recorrer cola
        n = len(self.ruleQueue)
        for i in range(n):
            neuron, rule = self.ruleQueue.pop(0)
            if neuron.delay>0:
                self.ruleQueue.append((neuron, rule))
            elif rule and neuron.delay==0:
                self.propagate_spikes(neuron, rule)


    def step(self):
        """Simula un paso de tiempo de manera secuencial, manejando neuronas con delay."""

        # Primera pasada: añadir delays a las neuronas cerradas
        for _, neuron in self.neurons.items():

            rule = neuron.can_fire()
            if rule:
                if rule["delay"] > 0:
                    neuron.delay += rule["delay"]
                self.ruleQueue.append((neuron, rule))  # Asociar regla con neurona
                neuron.spikes -= rule["spikes_in"]
            else:
                self.ruleQueue.append((neuron, None))  # Ninguna regla aplicada

        return [rule[1]['id'] for rule in self.ruleQueue if rule[1] != None]

    def simulate(self, max_steps):
        """Simula múltiples pasos hasta que no haya reglas aplicables."""
        for t in range(max_steps):
            
            # Imprimir los estados actuales de las neuronas
            print(f"Step {t}:")
            for neuron_id, neuron in self.neurons.items():
                print(f"  Neuron {neuron_id}: spikes={neuron.spikes}, delay={neuron.delay}")
            
            # Realizar un paso de simulación
            rules_applied = self.step()
            
            # Imprimir las reglas aplicadas
            print(f"  Rules applied: {rules_applied}\n")
            
            # Si no se aplicó ninguna regla, detener simulación
            if not rules_applied:
                print("No more rules can be applied. Stopping simulation.")
                break

            self.apply_rules()


# Crear las neuronas con sus reglas nombradas
neuron1 = Neuron(id=1, initial_spikes=2)
neuron1.add_rule("r11", condition=2, spikes_in=1, spikes_out=1, delay=0)
neuron1.add_rule("r12", condition=None, spikes_in=1, spikes_out=0, delay=0)

neuron2 = Neuron(id=2, initial_spikes=1)
neuron2.add_rule("r21",  condition=None, spikes_in=1, spikes_out=1, delay=0)
neuron2.add_rule("r22",  condition=None, spikes_in=1, spikes_out=1, delay=1)

neuron3 = Neuron(id=3, initial_spikes=3)
neuron3.add_rule("r31",  condition=None, spikes_in=3, spikes_out=1, delay=0)
neuron3.add_rule("r32",  condition=None, spikes_in=1, spikes_out=1, delay=1)
neuron3.add_rule("r33",  condition=None, spikes_in=2, spikes_out=0, delay=0)

# Crear el sistema y conectar las neuronas según las sinapsis
snp = SNPSystem()
snp.add_neuron(neuron1)
snp.add_neuron(neuron2)
snp.add_neuron(neuron3)
snp.connect(1, 2)
snp.connect(2, 1)
snp.connect(1, 3)
snp.connect(2, 3)

# Simular el sistema hasta que no haya reglas aplicables
snp.simulate(10)
