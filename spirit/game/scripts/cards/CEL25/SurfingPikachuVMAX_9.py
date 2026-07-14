from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage

card = PokemonCardDef(
    guid="fa92a5b1-0306-59dd-b692-cdebfc9985c9",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SurfingPikachuVMAX.Name",
    display_name="Surfing Pikachu VMAX",
    searchable_by=["Surfing Pikachu VMAX", "VMAX", "SurfingPikachuVMAX"],
    subtypes=["VMAX"],
    collector_number=9,
    set_code="CEL25",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SurfingPikachuV.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Max Surfer",
            game_text="This attack also does 30 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3},
            damage=160,
            effect=spread_damage(30, side="opponent", also_base=True),
        ),
    ],
)