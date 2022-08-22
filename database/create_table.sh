#!/bin/bash

psql -U postgres -f ./youtube_channel_stats.sql
psql -U postgres