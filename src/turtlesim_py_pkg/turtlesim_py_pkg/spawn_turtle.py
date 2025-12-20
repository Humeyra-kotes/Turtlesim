#!/usr/bin/env python3
import rclpy
import random
import math

from rclpy.node import Node
from functools import partial
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from turtlesim_interfaces.msg import Turtle
from turtlesim_interfaces.msg import TurtleArray
from turtlesim_interfaces.srv import CatchTurtle

class SpawnTurtleNode(Node):
    def __init__(self):
        super().__init__("spawn_turtle_node")
        self.name_ = "turtle"
        self.counter_ = 0
        self.new_turtles_ = []

        self.new_turtles_publisher_ = self.create_publisher(TurtleArray, "new_turtles", 10)
        self.timer = self.create_timer(1.0, self.spawn_turtle)
        
        # ANA MANTIK: Dışarıdan (Avcıdan) gelen "yakaladım" bilgisini dinleyen servis
        self.catch_turtle_service = self.create_service(
            CatchTurtle, "catch_turtle", self.callback_catch_turtle)
        
        self.get_logger().info("Spawn Turtle Node başlatıldı.")

    def callback_catch_turtle(self, request, response):
        """Avcı kaplumbağa hedefe değdiğinde bu fonksiyon çalışır."""
        # 1. Kaplumbağayı ekrandan (turtlesim) sil
        self.call_kill_server(request.name)
        
        # 2. Kaplumbağayı hedef listesinden sil
        for (i, turtle) in enumerate(self.new_turtles_):
            if request.name == turtle.name:
                del self.new_turtles_[i]
                self.publish_new_turtles() # Listeyi güncelle ki avcı yeni hedefe gitsin
                break
                
        response.success = True
        return response
    
    def publish_new_turtles(self):
        msg = TurtleArray()
        msg.turtles = self.new_turtles_
        self.new_turtles_publisher_.publish(msg)

    def spawn_turtle(self):
        self.counter_ += 1
        turtle_name = self.name_ + str(self.counter_)
        x = random.uniform(1.0, 10.0)
        y = random.uniform(1.0, 10.0)
        theta = random.uniform(0.0, 2 * math.pi)
        self.call_spawn_turtle_server(x, y, theta, turtle_name)

    def call_spawn_turtle_server(self, x, y, theta, turtle_name):
        client = self.create_client(Spawn, "/spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Spawn servisi bekleniyor...")

        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = turtle_name

        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_spawn_turtle, x=x, y=y, theta=theta, turtle_name=turtle_name))

    def callback_call_spawn_turtle(self, future, x, y, theta, turtle_name):
        try:
            response = future.result()
            if response.name != "":
                new_turtle = Turtle()
                new_turtle.name = response.name
                new_turtle.x = x
                new_turtle.y = y
                new_turtle.theta = theta
                self.new_turtles_.append(new_turtle)
                self.publish_new_turtles()
        except Exception as e:
            self.get_logger().error("Spawn hatası: %r" % (e,))

    def call_kill_server(self, turtle_name):
        """Kaplumbağayı ekrandan tamamen yok eden fonksiyon."""
        client = self.create_client(Kill, "/kill")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Kill servisi bekleniyor...")

        request = Kill.Request()
        request.name = turtle_name
        client.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    node = SpawnTurtleNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()