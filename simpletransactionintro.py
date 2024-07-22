from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class IntroduceBitcoinTransactions(VoiceoverScene):
    def construct(self):
        # set the speech synthesizer for the voiceover
        self.set_speech_service(
            AzureService(voice="en-US-JennyNeural", style="newscast")
        )
        # Create a rectangle for version
        rect1 = Rectangle()
        rect1.set_fill(BLUE, opacity=1)
        rect1.shift(LEFT)

        # Create a second rectangle outputs
        rect2 = Rectangle()
        rect2.set_fill(GRAY, opacity=1)
        rect2.next_to(rect1, RIGHT, buff=0.1)  # Position rect2 to the right of rect1


        # Create a third rectangle for outputs
        rect3 = Rectangle()
        rect3.set_fill(GREEN, opacity=1)
        rect3.next_to(rect2, RIGHT, buff=0.1)

        # Create a fourth rectangle for locktime
        rect4 = Rectangle()
        rect4.set_fill(YELLOW, opacity=1)
        rect4.next_to(rect3, RIGHT, buff=0.1)

        # create text for the rectangles
        version = Text("Version")
        inputs = Text("Inputs")
        outputs = Text("Outputs")
        locktime = Text("Locktime")

        

        # Scale the text to fit within the rectangles
        version.scale_to_fit_width(rect1.width * 0.8)
        inputs.scale_to_fit_width(rect2.width * 0.8)
        outputs.scale_to_fit_width(rect3.width * 0.8)
        locktime.scale_to_fit_width(rect4.width * 0.8)

        # Position the text in the center of the rectangles
        version.move_to(rect1.get_center())
        inputs.move_to(rect2.get_center())
        outputs.move_to(rect3.get_center())
        locktime.move_to(rect4.get_center())

          # Create a group of all the rectangles and text
        group = VGroup(rect1, version, rect2, inputs, rect3, outputs, rect4, locktime)

        # Scale the group to fit within the scene
        # group.scale_to_fit_width(self.camera.frame_width * 0.8)
        # group.scale_to_fit_height(self.camera.frame_height * 0.8)
        group.scale(0.5)
        group.to_edge(LEFT)

        with self.voiceover(
            """This is a source bitcoin transaction with a version, list of inputs, list of outputs, and a locktime. The output from first transaction is used as an input for the second transaction."""
        ):
            # Show the rectangles and text on screen
            self.play(Create(group))
            self.wait(5)
            
        with self.voiceover(
            """The new transaction uses the outputs of the previous transaction as inputs."""
        ):
            # Create a second group and place it under the first one
            group2 = group.copy()
            group2.next_to(group, DOWN, buff=0.5)

            # Draw an arrow from the output of the first group to the input of the second group
            arrow = Arrow(group[5].get_bottom(), group2[2].get_top())

            # Show the second group and the arrow on screen
            self.play(Create(group2), Create(arrow))
            self.wait(5)
        self.play(FadeOut(group))
        self.wait(5)
        self.play(FadeOut(group2), FadeOut(arrow))
        self.wait(5)

        # # Show the rectangles and text on screen
        # self.play(Create(rect1), Write(version), Create(rect2), Write(inputs), Create(rect3), Write(outputs), Create(rect4), Write(locktime))
        # self.wait(5)
        # self.play(FadeOut(rect1), FadeOut(version), FadeOut(rect2), FadeOut(inputs), FadeOut(rect3), FadeOut(outputs), FadeOut(rect4), FadeOut(locktime))
        # self.wait(5)
