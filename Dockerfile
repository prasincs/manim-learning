# Netlify Build Dockerfile for Manim Learning
# This image includes all system dependencies needed to render Manim animations

FROM python:3.11-slim-bullseye

# Install system dependencies in one layer to minimize image size
RUN apt-get update -qq && \
    apt-get install -y -qq --no-install-recommends \
    # LaTeX dependencies (required by Manim for text rendering)
    texlive \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-latex-recommended \
    texlive-science \
    texlive-fonts-recommended \
    cm-super \
    dvipng \
    # FFmpeg (required for video/GIF generation)
    ffmpeg \
    # Cairo and Pango (required for graphics rendering)
    libcairo2-dev \
    libpango1.0-dev \
    pkg-config \
    python3-dev \
    # Build tools
    gcc \
    g++ \
    make \
    # Utilities
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /opt/build/repo

# Install Python build tools
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Set environment variables for Manim
ENV MANIM_QUALITY=low_quality
ENV MANIM_FORMAT=gif
ENV PYTHONPATH=/opt/build/repo

# Create a simplified build script for Docker that only renders GIFs
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
echo "Starting GIF rendering in Docker..."\n\
echo ""\n\
\n\
# Create output directories\n\
mkdir -p public/previews/phase1\n\
mkdir -p public/previews/phase2\n\
mkdir -p media\n\
\n\
# Copy static files\n\
if [ -f "public_template/index.html" ]; then\n\
    cp public_template/index.html public/\n\
fi\n\
\n\
if [ -d "public_template/css" ]; then\n\
    cp -r public_template/css public/\n\
fi\n\
\n\
if [ -d "public_template/js" ]; then\n\
    cp -r public_template/js public/\n\
fi\n\
\n\
# Run the rendering\n\
bash scripts/render_all.sh\n\
\n\
echo ""\n\
echo "Build complete!"\n\
' > /opt/build/repo/docker-build.sh && chmod +x /opt/build/repo/docker-build.sh

# Default command - run the build
CMD ["bash", "/opt/build/repo/docker-build.sh"]
