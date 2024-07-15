from ginger.db import models



envs = (
    
        ("dev", "dev"),
    
        ("stage", "stage"),
    
        ("prod", "prod"),
    
)




class dbschema(models.Model):
        """DB Schema"""
    
    
     
        name = models.CharField(  max_length=100,         )
    
     
        description = models.CharField(  max_length=500,     blank=True,null=True,     )
    
     
        version = models.CharField(  max_length=10,         )
    
     
        created_at = models.DateTimeField(         auto_now_add=True,  )
    
     
        updated_at = models.DateTimeField(        auto_now=True,   )
    
     
        data = models.TextField(  max_length=10000,         )
    
     
        group_id = models.CharField(  max_length=500,         )
    
        class Meta:
            db_table = "dbschema"




class dbschema_branch(models.Model):
        """"""
    
    
     
        parent = models.ForeignKey('dbschema',related_name = 'definitions', on_delete=models.CASCADE,          )
    
     
        branch_name = models.CharField(  max_length=100,         )
    
     
        data = models.TextField(  max_length=10000,         )
    
     
        created_at = models.DateTimeField(         auto_now_add=True,  )
    
     
        updated_at = models.DateTimeField(        auto_now=True,   )
    
     
        merged = models.BooleanField(default=False,          )
    
        class Meta:
            db_table = "dbschema_branch"




class templates(models.Model):
        """All templates are public"""
    
    
     
        short_name = models.CharField(  max_length=100,         )
    
     
        description = models.TextField(  max_length=600,         )
    
     
        repo_link = models.CharField(  max_length=100,         )
    
     
        identifier = models.CharField(  max_length=40,         )
    
        class Meta:
            db_table = "templates"




class service(models.Model):
        """"""
    
    
     
        identifier = models.CharField(  max_length=50,         )
    
     
        group_id = models.CharField(  max_length=100,     blank=True,null=True,     )
    
        class Meta:
            db_table = "service"




class service_envs(models.Model):
        """"""
    
    
     
        parent = models.ForeignKey('service',related_name = 'envs', on_delete=models.CASCADE,          )
    
     
        spec = models.TextField(  max_length=10000,         )
    
     
        env = models.CharField( choices=envs, max_length=10,         )
    
     
        base_url = models.CharField(  max_length=100,         )
    
        class Meta:
            db_table = "service_envs"



