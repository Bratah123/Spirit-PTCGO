from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_special_energy
from spirit.game.card_effects.attacks_common import snipe_attack, bonus_if


def _has_special_energy(ctx) -> bool:
    return any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="09e45675-0e25-59f3-a42d-f3919594ce92",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagearnaV.Name",
    display_name="Magearna V",
    searchable_by=["Magearna V", "Basic", "V", "MagearnaV"],
    subtypes=["Basic", "V"],
    collector_number=128,
    set_code="SWSH12",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=801,
    abilities=[
        Attack(
            title="Gear Throw",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1},
            effect=snipe_attack(30, pool="any", count=1),
        ),
        Attack(
            title="Special Laser",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=bonus_if(_has_special_energy, 120),
        ),
    ],
)