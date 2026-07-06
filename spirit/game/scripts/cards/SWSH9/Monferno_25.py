from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fd88d2fd-aef3-5c2b-9d20-da63961f2668",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    display_name="Monferno",
    searchable_by=["Monferno", "Stage 1", "Monferno"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)