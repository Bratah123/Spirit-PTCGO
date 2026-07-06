from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0b78ab70-a9d8-55b0-b36f-f25ef5471dbf",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inteleon.Name",
    display_name="Inteleon",
    searchable_by=["Inteleon", "Stage 2", "Rapid Strike", "Inteleon"],
    subtypes=["Stage 2", "Rapid Strike"],
    collector_number=43,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    family_id=816,
    abilities=[
        Ability(
            title="Quick Shooting",
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)