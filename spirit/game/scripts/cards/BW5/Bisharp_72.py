from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4650a72f-62b7-53ce-a8f2-6ab460afca74",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp", "Stage 1", "Bisharp"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Fury Cutter",
            game_text="Flip 3 coins. If 1 of them is heads, this attack does 10 more damage. If 2 of them are heads, this attack does 30 more damage. If all of them are heads, this attack does 60 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)