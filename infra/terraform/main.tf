provider "aws" {
  region = "us-east-1"
}

resource "aws_ecs_cluster" "arbitrage_cluster" {}

resource "aws_ecs_task_definition" "arbitrage_task" {
  family                   = "arbitrage"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"
  memory                   = "1024"

  container_definitions = jsonencode([{
    name  = "arbitrage-engine"
    image = "your-cloud-repo/arbitrage-engine:latest"
    essential = true
    portMappings = [{ containerPort = 8000 }]
  }])
}

# Outputs and variables omitted for brevity
