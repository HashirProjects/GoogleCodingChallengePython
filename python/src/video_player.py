"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video = {"title" : "" , "paused" : False}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        
        videoList = []

        for video in self._video_library.get_all_videos():

            tagStr = ""
            for tag in video.tags:
                tagStr += tag + " "
            tagStr = tagStr[:-1]

            videoList.append(f"  {video.title} ({video.video_id}) [{tagStr}]")

        videoList.sort()

        print("Here's a list of all available videos:")

        for video in videoList:
            print (video)


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        try:
            new_video_title = self._video_library.get_video(video_id).title

            if self.current_video["title"] != "":
                print(f"Stopping video: {self.current_video['title']}")

            self.current_video["title"] = new_video_title
            self.current_video["paused"] = False

            print(f"Playing video: {self.current_video['title']}")
        except:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        """Stops the current video."""
        if self.current_video["title"] == "":
            print("Cannot stop video: No video is currently playing")

        else:
            print(f"Stopping video: {self.current_video['title']}")
            self.current_video["title"] = ""
            self.current_video["paused"] = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        import random
        videoList = []

        for video in self._video_library.get_all_videos():

            videoList.append(video.title)

        if self.current_video["title"] != "":
                print(f"Stopping video: {self.current_video['title']}")

        self.current_video["title"]= random.choice(videoList)
        self.current_video["paused"]= False

        print(f"Playing video: {self.current_video['title']}")

    def pause_video(self):
        """Pauses the current video."""

        if self.current_video["title"] == "":
            print("Cannot pause video: No video is currently playing")

        elif self.current_video["paused"]:
            print(f"Video already paused: {self.current_video['title']}")

        else:
            self.current_video["paused"] = True
            print(f"Pausing video: {self.current_video['title']}")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.current_video["title"] == "":
            print("Cannot continue video: No video is currently playing")

        elif not self.current_video["paused"]:
            print(f"Cannot continue video: Video is not paused")

        else:
            self.current_video["paused"] = False
            print(f"Continuing video: {self.current_video['title']}")

    def show_playing(self):
        """Displays video currently playing."""

        if self.current_video["title"] == "":
            print("No video is currently playing")

        else:

            for video in self._video_library.get_all_videos():
                
                if video.title == self.current_video["title"]:
                    
                    tagStr = ""
                    for tag in video.tags:
                        tagStr += tag + " "
                    tagStr = tagStr[:-1]

                    if self.current_video["paused"]:

                        print(f"Currently playing: {video.title} ({video.video_id}) [{tagStr}] - PAUSED")

                    else:

                        print(f"Currently playing: {video.title} ({video.video_id}) [{tagStr}]")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
