from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="729566be-e569-555f-9262-48736d25a7f5",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonVMAX.Name",
    display_name="Sylveon VMAX",
    searchable_by=["Sylveon VMAX", "VMAX", "Rapid Strike", "SylveonVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=75,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonV.Name",
    family_id=700,
    abilities=[
        Attack(
            title="Precious Touch",
            game_text="Attach an Energy card from your hand to 1 of your Benched Pok\u00e9mon. If you do, heal 120 damage from that Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Max Harmony",
            game_text="This attack does 30 more damage for each different type of Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)