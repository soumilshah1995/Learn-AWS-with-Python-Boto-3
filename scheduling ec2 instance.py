__Author__ = 'Soumil Nitin Shah'
__Version__ = "0.0.1"
__Email__ = "soushah@mt.bridgeport.edu"
__Github__ = "https://github.com/soumilshah1995?tab=repositories"


try:
    import boto3
    print("All Modules are Loaded ......")
except Exception as e:
    print("Some Modules are missings {}".format(e))


class EC2Master(object):

    def __init__(self):
        self.client = boto3.client('ec2')

    def stop(self, InstanceId = []):
        """

        :param InstanceId: List of Instance ID
        :return:
        """
        response = self.client.stop_instances(
            InstanceIds=InstanceId)
        return response

    def get_instanceid(self):
        """
        :return: List of Instance ID
        """
        id = []
        response = self.client.describe_instances()

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                id.append(instance["InstanceId"])
        return id

    def start(self, InstanceId = []):
        """

        :param InstanceId: List of Instance ID
        :return:
        """
        response = self.client.start_instances(
            InstanceIds=InstanceId)
        return response


if __name__ == "__main__":
    obj = EC2Master()

    # Instance ID in a List
    data = obj.get_instanceid()
    print("Instance Id {}".format(data))

    # start the EC2 Machine
    obj.stop(InstanceId=data)
    print("Machine is Turned On ... . .. . ")






