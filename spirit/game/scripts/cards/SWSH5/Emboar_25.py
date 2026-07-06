from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="19ccdd9a-83b9-50d9-9ef5-e3ca14d6bc9b",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emboar.Name",
    display_name="Emboar",
    searchable_by=["Emboar", "Stage 2", "Single Strike", "Emboar"],
    subtypes=["Stage 2", "Single Strike"],
    collector_number=25,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    family_id=498,
    abilities=[
        Ability(
            title="Fighting Fury Stance",
            game_text="Your Single Strike Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Heat Crash",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
    ],
)