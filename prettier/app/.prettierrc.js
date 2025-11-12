const config = {
  plugins: [
    require.resolve("@prettier/plugin-php"),
    require.resolve("@prettier/plugin-xml"),
    require.resolve("prettier-plugin-java"),
    require.resolve("prettier-plugin-nginx"),
    require.resolve("prettier-plugin-sh"),
    require.resolve("prettier-plugin-sql"),
    require.resolve("prettier-plugin-toml"),
  ],
};

module.exports = config;
