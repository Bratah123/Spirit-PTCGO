from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.pokemon import energy_provides_type


def _has_psychic_energy(ctx):
    return any(energy_provides_type(e, PokemonTypes.PSYCHIC.value)
               for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="e7532c9b-05d1-5242-b6cf-16f9c363bf81",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard an Energy attached to this Pok\u00e9mon and heal all damage from it.",
            cost={PokemonTypes.WATER: 1},
            effect=heal_attack(all_damage=True, discard_energy=1),
        ),
        Attack(
            title="Core Splash",
            game_text="If this Pok\u00e9mon has any Psychic Energy attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_has_psychic_energy, 30, base=60),
        ),
    ],
)