from spirit.game.card_effects.attacks_common import bonus_if, condition_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.session.effects import is_special_energy


def _has_special_energy(ctx) -> bool:
    return any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker))

card = PokemonCardDef(
    guid="4185dc51-a9dd-5940-8a61-d2990e6b6bf8",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1", "Electivire"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=125,
    abilities=[
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Electrified Bolt",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=bonus_if(_has_special_energy, 90),
        ),
    ],
)