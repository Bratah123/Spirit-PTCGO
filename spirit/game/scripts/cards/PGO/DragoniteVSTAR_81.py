from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a56db22e-4b35-56f3-ba94-732e42148400",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteVSTAR.Name",
    display_name="Dragonite VSTAR",
    searchable_by=["Dragonite VSTAR", "VSTAR", "DragoniteVSTAR"],
    subtypes=["VSTAR"],
    collector_number=81,
    set_code="PGO",
    rarity=Rarities.RareRainbow,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteV.Name",
    family_id=149,
    abilities=[
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=250,
            effect=unimplemented,
        ),
        Attack(
            title="Draconic Star",
            game_text="Look at the top 12 cards of your deck and attach any number of Water or Lightning Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)