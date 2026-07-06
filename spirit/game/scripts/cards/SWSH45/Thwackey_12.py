from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="77fb9e8a-b528-5742-82c1-995e38fcb067",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    display_name="Thwackey",
    searchable_by=["Thwackey", "Stage 1", "Thwackey"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SWSH45",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name",
    family_id=810,
    abilities=[
        Ability(
            title="Lay of the Land",
            game_text="If you have a Stadium in play, this Pok\u00e9mon has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Branch Poke",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)