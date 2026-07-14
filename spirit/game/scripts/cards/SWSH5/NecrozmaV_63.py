from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_special_energy
from spirit.game.card_effects.attacks_common import bonus_if, snipe_attack


def _has_special_energy(ctx) -> bool:
    return any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="6891b982-6a9d-5ecf-a6f1-f93d9a05d1b9",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NecrozmaV.Name",
    display_name="Necrozma V",
    searchable_by=["Necrozma V", "Basic", "V", "NecrozmaV"],
    subtypes=["Basic", "V"],
    collector_number=63,
    set_code="SWSH5",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=800,
    abilities=[
        Attack(
            title="Prismatic Ray",
            game_text="This attack also does 20 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=snipe_attack(20, pool="bench", count=2, also_base=True),
        ),
        Attack(
            title="Special Laser",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=bonus_if(_has_special_energy, 120),
        ),
    ],
)