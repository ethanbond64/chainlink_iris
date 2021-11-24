import datetime
import os


class ContractWriter:

    def __init__(self,name,event_id,env):
        # Contract name for reference
        self.name = name
        # Event Id to fill into api
        self.event_id = event_id
        # JSON blob that contains sensitive data
        # TODO learn how to handle sensitive data in smart contract
        self.env = env

        self.base_dir = os.path.dirname(__file__)
        self.filename = ""

    # Tie it all together
    def write(self):
        
        # generate filename
        self.filename = (self.name+str(datetime.datetime.now())).replace(" ","")+".sol"

        contents = self.fill_template()

        with open(self.base_dir+"/generated_sol/"+self.filename, "w+") as file:
            file.write(contents)

        return self.filename
    
    # save the file as a real sol file in a gen file 
    def fill_template(self):
        contents = None
        
        with open('env_template.json','r') as template:
            contents = template.read()

        for field in self.env:
            contents.replace("{% "+field+" %}",self.env[field])

        contents.replace("{% event_id %}",self.event_id)

        return contents

    # Optional getter to view the text
    def get_contract_text():
        # TODO
        return