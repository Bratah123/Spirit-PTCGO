from spirit.game.card_effects.attacks_common import count_energy, flip_damage
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e50b35b7-2c7e-5a0d-adaa-596ea8925d34",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CramorantVMAX.Name",
    display_name="Cramorant VMAX",
    searchable_by=["Cramorant VMAX", "VMAX", "CramorantVMAX"],
    subtypes=["VMAX"],
    collector_number=55,
    set_code="SWSH45",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CramorantV.Name",
    family_id=845,
    abilities=[
        Attack(
            title="Max Jet",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy("self"), per_heads=80),
        ),
    ],
)