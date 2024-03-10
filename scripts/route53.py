import boto3
import json

def add_static_website_bucket(domain:str, s3_client:object):
    s3_client.create_bucket(
        Bucket=domain,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-southeast-2' 
        }
    )

    # Update the bucket's public access configuration
    s3_client.put_public_access_block(
        Bucket=domain,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': False,
            'IgnorePublicAcls': False,
            'BlockPublicPolicy': False,
            'RestrictPublicBuckets': False
        }
    )

    # Enable website hosting
    website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'},
    }
    s3_client.put_bucket_website(
        Bucket=domain,
        WebsiteConfiguration=website_configuration
    )
    print(f"Website hosting enabled for bucket: {domain}")
    # Add policy allowing internet access to the domain bucket
    policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "AddPerm",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                f"arn:aws:s3:::{domain}/*"
            ]
        }]
    }
    # Convert the policy from a Python dict to a JSON string
    policy_json = json.dumps(policy)
    # Apply the policy to the bucket
    s3_client.put_bucket_policy(Bucket=domain, Policy=policy_json)
    print(f"Policy added to bucket: {domain}")
    

        
def configure_route_53(hosted_zone_name:str, s3_website_endpoint:str, route53_client:object):
    # Create Route 53 hosted zone
    route53_response = route53_client.create_hosted_zone(
        Name=hosted_zone_name,
        CallerReference='u9xx]987sif',  # A unique string used to ensure idempotent requests
        HostedZoneConfig={
            'Comment': 'Hosted zone for react news ag',
            'PrivateZone': False
        }
    )
    hosted_zone_id = route53_response['HostedZone']['Id']
    # Create the alias record
    """
    change_resource_record_set():Creates, changes, or deletes a resource record set, which contains authoritative DNS
    information for a specified domain name or subdomain name. For example, you can use
    ChangeResourceRecordSets to create a resource record set that routes traﬃc for
    test.example.com to a web server that has an IP address of 192.0.2.44.
    @see https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/client/change_resource_record_sets.html#
    """
    

    response = route53_client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id, # required
        ChangeBatch={ # required
            'Comment': 'Adding alias record to S3 website endpoint', # optional
            'Changes': [ # required
                {
                    'Action': 'CREATE', # required
                    'ResourceRecordSet': { # required
                        'Name': domain,
                        'Type': 'A',  # Alias record, @see https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html
                        'AliasTarget': {
                            'HostedZoneId': hosted_zone_id,  # Required. This is the hosted zone ID for S3 websites (This value is for the ap-southeast-2 region; it may vary)
                            'DNSName': f'{s3_website_endpoint}',
                            'EvaluateTargetHealth': False
                        }
                    }
                }
            ]
        }
    )
    print(response)


    

def remove_bucket(domain:str, s3_client:object):
    s3_client.delete_bucket(
        Bucket=domain
    )    
    
s3_client = boto3.client('s3')
domain = "kevindaviesnz.github.io"
subdomain = "reactnewsag.kevindaviesnz.github.io"
hosted_zone_name = "kevindaviesnz2.github.io.s3-website-ap-southeast-2.amazonaws.com."
# S3 website endpoint (Do not use "http://" or "https://", just the domain)
s3_website_endpoint = 's3-website-ap-southeast-2.amazonaws.com'
route53_client = boto3.client('route53')
    
#add_static_website_bucket(domain=domain, s3_client=s3_client)
#add_static_website_bucket(domain=subdomain, s3_client=s3_client)
configure_route_53(hosted_zone_name=hosted_zone_name, s3_website_endpoint=s3_website_endpoint, route53_client=route53_client)
# remove_bucket(domain=domain, s3_client=s3_client)
#remove_bucket(domain=subdomain, s3_client=s3_client)



