from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8d0567e8-2624-52e6-8abc-7ba26e335fe3",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoVMAX.Name",
    display_name="Morpeko VMAX",
    searchable_by=["Morpeko VMAX", "VMAX", "MorpekoVMAX"],
    subtypes=["VMAX"],
    collector_number=80,
    set_code="SWSH1",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoV.Name",
    family_id=877,
    abilities=[
        Attack(
            title="Max Discharge",
            game_text="This attack also does 20 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)