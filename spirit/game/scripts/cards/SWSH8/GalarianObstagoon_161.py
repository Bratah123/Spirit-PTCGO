from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b651cb52-3dac-5464-9504-ecf2a75e8ebd",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianObstagoon.Name",
    display_name="Galarian Obstagoon",
    searchable_by=["Galarian Obstagoon", "Stage 2", "GalarianObstagoon"],
    subtypes=["Stage 2"],
    collector_number=161,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Silence",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks. During your opponent's next turn, that Pok\u00e9mon can't use that attack.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Merciless Strike",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 90 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)