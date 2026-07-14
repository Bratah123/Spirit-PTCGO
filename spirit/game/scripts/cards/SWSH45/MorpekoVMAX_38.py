from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage

card = PokemonCardDef(
    guid="1d3d9134-27dd-5e42-99da-bfe219639d0a",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoVMAX.Name",
    display_name="Morpeko VMAX",
    searchable_by=["Morpeko VMAX", "VMAX", "MorpekoVMAX"],
    subtypes=["VMAX"],
    collector_number=38,
    set_code="SWSH45",
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
            effect=spread_damage(20, side="opponent", also_base=True),
        ),
    ],
)