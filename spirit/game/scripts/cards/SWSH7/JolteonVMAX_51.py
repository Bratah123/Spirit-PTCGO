from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7808eee-95b1-56b3-9cbb-d890fe3aa74c",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonVMAX.Name",
    display_name="Jolteon VMAX",
    searchable_by=["Jolteon VMAX", "VMAX", "JolteonVMAX"],
    subtypes=["VMAX"],
    collector_number=51,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonV.Name",
    family_id=135,
    abilities=[
        Attack(
            title="Max Thunder Rumble",
            game_text="This attack also does 100 damage to 1 of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)