from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _has_fusion_strike_energy(ctx):
    return any(
        "Fusion Strike" in subtypes_for(c.archetype_id)
        for c in ctx.attached_energies(ctx.attacker)
    )


card = PokemonCardDef(
    guid="af08582d-bde3-50d1-b090-a9016a286e8a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Fusion Strike", "Single Strike", "Rapid Strike", "Deoxys"],
    subtypes=["Basic", "Fusion Strike", "Single Strike", "Rapid Strike"],
    collector_number=120,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=386,
    abilities=[
        Attack(
            title="Photon Boost",
            game_text="If this Pok\u00e9mon has any Fusion Strike Energy attached, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_has_fusion_strike_energy, 80),
        ),
    ],
)