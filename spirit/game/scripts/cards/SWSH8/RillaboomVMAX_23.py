from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="f84cab2e-275e-5666-a8cd-08a381634e38",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomVMAX.Name",
    display_name="Rillaboom VMAX",
    searchable_by=["Rillaboom VMAX", "VMAX", "Rapid Strike", "RillaboomVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=23,
    set_code="SWSH8",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomV.Name",
    family_id=812,
    abilities=[
        Attack(
            title="G-Max Drum Solo",
            game_text="This attack also does 40 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=snipe_attack(40, pool="bench", count=2, also_base=True),
        ),
    ],
)