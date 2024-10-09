import gradio as gr
import nodes
from nodes import NODE_CLASS_MAPPINGS
from nodes import load_custom_node

load_custom_node("custom_nodes/ALP")
LoadImage = NODE_CLASS_MAPPINGS["LoadImage"]()
ExpressionEditor = NODE_CLASS_MAPPINGS["ExpressionEditor"]()

def reset_parameters():
    return gr.update(value=0), gr.update(value=0), gr.update(value=0), gr.update(value=0), \
            gr.update(value=0), gr.update(value=0), gr.update(value=0), gr.update(value=0), \
            gr.update(value=0), gr.update(value=0), gr.update(value=0), gr.update(value=0)

def predict(image_path, rotate_pitch, rotate_yaw, rotate_roll, blink, eyebrow, wink, pupil_x, pupil_y, 
            aaa, eee, woo, smile):
    src_ratio=1.0
    sample_ratio=1.0
    sample_parts="OnlyExpression"
    crop_factor=1.7
    sample_image=None
    motion_link=None
    add_exp=None
    src_image = LoadImage.load_image(image_path)[0]
    result = ExpressionEditor.run(rotate_pitch, rotate_yaw, rotate_roll, blink, eyebrow, wink, pupil_x, pupil_y, aaa, eee, woo, 
                                    smile, src_ratio, sample_ratio, sample_parts, crop_factor, src_image, 
                                    sample_image, motion_link, add_exp)
    output_image = result['result'][0]
    return output_image

with gr.Blocks() as demo:
    with gr.Column(elem_id="col-container"):
        with gr.Row():
            with gr.Column():
                image = gr.Image(
                    label="Input image",
                    sources=["upload"],
                    type="filepath",
                    height=250
                )
                with gr.Tab("HEAD"):
                    with gr.Column():
                        rotate_pitch = gr.Slider(
                            label="Rotate Up-Down",
                            value=0,
                            minimum=-20, maximum=20
                        )
                        rotate_yaw = gr.Slider(
                            label="Rotate Left-Right turn", 
                            value=0,
                            minimum=-20, maximum=20
                        )
                        rotate_roll = gr.Slider(
                            label="Rotate Left-Right tilt", value=0,
                            minimum=-20, maximum=20
                        )
                with gr.Tab("EYES"):
                    with gr.Column():
                        eyebrow = gr.Slider(
                            label="Eyebrow", value=0,
                            minimum=-10, maximum=15
                        )
                        with gr.Row():
                            blink = gr.Slider(
                                label="Blink", value=0,
                                minimum=-20, maximum=5
                            )
                            
                            wink = gr.Slider(
                                label="Wink", value=0,
                                minimum=0, maximum=25
                            )
                        with gr.Row():
                            pupil_x = gr.Slider(
                                label="Pupil X", value=0,
                                minimum=-15, maximum=15
                            )
                            pupil_y = gr.Slider(
                                label="Pupil Y", value=0,
                                minimum=-15, maximum=15
                            )
                with gr.Tab("MOUTH"):
                    with gr.Column():
                        with gr.Row():
                            aaa = gr.Slider(
                                label="Aaa", value=0,
                                minimum=-30, maximum=120
                            )
                            eee = gr.Slider(
                                label="Eee", value=0,
                                minimum=-20, maximum=15
                            )
                            woo = gr.Slider(
                                label="Woo", value=0,
                                minimum=-20, maximum=15
                            )
                        smile = gr.Slider(
                            label="Smile", value=0,
                            minimum=-0.3, maximum=1.3
                        )
                with gr.Row():
                    reset_btn = gr.Button("Reset")
                    submit_btn = gr.Button("Submit")
            with gr.Column():
                result_image = gr.Image(elem_id="top", interactive=False)

    inputs = [image, rotate_pitch, rotate_yaw, rotate_roll, blink, eyebrow, wink, 
              pupil_x, pupil_y, aaa, eee, woo, smile]
    reset_btn.click(
        fn = reset_parameters,
        inputs = None,
        outputs = [rotate_pitch, rotate_yaw, rotate_roll, blink, eyebrow, wink, pupil_x, pupil_y, aaa, eee, woo, smile],
        queue = False
    ).then(
        fn=predict,
        inputs=inputs,
        outputs=[result_image],
        show_api=False
    )
    submit_btn.click(
        fn=predict,
        inputs=inputs,
        outputs=[result_image],
        show_api=False
    )
    rotate_pitch.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    rotate_yaw.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    rotate_roll.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    blink.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    eyebrow.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    wink.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    pupil_x.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    pupil_y.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    aaa.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    eee.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    woo.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)
    smile.release(fn=predict, inputs=inputs, outputs=[result_image], show_progress="minimal", show_api=False)

demo.queue(api_open=False).launch(share=False, show_error=True, show_api=False)