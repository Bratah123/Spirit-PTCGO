from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4459f6d-7dd9-5796-bc17-da936eee7025",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardVMAX.Name",
    display_name="Charizard VMAX",
    searchable_by=["Charizard VMAX", "VMAX", "CharizardVMAX"],
    subtypes=["VMAX"],
    collector_number=74,
    set_code="SWSH35",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardV.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
        Attack(
            title="G-Max Wildfire",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 2},
            damage=300,
            effect=unimplemented,
        ),
    ],
)