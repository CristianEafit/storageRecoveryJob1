import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="job1", table_name="raw", transformation_ctx="S3bucket_node1"
)

# Script generated for node Filter
Filter_node1696634326538 = Filter.apply(
    frame=S3bucket_node1,
    f=lambda row: (bool(re.match("United States", row["country"]))),
    transformation_ctx="Filter_node1696634326538",
)

# Script generated for node S3 bucket
S3bucket_node2 = glueContext.write_dynamic_frame.from_options(
    frame=Filter_node1696634326538,
    connection_type="s3",
    format="csv",
    connection_options={"path": "s3://joblab1/trusted/", "partitionKeys": []},
    transformation_ctx="S3bucket_node2",
)

job.commit()
