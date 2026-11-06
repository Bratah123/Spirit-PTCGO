from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.ecard import (
    CrystalTypePassive, crystal_type_on_energy_attached, dual_burn,
)


card = PokemonCardDef(
    guid="0639fd0e-4e6f-59f4-9800-31542847e784",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=148,
    set_code="ECARD2",
    rarity=Rarities.RareSecret,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Ability(
            title="Crystal Type",
            game_text="Whenever you attach a Water, Lightning, or Psychic basic Energy card from your hand to Kingdra, Kingdra's type (color) becomes the same as that Energy card type until the end of the turn.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=CrystalTypePassive(),
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=crystal_type_on_energy_attached(
                PokemonTypes.WATER, PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC,
            ),
        ),
        Attack(
            title="Aquabomb",
            game_text="Kingdra does 10 damage to itself. (Don't apply Weakness or Resistance when Kingdra damages itself with this attack.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.LIGHTNING: 1},
            damage=40,
            effect=recoil_attack(10),
        ),
        Attack(
            title="Dual Burn",
            game_text="Flip 2 coins. For each tails, discard 1 Energy card attached to Kingdra.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=dual_burn,
        ),
    ],
)
