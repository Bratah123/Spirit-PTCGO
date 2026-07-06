from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bafdf6dd-960c-5255-b2a8-8fdf3249a08a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianStunfisk.Name",
    display_name="Galarian Stunfisk",
    searchable_by=["Galarian Stunfisk", "Basic", "GalarianStunfisk"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=618,
    abilities=[
        Attack(
            title="Field Trap",
            game_text="If your opponent has a Stadium in play, discard it. If you discarded a Stadium in this way, discard 2 Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)