import fire

class Instance():
    def __init__(self, instance_name):
        self.instance_name=instance_name

    def echo_name(self):
        msg = f'Hello world from {self.instance_name}'
        print(msg)

def start_exec(name='give_me_name', **kwargs):
    instance = Instance(instance_name=name)
    instance.echo_name()

if __name__ == '__main__':
    # run() -> error because cant recieve argument from CLI
    fire.Fire(start_exec)