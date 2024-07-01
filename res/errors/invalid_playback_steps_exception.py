class Invalid_playback_steps_exception(Exception):
    def __init__(self, playback_steps):
        self.message = f"Invalid playback steps {playback_steps}"
        super().__init__(self.message)