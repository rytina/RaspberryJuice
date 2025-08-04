# Building RaspberryJuice for Minecraft 1.20+

This document provides detailed instructions for building RaspberryJuice with Java 21 and Minecraft 1.20+ support.

## Prerequisites

### Required Software
- **Java 21+**: Download from [Eclipse Temurin](https://adoptium.net/) or [Oracle](https://www.oracle.com/java/technologies/downloads/)
- **Maven 3.6+**: Download from [Apache Maven](https://maven.apache.org/download.cgi)
- **Git**: For cloning the repository

### Verify Installation
```bash
java -version    # Should show version 21 or higher
mvn -version     # Should show Maven 3.6+ and Java 21+
```

## Building

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rytina/RaspberryJuice.git
   cd RaspberryJuice
   ```

2. **Build the plugin:**
   ```bash
   mvn clean package
   ```

3. **Locate the built JAR:**
   The plugin JAR will be created in `target/raspberryjuice-1.20.0.jar`

## Installation

1. **Copy to server:**
   Copy `target/raspberryjuice-1.20.0.jar` to your Minecraft server's `plugins/` directory

2. **Start server:**
   Start your Minecraft 1.20+ server (Bukkit/Spigot/Paper)

3. **Configure:**
   Edit `plugins/RaspberryJuice/config.yml` as needed

## Compatible Servers

- **Bukkit** 1.20+
- **Spigot** 1.20+
- **Paper** 1.20+ (recommended)
- **Purpur** 1.20+

## Dependencies

The plugin uses the following main dependencies:

- **Paper API 1.20.1**: For Minecraft server integration
- **Java 21**: For runtime compatibility

All dependencies are automatically downloaded by Maven during build.

## Troubleshooting

### Build Issues

**"Unsupported class file major version"**
- Ensure you're using Java 21+

**"Could not resolve dependencies"**
- Check internet connection
- Try `mvn clean package -U` to force dependency updates

**"JAVA_HOME not set"**
- Set JAVA_HOME environment variable to your Java 21 installation

### Runtime Issues

**"UnsupportedClassVersionError"**
- Ensure your Minecraft server is running on Java 21+

**"Plugin failed to load"**
- Verify server is Minecraft 1.20+ compatible
- Check server logs for specific error messages

## Development

For development work:

```bash
# Compile only
mvn clean compile

# Run tests
mvn test

# Create development build
mvn clean package -DskipTests
```