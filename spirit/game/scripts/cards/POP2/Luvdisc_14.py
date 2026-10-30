from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    paralyzing_kiss_dual, fast_stream_move_energy_dual,
)


card = PokemonCardDef(
    guid="097a8656-d562-5182-9983-2bd38f4bd8f5",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name",
    display_name="Luvdisc",
    searchable_by=["Luvdisc", "Basic", "Luvdisc"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="POP2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=370,
    abilities=[
        Attack(
            title="Paralyzing Kiss",
            game_text="If there are 2 Defending Pokémon in play, choose 1 of the Defending Pokémon. That Pokémon is now Paralyzed. (If there is only 1 Defending Pokémon, this attack does nothing.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=paralyzing_kiss_dual(),
        ),
        Attack(
            title="Fast Stream",
            game_text="Move 1 Energy card attached to the Defending Pokémon to the other Defending Pokémon. (Ignore this effect if your opponent has only 1 Defending Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=fast_stream_move_energy_dual(),
        ),
    ],
)
