from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.session.effects import is_special_energy


def _has_special_energy(ctx):
    return any(is_special_energy(c) for c in ctx.attached_energies(ctx.attacker))

card = PokemonCardDef(
    guid="0f9ce1b0-88d8-560f-b792-aa989c183fcb",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name",
    display_name="Wailord",
    searchable_by=["Wailord", "Stage 1", "Wailord"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    family_id=320,
    abilities=[
        Ability(
            title="Jumbo-Sized",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Special Wave",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=bonus_if(_has_special_energy, 120),
        ),
    ],
)